function callPythonFunction() {
  fetch('/python_function')
    .then(response => response.text())
    .then(data => console.log(data))
    .catch(error => console.error(error))
}

const { spawn } = require('child_process');
const express = require('express');
const app = express();

app.get('/python_function', (req, res) => {
  const python = spawn('python', ['./script.py']);
  python.stdout.on('data', data => {
    console.log('Python script output:', data.toString());
    res.send(data.toString());
  });
});

app.listen(3000, () => {
  console.log('Server started on port 3000');
});

