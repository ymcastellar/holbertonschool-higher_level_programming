#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) return console.log('Error: ', error);

  const counttask = {};
  const todo = JSON.parse(body);
  todo.forEach((completed) => {
    if (completed.completed === true) {
      const countuser = completed.userId;
      if (countuser in counttask) {
        counttask[countuser]++;
      } else {
        counttask[countuser] = 1;
      }
    }
  });
  console.log(counttask);
});
