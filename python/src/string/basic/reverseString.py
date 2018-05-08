# Reverse a string using recurssion

def reverseWithRecursion(listOfChar, index):
  if (index+1 == len(listOfChar)):
    return listOfChar[index]
  r = reverseWithRecursion(listOfChar, index+1)
  return ''.join(r+listOfChar[index])

print(reverseWithRecursion("ABCD",0))

