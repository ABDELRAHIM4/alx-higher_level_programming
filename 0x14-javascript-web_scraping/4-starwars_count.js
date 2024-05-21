#!/usr/bin/node
const req = require('request');
const num = process.argv[2];
let count = 0;
const ID = 18;
req(num, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const mods = JSON.parse(body).results;
    mods.forEach(mod => {
      const characters = mod.characters;
      if (characters.includes(`https://swapi-api.alx-tools.com/api/people/${ID}/`)) {
        count ++;
      }
    });
  console.log(count);
  }
});
