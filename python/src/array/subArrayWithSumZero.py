#  Find sub array with 0 sum
#  Eg : A=[4, 2, -3, 1, 6]
#
#  Author : ikigai

# logic - using hashmap insert number
# localsum += n
# if(localsum in hashmap)
#   true
# false

def subArrayWithSumZero(A):
    sumAtIndex = [];
    localsum = 0;
    for n in A:
        localsum += n;
        if(localsum == 0 or localsum in sumAtIndex):
            return True
        else:
            sumAtIndex.append(localsum)
    return False

A=[4, 2, -3, 1, 6]
B=[4, 2, 0, 1, 6]
C=[1, 4, -2, -2, 5, -4, 3]
X=[-3, 2, 3, 1, 6]

print(subArrayWithSumZero(A))
print(subArrayWithSumZero(B))
print(subArrayWithSumZero(C))
print(subArrayWithSumZero(X))

#  Variation
#  Maximum Size Subarray Sum Equals k
#  Eg A = [1, -1, 5, -2, 3] , k = 3
#  Output : [1, -1, 5, -2]

#  Variation
#  Largest subarray with equal number of 0s and 1s
#  Also fina all subsequence where 0s = 1s
#  Input: arr[] = {1, 0, 1, 1, 1, 0, 0}
#  Output: 1 to 6 (Starting and Ending indexes of output subarray)
#
#  Input: arr[] = {1, 1, 1, 1}
#  Output: No such subarray
#
#  Input: arr[] = {0, 0, 1, 1, 0}
#  Output: 0 to 3 Or 1 to 4
