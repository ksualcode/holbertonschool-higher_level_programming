#!/usr/bin/node

const request = require('request');
const options = {
  url: process.argv[2],
  method: 'GET'
};

request(options, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const movies = JSON.parse(body).results;
    let counter = 0;
    for (let i = 0; i < movies.length; i++) {
      const characters = movies[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].includes('/18/')) {
          counter++;
          break;
        }
      }
    }

    console.log(counter);
  }
});
