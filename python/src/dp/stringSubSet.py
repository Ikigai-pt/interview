# Given a set of characters, output all combinations such that it's a valid set. ie "ab" => {a,b,ab}
# example "abc" => {a, b, c, ab, bc, ca, abc} . Note in a set 'ab' is same as 'ba' (Math definition)

ex1 = "abc"
# ['a', 'b', 'c', 'ab', 'bc', 'ac', 'abc']
ex2 = "abcd"
# ['a', 'b', 'c', 'd', 'cd', 'bc', 'bd', 'bcd', 'ab', 'ac', 'ad', 'acd', 'abc', 'abd', 'abcd']

def subStringSet(input, index):
    result = []
    if ( len(input) == index ):
        return []
    else:
        current = input[index]
        if (current not in result):
            result.append(current)
        subSet = subStringSet(input, index+1)
        if (subSet not in result):
            result = result + subSet
        print("index %d result len %d" %(index, len(result)))
        print(result)
        length = len(result)
        for i in range(0,length):
            if (current != result[i]):
                result.append(current+result[i])
        print("Final %s" %result)
        return result

solution = subStringSet(ex2,0)

print("size %d result %s" %(len(solution), solution))

# --------------------------------------------------------------
# Prakash : Good job!
# I think you can still optimize it further. You are constantly checking to make sure there are no 
# duplicates. Every time you add an element you need to iterate through all the existing elements to 
# ensure they dont already exist. 
# Here is a much simpler solution - the trick is to not add "a" , "b", "c" right away rather start with an
# empty string "" and append to it 
# First iteration
#   "" + a  => ["", a]
# Second iteration
#   "" +  b, a + b  => ["",a, b, ab]
# Third iteration
#   "" + c, a+c, b+c, ab+c = > ["", a, b, ab, c, ac, bc, abc]



def combination(inputStr):
    resultSet = [""]
    for ch in inputStr:
        localSet = []
        for val in resultSet:
            localSet.append(val + ch)
        resultSet.extend(localSet)
    return resultSet[1:]


# Testing - data 
input = "abc"
result =  combination(input)
print 'Result for ', input, 'is :', result
print 'Total elements in set :', len(result)
