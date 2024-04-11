#!/usr/bin/node
function add (a, b) {
  console.log(`${a + b}`);
}
if (process.argv.length < 4) {
  console.log('NaN');
} else {
  const arg1 = parseInt(process.argv[2]);
  const arg2 = parseInt(process.argv[3]);
  add(arg1, arg2);
}
