# Selection Sort
#     Group the list into two buckets, sorted and unsorted.
#     Select the lowest/largent element from the unsorted buket and place it
#     in the sorted bucket. Continue this till all elements are moved to sorted
#     bucket.
#

def selectionSort(A):
    for i in range(0,len(A)-1):
        loc = i
        x = A[i]
        for j in range(i+1,len(A)):
            if(A[j]< x):
                x = A[j]
                loc = j
        A[i],A[loc] = A[loc], A[i]
    return A

T = [5,2,7,0,1,3,10,9]
print(T)
print(selectionSort(T))
