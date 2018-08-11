function setup() {
	createCanvas(windowWidth, windowHeight);
}

var angle = 0;
var projected2d = new Array();
var rotated = new Array();

function draw() {

	var points = [
		[windowWidth/2-200, windowHeight/2-200, 0],
		[windowWidth/2-200, windowHeight/2+200, 0],
		[windowWidth/2+200, windowHeight/2-200, 0],
		[windowWidth/2+200, windowHeight/2+200, 0]
	];

	var rotation = [
		[Math.cos(angle), -Math.sin(angle)],
		[Math.sin(angle), Math.cos(angle)]
	];

	var projection = [
		[1, 0, 0],
		[0, 1, 0]
	];

	background(0);
	for (p of points){
		var projected2d = matmul(projection, vecToMat(p));
		var rotated = matToVec3(matmul(rotation, projected2d));
		ellipse(rotated[0], rotated[1], 20);
	}
	angle += 0.01;
}

function vecToMat(v){
	var m = new Array();
	var i = 0;
	for (p of v){
		m.push([v[i]]);
		i++;
	}
	i = 0;
	return m;
}

function matToVec3(m){
	v = Array();
	v.push(m[0][0]);
	v.push(m[1][0]);
	if(m.length > 2){
			v.push(m[2][0]);
	}
	return v
}

/* Using a function I got off of Google because I'm too dumb to comprehend
what Daniel Shiffman was talking about. */
function matmul(a, b) {
  var rowsA = a.length, colsA = a[0].length,
      rowsB = b.length, colsB = b[0].length,
      m = new Array(rowsA);
  for (var r = 0; r < rowsA; ++r) {
    m[r] = new Array(colsB);
    for (var c = 0; c < colsB; ++c) {
      m[r][c] = 0;
      for (var i = 0; i < colsA; ++i) {
        m[r][c] += a[r][i] * b[i][c];
      }
    }
  }
  return m;
}

// function matmul(a, b){
// 	var colsA = a[0].length;
// 	var colsB = b[0].length;
// 	var rowsA = a.length;
// 	var rowsB = b.length;
// 	var result = [rowsA, colsB]
// 	if (colsA == rowsB){
// 		for (i = 0; i < rowsA; i++){
// 			for (j = 0; j < colsB; j++){
// 				var sum = 0;
// 				for (k = 0; k < colsB; k++){
// 					sum += a[i][k] * b[k][j];
// 				}
// 				result[i][j] = sum;
// 			}
// 		}
// 	}
// 	else{
// 		console.log("Columns of 'a' must match rows of 'b'.");
// 	}
// 	return result;
// }
