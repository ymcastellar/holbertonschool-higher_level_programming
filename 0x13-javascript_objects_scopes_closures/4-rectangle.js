#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.height = h;
      this.width = w;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    for (let i = 0; i < this.width * 2; i++) {
      console.log('X'.repeat(this.height * 2));
    }
  }

  double () {
    for (let i = 0; i < this.height * 2; i++) {
      console.log('X'.repeat(this.width * 2));
    }
  }
}
module.exports = Rectangle;
