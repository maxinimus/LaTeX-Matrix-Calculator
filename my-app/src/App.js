import './App.css';
import React, { useState } from 'react';
var Latex = require('react-latex');

function SubmitButton({ onMatrixUpdate }) {
  const handleClick = () => {
    console.log('The button was clicked');
    const inputString = document.querySelector('.input').value;
    fetch('/matrix', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({input_string: inputString})
    }, [])
    .then(response => response.json())
    .then(data => {
      onMatrixUpdate(
        data.rank, 
        data.determinant,
        data.eigenvalues,
        data.inverse,
        data.echelon
        );
      })
    .catch(error => console.error(error));
  };
  
  return (
    <button className='button' onClick={handleClick}>
      Submit
    </button>
  )
} 

function CopyButton( { value }) {
  const handleClick = () => {
    const outputString = value;
    navigator.clipboard.writeText(outputString);
  };

  return (
    <button className='button' onClick={handleClick}>
      Copy <Latex> $\LaTeX$ </Latex> Code
    </button>
  )
}

function App() {  
  const [rank, setRank] = useState(0);
  const [determinant, setDeterminant] = useState(0);
  const [eigenvalues, setEigenvalues] = useState([]);
  const [inverse, setInverse] = useState('0');
  const [echelon, setEchelon] = useState('0');


  const handleMatrixUpdate = (rank, determinant, eigenvalues, inverse, echelon)  => {
    setRank(rank);
    setDeterminant(determinant);
    setEigenvalues(eigenvalues);
    setInverse(inverse);
    setEchelon(echelon);
  };

  return (
    <div className="App-header">
      <p className='text'>Input <Latex> $\LaTeX$ </Latex> matrix code here</p>
      <textarea className='input' />
      <SubmitButton onMatrixUpdate={handleMatrixUpdate} />
      
      {/* Show the rank, determinant and eigenvalues of the inputted matrix */}
      <p className='field'>Rank: {rank} </p>
      <p className='field'>Determinant: {determinant} </p>
      {(eigenvalues !== "error" && eigenvalues !== "0") ? (<p className='field'> The eigenvalues are </p>) : (null)}
      {(eigenvalues !== '0' && eigenvalues !== 'error') ? (<Latex>{"$" + eigenvalues + "$"}</Latex>) : (null)}

      {/* use alert to alert the user if there is an error */}
      {(inverse === 'error') ? (alert('Error: your input is incorrectly formatted')) : (null)}

      {/* Show the inverse of the inputted matrix */}
      {(inverse !== '0' && inverse !== 'error') ? (<p className='field'> The inverse is </p>) : (null)}
      {(inverse === '0' || inverse === 'error') ? (<p className='field'>The inverse does not exist</p>) : (null)}

      {(inverse !== '0' && inverse !== 'error') ? (<Latex>{"$" + inverse + "$"}</Latex>) : (null)}
      {(inverse !== '0' && inverse !== 'error') ? (<CopyButton value={inverse} />) : (null)}
      
      {/* Show the echelon form of the inputted matrix */}
      {(echelon !== '0' && echelon !== 'error') ? (<p className='field'> The echelon form is </p>) : (null)}
      {(echelon === '0' || echelon === 'error') ? (<p className='field'>Echelon form does not exist</p>) : (null)}

      {(echelon !== '0' && echelon !== 'error') ? (<Latex>{"$" + echelon + "$"}</Latex>) : (null)}
      {(echelon !== '0' && echelon !== 'error') ? (<CopyButton value={echelon} />) : (null)}      
    </div>
  );
}

export default App;
