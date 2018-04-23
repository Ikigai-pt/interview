# Remove space from string "tes ting a s tring"
#

def shiftLeftByOne(index,input):
  return input[0:index] + input[index+1:len(input)]

def removeSpace(input):
  counter = 0
  while counter < len(input):
    if(input[counter] == ' '):
      input = shiftLeftByOne(counter,input)
      print(" found space "+input)
    counter+=1
  return input

ex = "tes ting a s tring"
print(removeSpace(ex));


# O(n) logic
# counter = 0
# if non-space then put current chan at index counter & increment counter
# add /n to the end after iteration is complete

def removeSpaceOn(input):
  counter = 0
  index = 0
  print(input)
  while index < len(input):
    if ( input[index] != ' ' ):
      input[counter] = input[index]
      counter+=1
    index+=1
  return ''.join(input[0:counter])

ex = "tes ting a s tring"
print(removeSpaceOn(list(ex)));

