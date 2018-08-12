var angle = 0;

//Creates the canvas
 function setup() {
	createCanvas(windowWidth, windowHeight);
}

//Resizes the canvas when the user's window is resized
function windowResized(){
	resizeCanvas(windowWidth, windowHeight);
}

function draw() {
//Creates the distance between the points
	var points = [
		[-200, -200, 200],
		[-200, 200, 200],
		[200, -200, 200],
		[200, 200, 200],
		[-200, -200, -200],
		[-200, 200, -200],
		[200, -200, -200],
		[200, 200, -200]
	];

//Matrices for rotation around the x, y, and z axes
	var rotationX = [
		[1, 0, 0],
		[0, Math.cos(angle), -Math.sin(angle)],
		[0, Math.sin(angle), Math.cos(angle)]
	];

	var rotationY = [
		[Math.cos(angle), 0, Math.sin(angle)],
		[0, 1, 0],
		[-Math.sin(angle), 0, Math.cos(angle)]
	];

	var rotationZ = [
		[Math.cos(angle), -Math.sin(angle), 0],
		[Math.sin(angle), Math.cos(angle), 0],
		[0, 0, 1]
	];

//Martix for projecting the 3D points into 2D
	var projection = [
		[1, 0, 0],
		[0, 1, 0]
	];

//Sets background to black
	background(0);

	for (p of points){
		//Rotates the points around all axes
		var rotated = matmul(rotationX, vecToMat(p));
		rotated = matmul(rotationY, rotated);
		rotated = matmul(rotationZ, rotated);
		//Projects the rotated points from 3D to 2D
		var projected2d = matToVec3(matmul(projection, rotated));
		//Finally draws the new points onto the screen
    ellipse(projected2d[0] + windowWidth/2, projected2d[1] + windowHeight/2, 20);
	}
	angle += 0.01;
}

//Converts a vector into a matrix. Vector can be of any length
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

//Converts a matrix into either a vector 2 or a vector 3. No more and no less.
function matToVec3(m){
	v = Array();
	v.push(m[0][0]);
	v.push(m[1][0]);
	if(m.length > 2){
			v.push(m[2][0]);
	}
	return v;
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

//My matmul function which will need more attention later on so I can use my own
//matmul function, rather than one I found from Google.

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
