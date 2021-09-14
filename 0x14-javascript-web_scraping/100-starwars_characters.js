#!/usr/bin/node

const request = require('request');

const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + process.argv[2],
  method: 'GET'
};

// Request de la pelicula
request(options, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const people = JSON.parse(body).characters;
    people.forEach(character => {
      request({ url: character, method: 'GET' }, function (err, resp, body) {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
