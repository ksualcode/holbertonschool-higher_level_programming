#!/usr/bin/node
const dict = require('./101-data').dict;
const ordDict = {};
Object.entries(dict).forEach(id => {
  if (ordDict[id[1]]) {
    ordDict[id[1]].push(id[0]);
  } else {
    ordDict[id[1]] = [id[0]];
  }
});
