# Merge Sort:
#     Divide an conquer, split the array into two and recursivelly divide till
#     the subset is sorted. Merge them back and sort again
# T = [5,2,7,0,1,3,10,9]


# Recursive merge sort uses additional memory
def mergeSort(I):
    if(len(I)==0 or len(I)==1):
        return I
    upperBound = len(I)
    lowerBound = 0
    mid = round((upperBound-lowerBound)/2)
    A = mergeSort(I[lowerBound:mid])
    B = mergeSort(I[mid:upperBound])
    MIN = min(len(A),len(B))
    C = [None] * (len(A)+len(B))
    i=j=k= 0
    for c in range(0,len(C)):
        if(i >= len(A) or j >= len(B)):
            break
        if A[i] < B[j]:
            C[k] = A[i]
            i+=1
        else:
            C[k] = B[j]
            j+=1
        k+=1
    if(j<len(B)):
        C[k:] = B[j:]
        k+=len(B[j:])
    if(i<len(A)):
        C[k:] = A[i:]
    print(C)
    return C

#Recursive merge sort without additional memory

T = [5,2,7,0,1,3,10,9]
# T = [6,5,10,9]
print(T)
print(mergeSort(T))

T1 = [8,7,6,5,4,3,2,1]
print(T1)
print(mergeSort(T1))

