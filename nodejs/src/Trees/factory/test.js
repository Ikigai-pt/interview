var fs = require('fs');
// file is included here:
eval(fs.readFileSync('nodejs/src/Trees/factory/nodes.js') +" ");

var treeHeight = 3;
var tmpb = generateSampleBinaryTree(treeHeight);
printBTree(tmpb);