#!/usr/bin/node
const url = process.argv[2];
const req = require('request');
req(url, (error, response, body) => {
  if (!error) {
    const data = JSON.parse(body);
    const com = {};
    data.forEach((id) => {
      if (id.completed) {
        if (com[id.userId]) {
          com[id.userId]++;
        } else {
          com[id.userId] = 1;
        }
      }
    });
    console.log(com);
  }
});
