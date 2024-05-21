#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];
const con = process.argv[3];
fs.writeFile(file, con, (err) => {
  if (err) {
    console.log(err);
  }
});
