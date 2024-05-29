#!/usr/bin/node
const req = require('request');
const num = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${num}`;

req(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const mod = JSON.parse(body);
    console.log(mod.title);
  } else {
    console.log(error);
  }
});
