#!/usr/bin/node
function add (a, b) {
  if (!Number.isInteger(a) || !Number.isInteger(b)) {
    return 0;
  } else {
    return a + b;
  }
}
module.exports = {
  add
};
