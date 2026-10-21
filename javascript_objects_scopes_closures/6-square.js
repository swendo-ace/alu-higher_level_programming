#!/usr/bin/node
const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  charPrint (c = 'X') {
    for (let row = 0; row < this.height; row++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
