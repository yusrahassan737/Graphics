var ctx = document.getElementById("cupcakeCanvas").getContext("2d");
var sprinkleClrs = ["rgb(205, 180, 219)", "rgb(255, 200, 221)", "rgb(255, 175, 204)", "rgb(189, 224, 254)", "rgb(72, 191, 227)"];
var cherry = "rgb(173, 19, 19)";

// Sprinkle-drawing function
function sprinkle(x, y, clr, type) {
  if (type === ".") {
    ctx.fillStyle = clr;
    ctx.beginPath();
    ctx.arc(x, y, 5, 0, Math.PI * 2)
    ctx.fill();
  }else if (type === "-") {
    ctx.fillStyle = clr;
    ctx.fillRect(x, y, 20, 5);
  }else {
    ctx.fillStyle = clr;
    ctx.fillRect(x, y, 5, 20);
}
}

function drawSprinkles() {
  // Draw a few random sprinkles
  for (var i = 0; i < 10; i++) {
    sprinkle(rdmize(400), rdmize(400), sprinkleClrs[rdmize(5)], [".", "l", "-"][rdmize(3)])
  }
  // Draw the cherry
  ctx.fillStyle = cherry;
  ctx.beginPath();
  ctx.arc(200, 200, 50, 0, Math.PI * 2)
  ctx.fill();
  ctx.fillStyle = "red";
  ctx.beginPath();
  ctx.arc(200, 200, 40, 0, Math.PI / 2)
  ctx.fill();
}

// Random number from 0 to a number function
function rdmize(num) {
  return Math.floor(Math.random() * num);
}

// Cupcake top
ctx.fillStyle = "beige";
ctx.fillRect(0, 0, 400, 400);