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
            var tmpCur = mat[ymin + k][xmax];
            mat[ymin + k][xmax] = mat[ymin][xmin + k];
            var tmpNext = mat[ymax][xmax - k];
            mat[ymax][xmax - k] = tmpCur;
            tmpCur = tmpNext;
            tmpNext = mat[ymax - k][xmin];
            mat[ymax - k][xmin] = tmpCur;
            tmpCur = tmpNext;
            tmpNext = mat[ymin][xmin + k];
            mat[ymin][xmin + k] = tmpCur;
        }
        xmin = xmin + 1;
        ymin = ymin + 1;
        xmax = xmax - 1;
        ymax = ymax - 1;

    }
    console.log("-Rotated-");
    console.log(mat);
    console.log("-*******************************************-");

}

// TEST DATA
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

// LOGIC 
// In place replacemnet not using additional memory
// TBD - Explain the logic.
// 