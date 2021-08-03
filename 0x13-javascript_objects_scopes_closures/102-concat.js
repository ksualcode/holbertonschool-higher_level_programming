#!/usr/bin/node
const fs = require('fs');
const string1 = fs.readFileSync(process.argv[2]).toString();
const string2 = fs.readFileSync(process.argv[3]).toString();

fs.writeFile(process.argv[4], string1 + string2, { overwrite: true }, function (err) {
  if (err) throw err;
});
