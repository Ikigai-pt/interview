#  rotate a give nxn matrix clockwise
#   eg: m[5,4] = > [1,2,3,4]
#                  [5,6,7,8]
#                  [a,b,c,d]
#                  [e,f,g,h]
#    */
#   op: m[5,4] = > [e,a,5,1]
#                  [f,b,6,2]
#                  [g,c,7,3]
#                  [h,d,8,4]
#

from random import randint

def prettyPrint(M):
    for r in range(len(M)):
            print(M[r])
    print("\n")
def rotateMatrix90degree(M):
    #  if(direction == 'clockwise'):
    O = M;
    rowLen = len(M);
    colLen = len(M[0]);
    for d in range(0,rowLen/2):
        for y in range(0,colLen):
            start = M[y][y];
            #  O[rowLen-y-1][colLen-x-1] = M[x][rowLen-y-1]
            for r in range(0,rowLen):
                if(r%2 == 0):
                    O[r][y]= M[rowLen-d-1][r]
                else:
                    O[rowLen-d-1][y]= M[rowLen-d-1:][rowLen-d-1]
            prettyPrint(O)
    return O

def rotateMatrix(M):
    #let the matrix be arranged in x & y coordinates
    rowLen = len(M)
    colLen = len(M[0])
    firstVal = M[0][0]
    print("Col len %d Row Len %d", colLen,rowLen )
    for y in range(0,1):
        colLen -=1
        for x in range(1,5):
            print(x)
            if(x % 2 > 0):
                rowLen -=1
                print(M[rowLen -x +1][x-1])
                print(M[colLen -rowLen +x -1 ][colLen -rowLen -x])
                M[colLen - rowLen][colLen - rowLen] = M[rowLen -x +1][x-1]
            else:
                print(M[rowLen][rowLen])
                M[rowLen][x-2] = M[rowLen][rowLen]
            prettyPrint(M)
        M[0][rowLen] = firstVal
    return M

def rotateAnyMatrix(M):
    # base case M[1,1]
    if(len(M) == len(M[0]) == 1):
        return M
    rows = len(M)
    columns = len(M[0])

    for r in range(1,rows):
        for c in range(0,columns):
            fromR = rows - r
            fromC = c
            toR = r
            toC =  c
            print("from position %d ,%d" %(fromR, fromC))
            print("to position %d, %d"%(toR,toC))




data = 0;
M = [[ randint(1,100) for r in range(4)] for c in range(4)]
prettyPrint(M)
rotateAnyMatrix(M)
#prettyPrint(rotateMatrix(M))
