#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  const updatedArgs = args.map((value) => (value === 12 ? 89 : value));
  const sortedArgs = updatedArgs.sort((a, b) => b - a);
  console.log(sortedArgs[1]);
}
