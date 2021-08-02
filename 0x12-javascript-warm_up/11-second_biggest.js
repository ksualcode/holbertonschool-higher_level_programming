#!/usr/bin/node
let biggest;
let second;

const input = process.argv;

if (input.length == 2 || input.length == 3) {
  console.log('0');
  return;
}

for (let i = 0; i < input.length; i++) {
  if (parseInt(input[2 + i]) > biggest || biggest == undefined) {
    second = biggest;
    biggest = parseInt(input[2 + i]);
  } else if (second == undefined) {
    second = parseInt(input[2 + i]);
  }
}
console.log(second);
