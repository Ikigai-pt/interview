from BT import createRandomBinaryTree
LEVEL = 2
root = createRandomBinaryTree(LEVEL)
# printBinaryTree(root)

#Pretty Print Binary Tree

# Depth :First find the max depth of the given binary tree
# Node size : 10 char
# PrintOffset = depth * NodeSpace
# Do inorder traversal and print the node values
# Decrement the depth by 1

NODE_PRINT_SIZE = 6
def generateOffset(length):
  text = ""
  offsetLength = int((length) * NODE_PRINT_SIZE)
  for i in range(0,offsetLength):
    text +=" "
  return text

def prettyPrintBT(node,offset):
  if node:
    prettyPrintBT(node.right,offset+1)
    pNode = "----[{0}]".format(node.val)
    print(generateOffset(offset)+pNode)
    print(generateOffset(offset)+"|")
    prettyPrintBT(node.left,offset+1)

print(prettyPrintBT(root,LEVEL))
