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

def longestIncSubSeq(n, mlen, input):
    maxLenSubSeq = mlen
    if(n >= 0 && input[n] < input[memo[n+1]]):
        memo[n] = n
        mlen+=1
        maxLenSubSeq = max( longestIncSubSeq(n-1,mlen, input), mlen)
    return maxLenSubSeq

input = [ 3, 10, 2, 1, 20 ]
memo = [0] * (5+1)
print(longestIncSubSeq(4,1,input))
