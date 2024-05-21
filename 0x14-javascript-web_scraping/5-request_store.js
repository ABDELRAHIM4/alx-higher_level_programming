#!/usr/bin/node
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];
const req = require('request');
req(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    fs.writeFile(file, body, 'utf-8', (error) => {
      if (error) {
        console.error(error);
      }
    });
  }
});
