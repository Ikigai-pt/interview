# Max SubArray Kadane's Algo
# Referred Wiki to solve this problem
# https://en.wikipedia.org/wiki/Maximum_subarray_problem
#
# Enhanced version: Print the sub array elements
#
def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    start = 0;
    end = 0;
    counter = 0;
    for x in A[1:]:
        counter +=1;
        if(x + max_ending_here >= max_ending_here):
            end = counter;
        max_ending_here = max(x, max_ending_here + x)
        if(max_ending_here > max_so_far):
            start +=1;
            end = counter;
        print("start %d end %d " %(start,end))
        max_so_far = max(max_so_far, max_ending_here)
    print(A[start:end+1])
    return max_so_far

a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
b = [-2, -3, 4, -1, -2, 1, 5, -3]
print(a);
print(max_subarray(a));

print(b);
print(max_subarray(b));


# Variation of this problem set !
# Question: Value of each house on a street is represented by V[i]
# Robber plans to maximize his theft, given if H[i] is robbed
# then H[i-1] and H[i+1] cannot be robbed.


