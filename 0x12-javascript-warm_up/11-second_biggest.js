#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  const args = process.argv.slice(2);
  const orderedArgs = args.sort((a, b) => a - b);
  console.log(orderedArgs[orderedArgs.length - 2]);
}
