const express = require('express');
const app = express();
const port = 3000;

// Set the view engine to EJS
app.set('view engine', 'ejs');

// Define routes
app.get('/login', (req, res) => {
  res.render('login');
});

app.get('/facilities', (req, res) => {
  res.render('facilities', { facilities });
});

app.get('/classrooms', (req, res) => {
  res.render('classrooms', { classrooms });
});

app.get('/teachers', (req, res) => {
  res.render('teachers', { teachers });
});

app.get('/children', (req, res) => {
  res.render('children', { children });
});

// Start the server
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});