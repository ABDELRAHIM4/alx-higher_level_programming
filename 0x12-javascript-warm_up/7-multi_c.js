#!/usr/bin/node
const num = process.argv[2];
const nums = parseInt(num, 10);
if (Number.isNaN(nums)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < nums; i++) {
    console.log('C is fun');
  }
}
