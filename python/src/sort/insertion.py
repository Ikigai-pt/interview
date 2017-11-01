# Insertion sort : for element e find the best location in insert in
# the existing list
# eg: [5,2,7,1,9]
#

def insertionSort(A):
    for i in range(0,len(A)):
        x = A[i]
        for j in range(0,i):
            if(x < A[j]):
                A[j], A[i] = A[i] , A[j]
    return A

T = [5,2,7,0,1,3,10,9]
print(T)
print("*******")
print(insertionSort(T))
# TODO Implement insertion sort recursively

