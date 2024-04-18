#!/usr/bin/node
const num = process.argv[2];
const nums = parseInt(num, 10);
if (Number.isNaN(nums)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < nums; i++) {
    let row = '';
    for (let y = 0; y < nums; y++) {
      row += 'X';
    }
    console.log(row);
  }
}
