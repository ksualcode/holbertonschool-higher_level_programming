#!/usr/bin/node
const number = process.argv[2];

if (parseInt(number)) {
  for (let i = 0; i < parseInt(number); i++) {
    console.log('X'.repeat(number));
  }
} else {
  console.log('Missing size');
}
