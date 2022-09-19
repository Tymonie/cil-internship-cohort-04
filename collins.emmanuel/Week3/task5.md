// A simple JS to call the backend API.

fetch('http://skysports.com/football.json')
  .then((response) => response.json())
  .then((data) => console.log(data));
