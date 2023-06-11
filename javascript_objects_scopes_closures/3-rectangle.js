#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || !Number.isInteger(w) || h <= 0 || !Number.isInteger(h)) {
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print() {
    if (Object.keys(this).length === 0) {
      console.log("Empty rectangle");
      return;
    }

    for (let i = 0; i < this.height; i++) {
      console.log("X".repeat(this.width));
    }
  }
}
