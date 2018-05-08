function rotateMatrix(mat) {
    console.log(mat);
    var max = mat.length - 1;
    var min = 0;
    var loops = Math.floor(mat.length / 2);
    var xmin = 0;
    var ymin = 0;
    var xmax = max;
    var ymax = max;
    for (var i = 0; i < loops; i++) {
        var innerLoop = ymax - ymin;
        for (var k = 0; k < innerLoop; k++) {
            var tmp = mat[ymin][xmin + k];
            mat[ymin][xmin + k] = mat[ymax - k][xmin];
            mat[ymax - k][xmin] = mat[ymax][xmax - k];
            mat[ymax][xmax - k] = mat[ymin + k][xmax];
            mat[ymin + k][xmax] = tmp;
        }
        xmin++;
        ymin++;
        xmax--;
        ymax--;
    }
    console.log("-Rotated-");
    console.log(mat);
    console.log("-*******************************************-");

}

// TEST DATA
var matSym = [
    ['&', '&', '&', '&', '&'],
    ['|', '&', '&', '&', '-'],
    ['|', '|', '0', '-', '-'],
    ['|', '@', '@', '@', '-'],
    ['@', '@', '@', '@', '@']
];
var mat5 = [
    ['a1', 'a2', 'a3', 'a4', 'a5'],
    ['b1', 'b2', 'b3', 'b4', 'b5'],
    ['c1', 'c2', 'c3', 'c4', 'c5'],
    ['d1', 'd2', 'd3', 'd4', 'd5'],
    ['e1', 'e2', 'e3', 'e4', 'e5']
];

var mat4 = [
    ['a1', 'a2', 'a3', 'a4'],
    ['b1', 'b2', 'b3', 'b4'],
    ['c1', 'c2', 'c3', 'c4'],
    ['d1', 'd2', 'd3', 'd4']
];

var mat3 = [
    ['a1', 'a2', 'a3'],
    ['b1', 'b2', 'b3'],
    ['c1', 'c2', 'c3']
];

rotateMatrix(mat3);
rotateMatrix(mat4);
rotateMatrix(mat5);
rotateMatrix(matSym);

// LOGIC 
// In place replacemnet not using additional memory
//
// Lets take the following matrix as an example
// var mat3 = [
//     ['a1', 'a2', 'a3'],
//     ['b1', 'b2', 'b3'],
//     ['c1', 'c2', 'c3']
// ];

// One way to do an in place rotation is to use the following strategy

// a3 <- a1
// c3 <- a3
// c1 <- c3
// a1 <- c1

// Lets figure out the formula for the above rotation pattern 

// Lets refer each of the points using the co-ordinates.We Need to represent the array in y,x format as opposed to conventionl x,y format because of the way array stores data. For example  "a3" in the above matrix is located at [0][3] but if this array was a graph "a3" would be at (3, 0) which is 3 units in x direction and 0 units in y direction. For ease of deriving the logic going ahead each point in the array will be represented in (y,x) format

// If this matrix was represented as a graph with xy co-ordinates then each value in the matrix would look as follows

// let x = 0; y=0
// [
//  (y,   x)   (y,   x+1)   (y,   x+2)
//  (y+1, x)   (y+1, x+1)   (y+1, x+2)
//  (y+2, x)   (y+2, x+1)   (y+2, x+2)
// ]

// So as per the above representation I can access "C3" by mat[y+2,x+2] which is mat[2,2]

// Now lets transform  this 

// a3 <- a1
// c3 <- a3
// c1 <- c3
// a1 <- c1

// to a generic format
// (y,   x+2) =  (y,   x)
// (y+2, x+2) =  (y,   x+2)
// (y+2, x)   =  (y+2, x+2)
// (y,   x)   =  (y+2, x) 

// Assuming the matrix can be of any size the lets replace the constants with a variable 
// where ymin = y, xmin = x  likewise ymax = y+2 , xmax = x+2

// (ymin, xmax) =  (ymin, xmin)
// (ymax, xmax) =  (ymin, xmax)
// (ymax, xmin) =  (ymax, xmax)
// (ymin, xmin) =  (ymax, xmin) 

// Note so far we have just derived the formula for moving points at the four corners of the matrix. We subsequently will also have to move other points. Example "a2" needs to be moved to "b3".  Looking closely we see that there is a pattern to it as well . A more generic formula for moving any point is as follows. 

// (ymin +k , xmax   ) =  (ymin    , xmin +k)
// (ymax    , xmax -k) =  (ymin +k , xmax   )
// (ymax -k , xmin   ) =  (ymax    , xmax -k)
// (ymin    , xmin +k) =  (ymax -k , xmin   ) 

// Now by incrementing k you can move any rotate any point in the matrix outer loop. 
// Setting k = 0 will move 

// "a1" -> "a3" -> "c3" -> "c1" ->  "a1"

// when k =1 

// "a2" -> "b3" -> "c2" -> "b1" -> "a2"


// We have managed to rotate the outer loop in a matrix. Now we can dwell one level deaper and rotate the inner loop in the matrix. We need to be congnizant that the size of the loop is smaller as we go deeper so we adjust the ymin,xmin,ymax and xmax values as follows.


// xmin++;
// ymin++;
// xmax--;
// ymax--;


// A size "N" matrix can now be rotated in ((N/2)*(N-1)!) iterations which is O(n^2) with no additional memory. 

