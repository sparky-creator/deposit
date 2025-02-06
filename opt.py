# Use line search from powell for CD
from scipy.optimize._optimize import _linesearch_powell
import numpy as np


def coordinate_descent_with_linesearch(
    func,
    x_init,
    max_iter=100,
    tol=1e-2,
    save_details_path="progress_at_step.npz",
    verbose=0,
    lower_bound=None,
    upper_bound=None,
):
    """
    Black-Box Coordinate Descent with Powell Line Search for each coordinate.

    Parameters:
    - func: callable, the black-box function to optimize
    - x_init: array-like, the initial guess for the solution
    - max_iter: int, the maximum number of iterations
    - tol: float, the tolerance for line search only

    Returns:
    - x_opt: array-like, the optimized coordinates
    - history: list, the objective function value at each iteration
    """
    x = x_init.copy()
    n = len(x)
    fval_history = []
    x_history = []

    # Initial eval
    fval = func(x)
    fval_history.append(fval)
    x_history.append(x)
    if verbose > 0:
        print(f"Start score:", fval)

    for iteration in range(max_iter):
        if verbose > 0:
            print(f"Iter:{iteration}", flush=True)

        for i in range(n):
            # Perform line search for coordinate i using Powell's method
            direction = np.zeros_like(x)
            direction[i] = 1.0  # Focus on one coordinate at a time

            # Use the Powell line search to optimize along this direction
            new_fval, new_x, _ = _linesearch_powell(
                func,
                x.copy(),
                direction,
                tol=tol,
                lower_bound=lower_bound,
                upper_bound=upper_bound,
                fval=fval,
            )
            # Only take value if better one is found...
            if new_fval < fval:
                x = new_x
                fval = new_fval

            # Log history
            fval_history.append(fval)
            x_history.append(x.copy())

            if verbose > 0:
                print(f"   p:{i} fval:{fval}", flush=True)

            if save_details_path is not None and len(save_details_path) > 0:
                np.savez_compressed(
                    save_details_path, fval_history=fval_history, x_history=x_history
                )

    return x, fval_history, x_history
