# Input  : arr[] = {3, 10, 2, 1, 20}
# memo  : arr[] = {1, 4, , 2, 1}
# Output : Length of LIS = 3
# The longest increasing subsequence is 3, 10, 20

# Input  : arr[] = {3, 2}
# Output : Length of LIS = 1
# The longest increasing subsequences are {3} and {2}

# Input : arr[] = {50, 3, 10, 7, 40, 80}
# memo  : arr[] = {5, 3, 4, 4, 5, 5}
# Output : Length of LIS = 4
# The longest increasing subsequence is {3, 7, 40, 80}

# Steps
# think what data is required to make the decision
# what data is required for step (n+1) and step(n-1)
# Arrive at a recurrsive equation
# memoization
# pick or not pick !!
# Bottom-Up approach
# eg {3,10,2,1,20}
#   => OPT(n) = 20 ie 1,
#   => OPT(n-1) => max(OPT(n-1) + OPT(next(n))) ie 2
#   => OPT(n-2) => max(OPT(n-2) + OPT(next(n-1))) ie 2
#   => OPT(n-3) => max(OPT(n-3) + OPT(next(n-2))) ie 2
#   => OPT(n-4) => max(OPT(n-4) + OPT(next(n-3))) ie 3
# OPT(i) = max(OPT(i) + OPT(i+1))
# save the maxLenSubSeq + all indices


# LIS given an array of numbers find the largest non-continuous sequence of
# increasing numbers.
# Idea: if n = 1 then return 1
# n = 2 then store the index of last maxSeq

input = []
def longestIncSubSeq(lastMaxLength, lastMaxNumber, index):
    if ( index < len(input)):
        if ( input[index] >= lastMaxNumber ):
            return max(longestIncSubSeq(lastMaxLength + 1, input[index], index+1), longestIncSubSeq(lastMaxLength+1,
                input[index], index+2))
        else :
            return max(longestIncSubSeq(lastMaxLength, lastMaxNumber, index+1), longestIncSubSeq(lastMaxLength,
                lastMaxNumber, index+2))
    else :
        return lastMaxLength

def wrapper(data):
    global input
    input = data
    print(input)
    print(longestIncSubSeq(0, 0, 0))

eg1 = [ 10, 22, 9, 33, 21, 50, 41, 60, 80]
eg2 = [ 0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
eg3 = [ 0, 22, 9, 33, 21, 50, 41, 60]

wrapper(eg3)
wrapper(eg2)
wrapper(eg3)

## solved using Dynamic programming 
memo = []
def longestIncSubSeqV2(input):
    memo = [1] * len(input)

    for i in range ( 1, len(input)):
        for j in range( 0, i ):
            if ( input[i] > input[j] and memo[i] < memo[j] +1 ):
                memo[i] = memo[j] +1
    return max(memo)
print(eg1)
print(longestIncSubSeqV2(eg1))

