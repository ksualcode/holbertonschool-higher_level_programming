#!/usr/bin/node
const number = process.argv[2];

if (parseInt(number)) {
  for (let i = 0; i < parseInt(number); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
