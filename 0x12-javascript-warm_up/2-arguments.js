#!/usr/bin/node
let argument;

if (process.argv.length < 3) {
  argument = 'No argument';
} else if (process.argv.length === 3) {
  argument = 'Argument found';
} else {
  argument = 'Arguments found';
}

console.log(argument);
