# ETH-HACKATHON-2024: Qilimanjaro Challenge
Team Banana State: Amanda Scoles, Yaron Castor, Maurice Rieger, Hendrik Kühne

## The challenge

The contents of this repository are our thoughts on the challenge by [Qilimanjaro](https://www.qilimanjaro.tech). The task is to find a set set $S$ that maximizes $\sum_{i\in S}v_i$, subject to the constraint $\sum_{i\in S} d_i \leq d_{\text{max}}$.

## Our solutions

Our solutions are contained in `challenge_description/problem.ipynb`. The remaining code in this repository is structured as follows:

* `QAOA_subspace.ipynb` contains code that investigates circumventing the duration-value conflict by limiting the Hilbert space to a subspace that fulfills the inequality constraint.
* `QAOA_wholespace.ipynb` contains code that we used to test different Hamiltonians in the context of the QAOA algorithm and familiarize ourselves with the framework of this challenge.
* `plots/` contains plots of `(value,loss)` data pairs for different Hamiltonians, that illustrate how instrumental it is to construct an appropriate loss Hamiltonian for the optimization procedure. These plots have been created using `plot_eigenvalue_progression.py`.
* `plot_process_management_problem.ipynb` contains code that runs the QAOA and QAE algorithms for many different problem instances and calculates statistics, comparing the two methods.