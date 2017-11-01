# Bubble sort:
#     Sorts adjacent elements if they are worngly sorted
# Eg: T=[9,8,7,6,5,4,3,2,1]

def bubbleSort(I):
    A = I[:]
    for o in range(0,len(A)-1):
        for i in range(0,len(A)-o-1):
            if(A[i] > A[i+1]):
                A[i], A[i+1] = A[i+1], A[i]
    return A
# T=[9,8,7,6,5,4,3,2,1]
T = [5, 1, 4, 2, 8]
print(T)
print("***")
print(bubbleSort(T))

def bubbleRecurssion(A,index):
    if(len(A)-1 == index):
        return A
    if(A[index]> A[index+1]):
        A[index],A[index+1] = A[index+1], A[index]
    index +=1
    return bubbleRecurssion(bubbleRecurssion(A,index),index)

print("************")
print(bubbleRecurssion(T,0))
