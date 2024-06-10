import numpy as np

from colors import bcolors
from matrix_utility import *
from gaussian_elimination import gaussianElimination


def polynomialInterpolation(table_points, x):

    n = len(table_points)
    matrix = np.full((n, n+1), None)            # Initialize n x n+1 matrix with None
    for i in range(n):
        x_i = table_points[i][0]
        y_i = table_points[i][1]
        for j in range(n):                                     # Initialize the matrix with the x values to appropriate power from point table
            matrix[i][j] = x_i ** j
        matrix[i][n] = y_i                                     # Initialize the result vector of the matrix with the respective y values

    resultVec = gaussianElimination(matrix)                       # Solve matrix by gaussian elimination


    if isinstance(resultVec, str):                          # Inform doesn't have a single solution
        print(resultVec)
    else:
        print(bcolors.OKBLUE, "\nSolution for the system:", bcolors.ENDC)
        for x1 in resultVec:
            print("[","{:.6f}".format(x1), "]")              # Printing the coefficients of the polynomial


    solution = 0
    for i in range(n):
        solution += resultVec[i] * (x ** i)                   # Calculate y value of polynomial at point x


    polynomial_terms = []
    for i in range(n):
        term = f'({resultVec[i]}) * x^{i}'                         # Build polynomial
        polynomial_terms.append(term)

    polynomial_string = ' + '.join(polynomial_terms)
    print(f'\nP(X) = {polynomial_string}')                                              # Print polynomial

    print(bcolors.OKBLUE, f"\nThe Result of P(X={x}) is:", bcolors.ENDC, solution)          # Print solution




if __name__ == '__main__':

    table_points = [(0, 0), (1, 0.8415), (2, 0.9093), (3, 0.1411), (4, -0.7568), (5, -0.9589), (6, -0.2794)]

    x = 3.5

    print(bcolors.OKBLUE, "----------------- Interpolation & Extrapolation Methods -----------------\n", bcolors.ENDC)
    print(bcolors.OKBLUE, "Table Points: ", bcolors.ENDC, table_points)
    print(bcolors.OKBLUE, "Finding an approximation to the point: ", bcolors.ENDC, x,'\n')
    polynomialInterpolation(table_points, x)
    print(bcolors.OKBLUE, "\n---------------------------------------------------------------------------\n", bcolors.ENDC)
