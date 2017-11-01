var fs = require('fs');
// file is included here:
eval(fs.readFileSync('nodes.js') +" ");
var value = Math.floor(Math.random() * 10);
var treeHeight = 3;
var tmpb = generateSampleBinaryTree(value);
printBTree(tmpb);
