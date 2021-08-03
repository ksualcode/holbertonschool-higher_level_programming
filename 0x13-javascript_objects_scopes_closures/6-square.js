#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let char = c;
    if (!c) {
      char = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.height));
    }
  }
};
