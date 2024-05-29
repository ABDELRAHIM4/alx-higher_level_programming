#!/usr/bin/node
const ID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${ID}`;
const req = require('request');
req(url, (error, response, body) => {
  if (!error) {
    const names = JSON.parse(body);
    const charc = names.characters;
    charc.forEach((item) => {
      req(item, (error, response, body) => {
        if (!error) {
          const num = JSON.parse(body);
          console.log(num.name);
        }
      });
    });
  }
});
