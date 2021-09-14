#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const options = {
  url: process.argv[2],
  method: 'GET'
};

request(options, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(process.argv[3], body, 'utf8', function (err) {
      if (err) {
        console.error(err);
      }
    });
  }
});
