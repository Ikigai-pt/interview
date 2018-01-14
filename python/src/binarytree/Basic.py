# Basic Binary Tree Questions
from BT import createRandomBinaryTree, prettyPrintBT

# Find height of Binary Tree
def findHeight(n):
    height = 0
    if(n):
        height += max(findHeight(n.left), findHeight(n.right)) + 1
    return height

DEPTH = 4
tree = createRandomBinaryTree(DEPTH)
print(findHeight(tree))
# Check if two Binary Trees are identical
def checkTreesIdentical(a, b):
    if(a is None and b is None):
        return True
    if(a and b):
        return checkTreesIdentical(a.left,b.left) and checkTreesIdentical(a.right,b.right)
    if (a is None and b is not None) or (b is None and a is not None):
        return False

DEPTH = 2
a = createRandomBinaryTree(DEPTH)
b = createRandomBinaryTree(1+DEPTH)
print(checkTreesIdentical(a,b))
# Check if BT is a complete BT (Diff btw balanced & Complete BT)
# Determine if two nodes are cousins
# Print counsins of a given node
# Find diameter of BT
# Check if BT has symentric structure
# Find Lowest Common Ancestor of two nodes in BT
# Print All paths from root to leaf
# Print corner nodes of every level in BT
# 

    
