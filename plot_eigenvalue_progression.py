import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

from qibo.symbols import X,Y,Z
from qibo.hamiltonians import SymbolicHamiltonian
from qibo import set_backend
import random

random.seed(13)

# set the backend used for the calculation 
set_backend("numpy", platform=None)

# ----------------------------------------------------------------------------------------------------
#                       Generating the dataset
# ----------------------------------------------------------------------------------------------------

# Define the number of items
n_items = 6

# Define ranges
duration_range = [1, 7]
values_range = [5, 15]
max_duration_percentage = 0.7

# Fill the weights and values 
duration = [random.randint(duration_range[0], duration_range[1]) for _ in range(n_items)]
values  = [random.randint(values_range[0], values_range[1]) for _ in range(n_items)]

# Compute the maximum allowed weight
max_duration = int(max_duration_percentage * sum(duration))

# Print the instance
print("-" * 20)
print("Instance Details:")
print("-" * 20)
print(f"Duration                 : {duration}")
print(f"Values                   : {values}")
print(f"Total duration           : {sum(duration)}")
print(f"Maximum allowed duration : {max_duration}")

nQubits = n_items

# ----------------------------------------------------------------------------------------------------
#                       Defining the Hamiltonian
# ----------------------------------------------------------------------------------------------------

def build_cost_hamiltonian(values: list, duration: list, max_duration: int) -> SymbolicHamiltonian:
    """
    This function should be filled to build the problem cost hamiltonian.

    Args:
        values (list[int]): the list of values.
        duration (list[int]): the list of durations. 
        max_duration (int): the maximum value of the allowed duration.
    """
    nQubits = len(values)
    nAncillas = int(np.ceil(np.log2(max_duration)))
    cost_hamiltonian = (-1) * sum([values[i] * (1 - Z(i))/2 for i in range(nQubits)]) + (max_duration - sum([2**i * (1 - Z(nQubits + i))/2 for i in range(nAncillas)]) - sum([duration[i] * (1 - Z(i))/2 for i in range(nQubits)]))
    # 1st cost_hamiltonian = (-1) * sum([values[i] * (1 - Z(i))/2 for i in range(nQubits)])
    # 2nd cost_hamiltonian = (-1) * sum([values[i] * (1 - Z(i))/2 for i in range(nQubits)]) - max_duration + sum([duration[i] * (1 - Z(i))/2 for i in range(nQubits)])
    # 3rd cost_hamiltonian = (-1) * sum([values[i] * (1 - Z(i)) / (2 * duration[i]) for i in range(nQubits)])
    # 4th cost_hamiltonian = (-1) * (1 - sum([duration[i] * (1 - Z(i))/2 for i in range(nQubits)]) / max_duration) * sum([values[i] * (1 - Z(i))/2 for i in range(nQubits)])

    return SymbolicHamiltonian(cost_hamiltonian)

# ----------------------------------------------------------------------------------------------------
#                       Diagonalizing the hamiltonian
# ----------------------------------------------------------------------------------------------------

# create the cost Hamiltonian for the given graph
cost_hamiltonian = build_cost_hamiltonian(values=values, duration=duration, max_duration=max_duration)

ham_matrix = cost_hamiltonian.matrix

eig_val, eig_vec = np.linalg.eig(ham_matrix)
eig_vec = ["{0:0{bits}b}".format(i.argmax(), bits=nQubits) for i in eig_vec]

vec = zip(eig_val, eig_vec)
diagonalized_solution = sorted(vec, key=lambda x: x[0])
#print(diagonalized_solution)

# ----------------------------------------------------------------------------------------------------
#                       Utilities
# ----------------------------------------------------------------------------------------------------

def value_from_eigvec(eigvec:str) -> float: return sum([values[i] for i,b in enumerate(eigvec) if b == '1' and i < nQubits])
def duration_from_eigvec(eigvec:str) -> float: return sum([duration[int(i)] for i,b in enumerate(eigvec) if b == '1' and i < nQubits])

# ----------------------------------------------------------------------------------------------------
#                       Plotting
# ----------------------------------------------------------------------------------------------------

# finding the optimal solution in the data
optimal_solution = '011101'
iOpt = 0
while diagonalized_solution[iOpt][1][0:6] != optimal_solution: iOpt += 1

max_duration_switch = lambda d: int(d <= max_duration)
plotting_data = np.array([(loss,value_from_eigvec(binstr),max_duration_switch(duration_from_eigvec(binstr))) for loss,binstr in diagonalized_solution])

subspace_mask = plotting_data[:,2] == 1
anti_mask = np.logical_not(subspace_mask)
subspace_mask[iOpt] = False

fig,ax = plt.subplots(figsize=(6,6))
# scatterplots of the eigenstates
ax.scatter(x=plotting_data[subspace_mask,1],y=plotting_data[subspace_mask,0],c="green",label=r"$\sum d_i \leq d_{\mathrm{max}}$")
ax.scatter(x=plotting_data[anti_mask,1],y=plotting_data[anti_mask,0],c="red",label=r"$\sum d_i > d_{\mathrm{max}}$")

# optimal solution
ax.plot(plotting_data[iOpt,1],plotting_data[iOpt,0],"b*",markersize=plt.rcParams['lines.markersize']*2,label="Optimal solution")

# cosmetics
# 1st fig.suptitle(r"$\hat{H} = -\sum v_i\frac{1-\hat{Z}_i}{2}$")
# 2nd fig.suptitle(r"$\hat{H} = -\sum v_i\frac{1-\hat{Z}_i}{2} - \left(d_{\mathrm{max}} - \sum d_i\frac{1-\hat{Z}_i}{2}\right)$")
# 3rd fig.suptitle(r"$\hat{H} = -\sum \frac{v_i}{d_i}\frac{1-\hat{Z}_i}{2}$")
# 4th fig.suptitle(r"$\hat{H} = -\left(1 - \frac{1}{d_{\mathrm{max}}}\sum d_i\frac{1-\hat{Z}_i}{2}\right)\sum v_i\frac{1-\hat{Z}_i}{2}$")
ax.set_xlabel("Value")
ax.set_ylabel("Loss")
ax.legend()

# plt.show()
plt.savefig("plots/H0.pdf",bbox_inches="tight")
plt.close()