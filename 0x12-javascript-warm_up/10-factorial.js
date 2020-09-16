#!/usr/bin/node

function factorialize (num) {
  if (num < 0) return -1;
  // If the number is 0 or if num doesn't exist, its factorial is 1.
  else if (num === 0 || isNaN(num)) return 1;
  // Otherwise, call the recursive procedure again
  else {
    return num * factorialize(num - 1);
  }
}

const num = parseInt(process.argv[2]);
console.log(factorialize(num));
