# LaTeX-Matrix-Calculator

This website is a matrix calculator that allows users to enter the latex code of a matrix and perform various operations on it. The website is built using the React framework and Flask framework for Python.

## Features

The website has a text window where users can enter the latex code of a matrix. The supported matrix environments include `bmatrix`, `array`, and others. The entries of the matrix should be separated by `&`, and each line except the last one needs to have `\\` at the end like so
`\left[\begin{array}{ccc} \n
4 & -4 & 2 \\ \n
-4 & 4 & -2 \\ \n
2 & -2 & 1
\end{array}\right]`

Once the matrix code is entered, the user can click on the submit button to perform various operations on the matrix. The server then executes the `get_matrix` function that converts the latex matrix code into a numpy matrix. The following operations can be performed on the matrix:

- Rank calculation
- Determinant calculation
- Eigenvalue calculation
- Inverse calculation
- Echelon form calculation

All the calculated data is displayed on the website, along with a copy latex code button that can be used to copy the latex code of the inverse of the matrix and the echelon form of the matrix. This makes it easy to copy and paste the matrices into your file.

## Usage

To use the website, simply navigate to https://latex-matrix-calculator.herokuapp.com/ and enter the latex code of the matrix in the text window. Once the code is entered, click on the submit button to perform the desired operation on the matrix. The results will be displayed on the website.

## Technical Details

The website is built using the React framework for the frontend and Flask framework for Python on the backend. The server executes the `get_matrix` function to convert the latex matrix code into a numpy matrix. The matrix operations are performed using the numpy and sympy libraries. The website is deployed on Heroku.
