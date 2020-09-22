#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) return console.log('Error: ', error);

  const result = JSON.parse(body).results;
  let count = 0;
  result.forEach(function (result) {
    const people = result.characters;
    people.forEach(function (people) {
      if (people.includes('/18')) {
        count++;
      }
    });
  });
  console.log(count);
});
