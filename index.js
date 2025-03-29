#!/usr/bin/env node

const { PythonShell } = require('python-shell');
const path = require('path');

// Get the path to the snake game script
const scriptPath = path.join(__dirname, 'snake_game.py');

// Run the Python script
const pyshell = new PythonShell(scriptPath, {
    mode: 'text',
    pythonPath: 'python3'
});

// Handle errors
pyshell.on('error', function (err) {
    console.error('Error running snake game:', err);
});

// Handle script exit
pyshell.end(function (err) {
    if (err) {
        console.error('Error:', err);
    }
}); 