# Numerical Analysis Final Project

This project focuses on numerical analysis methods, featuring implementations of Cubic Spline, Polynomial Interpolation, and Gauss-Legendre Quadrature techniques. It also explores refactoring concepts, providing comprehensive explanations and implementations of these numerical methods.
## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Methods](#methods)
  - [Cubic Spline](#cubic-spline)
  - [Polynomial Interpolation](#polynomial-interpolation)
  - [Gauss-Legendre Quadrature](#gauss-legendre-quadrature)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Numerical analysis is a branch of mathematics that deals with the study of algorithms for approximating solutions to mathematical problems. This project focuses on three specific methods: Cubic Spline, Polynomial Interpolation, and Gauss-Legendre Quadrature.

## Installation

To use this project, you need to have Python installed on your system. You can download Python from the official website: https://www.python.org/downloads/

After installing Python, you can clone this repository to your local machine using the following command:

```
git clone https://github.com/shulamitmorjossef/final-project-numerical-analysis.git
```

## Usage

Navigate to the project directory and run the desired Python script for each method. For example, to run the Cubic Spline implementation, execute the following command:

```
python refactoring/cubicSpline.py
```

Follow the prompts or modify the script to provide the necessary input data for the chosen method.



## Project Structure

The project is organized into two main directories:

- **`gauss legendre method`**:  Contains the implementation of the Gauss-Legendre Quadrature method in the gaussian quadrature method file.

- **`refactoring`**: Contains the following files:
  - `colors.py`: A utility file providing color formatting functionality.
  - `cubicSpline.py`: Implementation of the Cubic Spline method.
  - `gaussian_elimination.py`: Implementation of the Gaussian Elimination method.
  - `polynomial_interpolation.py`: Implementation of the Polynomial Interpolation method.
 
## Methods

### Cubic Spline

The Cubic Spline method is used for interpolating a set of data points with a piecewise cubic polynomial. This method ensures that the interpolating function is continuous and smooth, making it suitable for approximating curves and surfaces.

### Polynomial Interpolation

Polynomial Interpolation is a method for constructing a polynomial function that passes through a given set of data points. It involves determining the coefficients of the polynomial such that it interpolates the provided data points exactly.  

### Gauss-Legendre Quadrature

The Gauss-Legendre Quadrature method is a numerical integration technique used to approximate definite integrals over a finite interval. It is part of the Gaussian quadrature family, which includes methods for different weight functions. This project focuses on the Legendre weight function and provides a detailed explanation and implementation of the Gauss-Legendre Quadrature method.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). 
