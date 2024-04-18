#!/usr/bin/node
function factorial (n) {
  if (typeof n !== 'number' || !Number.isInteger(n)) {
    return 1;
  }
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}
const arg1 = parseInt(process.argv[2]);
console.log(`${factorial(arg1)}`);
