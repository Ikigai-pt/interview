# Binary search - will use recurssion
# result = BS(start, mid) && BS(mid+1, end)

def binarySearch(left, right, input, number):
    if (right >= left):
        mid = left + (right - 1)/2
        print("mid %i"%mid)
        if (input[mid] == number):
            return 1
        elif (input[mid] < number ):
            return binarySearch(mid+1, right, input, number)
        else:
            return binarySearch(left, mid-1, input, number)
    else:
        return 0

eg  = [2, 3, 4, 10, 40]
print(eg)
print(" Binary Search %i " %binarySearch(0, len(eg)-1, eg, 4))
print(" Binary search %i " %binarySearch(0, len(eg)-1, eg, 6))
