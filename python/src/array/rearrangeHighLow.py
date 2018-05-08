# Rearrage elements of array with alternate high low
# Eg:
#     Input  = [1,2,3,4,5,6,7]
#     Output = [1,3,2,5,4,7,6]
# Sol With Extra Space: O(nlogn) to sort
#     Sort array and pick one element from bottom
#     and another from top and insert into new array
#
# Sol Without Extra Space: O(n)
#     Use two index, i,index
#     if Left < CurrentElement > Right
#         nops
#     if Left > CurrentElement
#         fetchNextSmallElement()
#     if right < CurrentElement
#         fetchNextLargeElement()


# def rearrangeHighLow(A):
#     swapWithLargeAtIndex qjj= 0;
#     for(i = 0; i < len(A); i++):
#         if(i>0 and i < len(A)-1):
#             if(A[i-1] > A[i] ):
#                 swapIndex = i;
#             if(A[i] > A[i+1]):
#                 sawpIndex = i;
#
#             if(A[i-1] < A[i] && A[i] < A[i+1] )
import math

def rearrangeRecurssion(A):
    if(len(A) == 0):
        return A;
    offset =1;
    for i in range(1,(len(A)-1)):
        # print(" %d %d " %(A[i],A[i-1]))
        if(A[i] < A[i-1]):
            temp = A[i-1]
            A[i-1] = A[i]
            A[i] = temp
            # print("sawp %d "%(i))
        if(A[i] < A[i+1]):
            temp = A[i+1]
            A[i+1] = A[i]
            A[i] = temp
            # print("sawp %d "%(i))
        if(A[i] == A[i-1]):
            alt = 0;
            for j in range(i,len(A)-1):
                if(A[j] > A[i]):
                    alt = j
                    break;
            temp = A[i];
            A[i] = A[alt];
            A[alt] = temp;
            # print(A)

T =[ [1,1,1,2,2,2],[1,2,3,4,5,6,7], [9,6,8,3,7],[6,9,2,5,1,4]]
for test in T:
    print(test)
    rearrangeRecurssion(test)
    print(test)
    print("**************")


