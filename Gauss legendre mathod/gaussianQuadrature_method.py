import numpy as np
import math
from colors import bcolors

def gauss_legendre_quadrature(f, a, b, n):
    """
    Gauss-Legendre Quadrature for Numerical Integration

    Parameters:
    f (function): The function to be integrated.
    a (float): The lower limit of integration.
    b (float): The upper limit of integration.
    n (int): The number of nodes and weights.

    Returns:
    float: The approximate definite integral of the function over [a, b].
    """

    # Define the nodes and weights for Gauss-Legendre Quadrature
    nodes, weights = np.polynomial.legendre.leggauss(n)

    # transform nodes from [-1, 1] to [a, b]
    transformed_nodes = []
    for node in nodes:
        transformed_nodes.append(0.5 * (b - a) * node + 0.5 * (a + b))


    # Calculate the integral using the Gauss-Legendre Quadrature formula
    integral=0
    for i in range(n):
        integral += weights[i] * f(transformed_nodes[i])
    integral *= 0.5 * (b - a)

    return integral


if __name__ == '__main__':
    a = 0                                    # lower bound of integral
    b = 2                                    # upper bound of integral
    points = 4                               # Number of nodes, to get better approximation
    f = lambda x: math.e ** (3 * x)

    integral = gauss_legendre_quadrature(f, a, b, points)
    print(bcolors.OKBLUE,f'The integral over the interval [{a}, {b}] is: {integral}')