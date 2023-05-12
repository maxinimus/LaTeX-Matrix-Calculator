from flask import Flask, request
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin
import matrix as m

app = Flask(__name__, static_folder='my-app/build', static_url_path='')
CORS(app)

@app.route('/matrix', methods=['POST'])
@cross_origin()
def matrix():
    input_string = request.json['input_string']
    matrix = m.get_matrix(input_string)
    if matrix.shape == (1, ):
        return {'rank': 'error', 'determinant': 'error', 'inverse': 'error', 'echelon': 'error'}
    
    rank = m.get_rank(matrix)
    determinant = m.get_determinant(matrix)
    eigenvalues = m.get_eigenvalues(matrix)
    inverse = m.get_inverse(matrix)
    echelon = m.get_echelon(matrix)

    return {'rank': str(rank), 
            'determinant': str(determinant), 
            'eigenvalues': str(eigenvalues),
            'inverse': str(inverse), 
            'echelon': str(echelon)}

@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    app.run(debug=True)