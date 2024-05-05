The hamiltonians we plotted are:

* 1st: $\hat{H} = -\sum v_i\frac{1-\hat{Z}_i}{2} \equiv \sum v_i\hat{Z}_i$
* 2nd: $\hat{H} = -\sum v_i\frac{1-\hat{Z}_i}{2} - \left(d_{\text{max}} - \sum d_i\frac{1-\hat{Z}_i}{2}\right) \equiv \sum (v_i-d_i)\hat{Z}_i$
* 3rd: $\hat{H} = -\sum \frac{v_i}{d_i}\frac{1-\hat{Z}_i}{2} \equiv \sum \frac{v_i}{d_i}\hat{Z}_i$
* 4th: $\hat{H} = -\left(1 - \frac{1}{d_{\text{max}}}\sum d_i\frac{1-\hat{Z}_i}{2}\right)\sum v_i\frac{1-\hat{Z}_i}{2}$
* 5ht: $\hat{H} = \text{softplus}\left(\frac{1}{d_{\text{max}}}\sum d_i\frac{1-\hat{Z}_i}{2}-1\right)-\sum v_i\frac{1-\hat{Z}_i}{2}$

Every plot shows the losses of the eigenstates of the corresponding Hamiltonian. We show data points in green if they satisfy the duration constraint. The ideal solution for this dataset is marked with a blue star.

The plots show how constructing an appropriate Hamiltonian is instrumental to the performance of the optimization. Each Hamiltonian without ancilla qubits that does not operate on a subspace of the whole Hilbert space $\mathcal{H}$ represents a compromise between two different goals: Maximizing value and minimizing duration. Accordingly, the different loss-value plots show that many hamiltonians do not assign the lowest loss to the ideal solution; indeed, many of the lowest loss eigenstates do not even satisfy the duration constraint. We have thus illustrated how influential the constrction of an appropriate Hamiltonian on the result of the optimization procedure is.