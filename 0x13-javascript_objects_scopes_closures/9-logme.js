#!/usr/bin/node
let totalP = 0;
exports.logMe = function (item) {
  console.log(totalP + ': ' + item);
  totalP++;
};
