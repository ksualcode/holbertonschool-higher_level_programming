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
    const counter = {};
    let lastUser = 1;
    let count = 0;
    const tasks = (JSON.parse(body));
    tasks.forEach(task => {
      if (task.userId !== lastUser) {
        if (count !== 0) {
          counter[lastUser] = count;
        }
        lastUser = task.userId;
        count = 0;
      }
      if (task.completed) {
        count++;
      }
    });
    if (count !== 0) {
      counter[lastUser] = count;
    }
    console.log(counter);
  }
});
