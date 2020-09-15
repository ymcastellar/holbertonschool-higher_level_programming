#!/usr/bin/node
let argument;

if (process.argv[2] !== undefined) {
  argument = process.argv[2];
} else {
  argument = 'No argument';
}

console.log(argument);
