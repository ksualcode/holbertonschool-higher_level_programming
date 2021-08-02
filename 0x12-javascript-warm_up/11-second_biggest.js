#!/usr/bin/node
function secondBig () {
  let biggest;
  let second;
  const input = process.argv;

  if (input.length === 2 || input.length === 3) {
    return 0;
  }

  for (let i = 0; i < input.length; i++) {
    if (parseInt(input[2 + i]) > biggest || biggest === undefined) {
      second = biggest;
      biggest = parseInt(input[2 + i]);
    } else if (second === undefined) {
      second = parseInt(input[2 + i]);
    }
  }
  return second;
}

console.log(secondBig());
