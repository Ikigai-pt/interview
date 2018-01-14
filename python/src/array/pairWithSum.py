# Find pair with Sum
# Qn : Given an array A[] and a number x, check for pair in A[] with sum as x
# Eg : Let Array be {1, 4, 45, 6, 10, -8} and sum to find be 16
# Author: ikigai

# Assumption the array is sorted
def pairWithSumSorted(A,sum):
   start = 0;
   end = len(A)-1;
   while(start < end):
       localSum = A[start]+A[end]
       if(localSum == sum):
           return True
       if(localSum > sum):
           end -=1
       else:
           start +=1
   return False

# Set up test data
# Positive
A = [-8, 1, 4, 6, 10, 45]
#Negative
B =[1, 4, 45, 6, 10, -8]
print(pairWithSumSorted(A,10))
print(pairWithSumSorted(B,10))

def pairWithSumUnsorted(A,sum):
    sumComplement =[]
    for n in A:
        if(n in sumComplement):
            return True;
        else:
            sumComplement.append( sum-n )
    return False

print(pairWithSumUnsorted(B,10))
