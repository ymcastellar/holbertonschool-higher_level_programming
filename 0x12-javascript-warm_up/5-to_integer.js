#!/usr/bin/node
let argument;

if (parseInt(process.argv[2])) {
  argument = 'My number: ' + process.argv[2];
} else {
  argument = 'Not a number';
}

console.log(argument);
