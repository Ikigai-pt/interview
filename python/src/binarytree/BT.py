
# Binary tree defintion
import random
NODE_PRINT_SIZE = 6

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        print(val)

    def __init__(self,val, left = None ,right = None):
        self.left = left
        self.right = right
        self.val = val

def createRandomBinaryTree(level):
  # numberOfNode = pow(2,size) - 1
  # print(numberOfNode)
  tree = generateTree(level)
  return tree

def printBinaryTree(node):
  if node:
    print(node.val)
    printBinaryTree(node.left)
    printBinaryTree(node.right)

def generateTree(level):
  if(level < 0):
    return None
  n = Node(random.randint(0,99))
  n.right = generateTree(level-1)
  n.left = generateTree(level-1)
  # print(n.val)
  return n

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

