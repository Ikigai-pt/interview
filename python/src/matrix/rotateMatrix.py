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
                else
                    O[rowLen-d-1][y]= M[rowLen-d-1:][rowLen-d-1]
            prettyPrint(O)
    return O

data = 0;
M = [[ randint(1,100) for r in range(4)] for c in range(4)]
prettyPrint(M)
prettyPrint(rotateMatrix90degree(M))
