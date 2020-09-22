#!/usr/bin/node

const fs = require('fs');

const content = 'Python is cool';

fs.writeFile(process.argv[2], content, (err) => {
  if (err) {
    console.error(err);
  }
  // file written successfully
});
