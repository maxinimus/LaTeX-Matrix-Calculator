import numpy as np
import sympy

# reverse the string
def reverse(string):
    string = string[::-1]
    return string

# Get the matrix from the latex code
def get_matrix(matrix_latex):
    if (matrix_latex == ""):
        return np.array([])
    
    try:
        # split matrix into rows
        rows = matrix_latex.strip().split('\n')[1:-1]
        num_rows = len(rows)
        for i in range(num_rows - 1):
            rows[i] = rows[i][:len(rows[i]) - 2]

        # split each row into columns and convert to numpy array
        num_columns = len(rows[0].split('&'))
        matrix = np.zeros((num_rows, num_columns))
        for i, row in enumerate(rows):
            for j, entry in enumerate(row.split('&')):
                matrix[i, j] = float(entry.strip())

        return matrix
    except:
        # return empty numpy array if there is an unhandled error
        return np.array([0])

# Print the matrix in latex code
def matrix_to_latex(matrix):
    rows, cols = matrix.shape
    latex_code = "\\left[\\begin{array}{" + "r" * rows + "}\n"
    
    for i in range(rows):
        for j in range(cols - 1):
            if (j != cols - 1):
                double_entry = matrix[i, j]
                entry = "{:.2f}".format(double_entry)
                latex_code += entry + " & "
            else:
                double_entry = matrix[i, j]
                entry = "{:.2f}".format(double_entry)
                latex_code += entry
        double_entry = matrix[i, cols - 1]
        entry = "{:.2f}".format(double_entry)
        latex_code += entry
        if (i != rows - 1):
            latex_code += " \\\\"

        latex_code += "\n"

    latex_code += "\\end{array}\\right]"
    return latex_code

# Get rows of matrix
def get_rows(matrix):
    rows = matrix.shape[0]
    return rows

# Get columns of matrix
def get_columns(matrix):
    columns = matrix.shape[1]
    return columns

# Get rank of matrix
def get_rank(matrix): 
    if matrix.shape == (0,):
        return 0
    rank = np.linalg.matrix_rank(matrix)
    return rank

# Get determinant of matrix
def get_determinant(matrix):
    if matrix.shape == (0,):
        return 0
    if (matrix.shape[0] != matrix.shape[1]):
        return 0
    else: 
        determinant = np.linalg.det(matrix)
        return round(determinant, 2)

# Get eigenvalues of matrix
def get_eigenvalues(matrix):
    if matrix.shape == (0,):
        return 0
    if (get_rows(matrix) != get_columns(matrix)):
        return 0
    else:
        eigenvalues = np.linalg.eigvals(matrix)
        for i, eigenvalue in enumerate(eigenvalues):
            eigenvalues[i] = round(eigenvalue, 2)
        # put eigenvalues into a string including the latex code
        str = ""
        for i, eigenvalue in enumerate(eigenvalues):
            str += "\\lambda_{} = {}".format(i + 1, eigenvalue)
            if (i != len(eigenvalues) - 1):
                str += " \\\\ "
            str += "\n"

        return str
    
# Get inverse of matrix
def get_inverse(matrix):
    if matrix.shape == (0,):
        return 0
    if (get_rows(matrix) != get_columns(matrix)):
        return 0
    else:
        rank = get_rank(matrix)
        if (rank != get_rows(matrix)):
            return 0
        else:
            inverse = np.linalg.inv(matrix)
            return matrix_to_latex(inverse)
        
# Find the echelon form of the matrix
def get_echelon(matrix):
    if matrix.shape == (0,):
        return 0

    echelon = sympy.Matrix(matrix).echelon_form()
    for i in range(echelon.shape[0]):
        for j in range(echelon.shape[1]):
            echelon[i, j] = round(echelon[i, j], 2)    

    return matrix_to_latex(echelon)