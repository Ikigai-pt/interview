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
