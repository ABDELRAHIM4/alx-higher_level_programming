#!/usr/bin/node
const arg = process.argv.slice(2);
if (arg.length === 0 || arg.length === 1) {
  console.log(0);
} else {
  const sort = arg.map(x => parseInt(x)).sort((a, b) => b - a);
  const second = sort[1];
  console.log(second);
}
