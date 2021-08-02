#!/usr/bin/node
const number = process.argv[2];
let x = '';

if (parseInt(number)) {
  for (let i = 0; i < parseInt(number); i++) {
    x += 'x';
  }
  for (let i = 0; i < parseInt(number); i++) {
    console.log(x);
  }
} else {
  console.log('Missing size');
}
