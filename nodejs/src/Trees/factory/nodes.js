function Node(value) {
    this.value = value;
}

function BTreeNode(left,right,value) {
    //if (left instanceof BTreeNode && right instanceof BTreeNode)
    Node.call(this, value);
    this.left = left;
    this.right = right;
}

BTreeNode.prototype = Object.create(Node.prototype);
BTreeNode.prototype.constructor = BTreeNode ;

// var nodeLeft = new BTreeNode(null, null, "1");
// var nodeRight = new BTreeNode(null, null, "2");
// var nodeM = new BTreeNode(nodeLeft, nodeRight, "0");

// console.log(nodeLeft);
// console.log(nodeRight);
// console.log(nodeM);
// nodeLeft.value = "left";
// console.log(nodeM);
// BAD fix this
var outputString = "";
function printBTree(bTree) {
  outputString ="";
  _getBTreeString(bTree, 0);
  console.log(outputString);

}

function _getBTreeString(bTree, shift) {
    if (bTree) {
        outputString = outputString+ "\n";
        for (var i =0; i< shift; i++) {
            outputString = outputString +" ";
        }
        outputString = outputString + "[";
        outputString = outputString + bTree.value;
        if (bTree.left || bTree.right) {
            if (bTree.left) {                
                _getBTreeString(bTree.left, shift+3);
            }
            if (bTree.right) {
                _getBTreeString(bTree.right, shift+3);
            }
            outputString = outputString+ "\n";        
            for (var i =0; i< shift; i++) {
                outputString = outputString +" ";
            }
            outputString = outputString + "]";
        }else {
            outputString = outputString + "]";            
        }
    }
} 

function generateSampleBinaryTree(height){
    return createNodeAt(height);
}

function createNodeAt(height) {
    var value = Math.floor(Math.random() * 100);
    if (height === 0) {
        return new BTreeNode(null, null, value);
    }
    var leftNode = createNodeAt(height-1),
        rightNode = createNodeAt(height-1);
    return new BTreeNode(leftNode, rightNode, value);
}

// printBTree(generateSampleBinaryTree(5));
//console.log(JSON.stringify(generateSampleBinaryTree(5)));