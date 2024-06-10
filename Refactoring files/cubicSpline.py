import numpy as np
from sympy import *
from gaussian_elimination import gaussianElimination
from colors import bcolors


x = Symbol('x')
def build_s_printx0(f, x0, n, result):
    s_list = [None] * n

    for i in range(n-1):
        h_i = f[i+1][0] - f[i][0]
        term_1 = (f[i+1][1] * (x - f[i][0]))/h_i - (f[i][1] * (x - f[i+1][0])) / h_i
        term_2 = result[i+1] / 6 * (((x - f[i][0]) ** 3)/h_i - h_i * (x - f[i][0]))             # Build the s polynomials
        term_3 = result[i] / 6 * (((x - f[i+1][0]) ** 3)/h_i - h_i * (x - f[i+1][0]))

        s_list[i] = term_1 + term_2 - term_3
        print("s" + str(i) + "(x) = " + str(s_list[i]))                                     # Print the polynomials


    # Find f(x0)

    if (x0 < f[0][0]):
        print(
            "\nx0 smaller than f(x" + str(0) + ") = " + str(f[0][0]) + " so:")                   # In the case of extrapolation from the left
        print("s" + str(0) + "(" + str(x0) + ") = " + str(float(s_list[0].subs(x, x0))))
    else:
        if (x0 > f[n - 1][0]):
            print(
                "\nx0 bigger than f(x" + str(n) + ") = " + str(f[n - 1][0]) + " so:")                 # In the case of extrapolation from the right
            print("s" + str(n - 1) + "(" + str(x0) + ") = " + str(float(s_list[n - 2].subs(x, x0))))

        else:
            for i in range(n - 1):
                if (x0 > f[i][0] and x0 < f[i + 1][0]):
                    print(
                        "\nx0 between f(x" + str(i) + ") = " + str(f[i][0]) + " and f(x" + str(           # Finding the appropriate polynomial
                            i + 1) + ") = " + str(
                            f[i + 1][0]) + " so:")
                    print("s" + str(i) + "(" + str(x0) + ") = " + str(float(s_list[i].subs(x, x0))))


def natural_cubic_spline(f, x0):
    n = len(f)

    matrix = []
    for i in range(n):
        row = []
        for j in range(n + 1):                         # Initialize n x n+1 matrix with 0
            row.append(0)
        matrix.append(row)

    # Initialize the matrix with the values according to the formula

    matrix[0][0] = 1
    matrix[n-1][n-1] = 1

    for i in range(1, n-1):
        h0 = f[i][0] - f[i-1][0]
        h1 = f[i+1][0] - f[i][0]
        for j in range(0,n):
            if(i == j):
                matrix[i][j] = 1/3 * (h0 + h1)
                matrix[i][j-1] = 1/6 * h0
                matrix[i][j+1] = 1/6 * h1
        matrix[i][n] = (f[i+1][1] - f[i][1])/h1 - (f[i][1] - f[i-1][1])/h0

    print("matrix:\n", np.array(matrix))

    # Solve matrix by gaussian elimination

    result = gaussianElimination(matrix)
    if isinstance(result, str):                           # Inform doesn't have a single solution
        print(result)
        return
    else:
        print(bcolors.OKBLUE, "\nvector m:", bcolors.ENDC)
        for x1 in result:
            print("[", "{:.6f}".format(x1), "]")                  # Print vector m
        print("\n")

    build_s_printx0(f, x0, n, result)



if __name__ == '__main__':
    f = [(1, 1), (2, 2), (3, 1), (4, 1.5), (5, 1)]
    x0 = 1.5


    # Fx_0 = 0         # For regular cubic sline
    # Fx_n = 0

    print("func: " + str(f))
    print("x0 = " + str(x0) + "\n")
    natural_cubic_spline(f, x0)

