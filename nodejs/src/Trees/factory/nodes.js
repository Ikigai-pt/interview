
// CLASS definitions
function Node(value) {
    this.value = value;
}

function BTreeNode(left, right, value) {
    Node.call(this, value);
    this.left = left;
    this.right = right;
}

BTreeNode.prototype = Object.create(Node.prototype);
BTreeNode.prototype.constructor = BTreeNode;

function generateSampleBinaryTree(height) {
    return createNodeAt(height);
}

function createNodeAt(height) {
    var value = Math.floor(Math.random() * 100);
    if (height === 0) {
        return new BTreeNode(null, null, value);
    }
    var leftNode = createNodeAt(height - 1),
        rightNode = createNodeAt(height - 1);
    return new BTreeNode(leftNode, rightNode, value);
}

// BAD fix this
var outputString = "";
function printBTree(bTree) {
    outputString = "";
    console.log("");
    _getBTreeString(bTree, "", null);
    console.log(outputString);
}


// PRIVATE methods ********************************

function _getBTreeString(bTree, shiftString, isLeftNode) {
    var verticalLine = "|";
    var hrlLine      = "____";
    var hrSpace      = "     ";
    var hrSpacePlusOne  = hrSpace +" ";
    var prefix = isLeftNode ? "L ":"R ";
    if (bTree) {
        if (isLeftNode === null ) {
            //Root node 
            outputString = outputString +" [ " +bTree.value + " ]";
        }else {
            outputString = outputString + "\n"+shiftString + verticalLine+  hrlLine + "[" +prefix+ bTree.value + "]";            
        }
        var isLeftPresent = bTree.left ? true : false;
        var isRightPresent = bTree.right ? true : false;
        var shiftStringNew = isLeftNode ? shiftString + verticalLine + hrSpace : shiftString + hrSpacePlusOne;
        
        if (isLeftPresent || isRightPresent ) {
            _getBTreeString(bTree.left, shiftStringNew, true);
            _getBTreeString(bTree.right, shiftStringNew, false);
        }

    } else {
        outputString = outputString + "\n";
        outputString = outputString + shiftString +  verticalLine+ hrlLine + "( "+ prefix+")";
    }
}
// PRIVATE methods ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


// TESTING code 

// var tmpb = generateSampleBinaryTree(8);
// tmpb.left.left = null;
// tmpb.right.right =null;
// tmpb.left.right.left.right =null;
// printBTree(tmpb);



//console.log(JSON.stringify(generateSampleBinaryTree(5)));


// var nodeLeft = new BTreeNode(null, null, "1");
// var nodeRight = new BTreeNode(null, null, "2");
// var nodeM = new BTreeNode(nodeLeft, nodeRight, "0");

// console.log(nodeLeft);
// console.log(nodeRight);
// console.log(nodeM);
// nodeLeft.value = "left";
// console.log(nodeM);