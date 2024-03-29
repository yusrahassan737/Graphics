var ctx = document.getElementById("myCanvas").getContext("2d");
var snow = "rgb(211, 238, 242)";
var shadowSnow = "rgb(181, 183, 201)";
var ground = "rgb(162, 164, 176)";
var shadowGround = "rgb(122, 124, 130)";
var shadowY = 355;

// Ground
ctx.fillStyle = ground;
ctx.fillRect(0, 320, 400, 80);

// Shadow
ctx.fillStyle = shadowGround;
ctx.fillRect(120, shadowY - 25, 230, 50);
ctx.beginPath();
ctx.arc(120, shadowY, 25, 0, 360);
ctx.fill();
ctx.beginPath();
ctx.arc(350, shadowY, 25, 0, 360);
ctx.fill();

// Snowman Base
ctx.fillStyle = shadowSnow;
ctx.beginPath();
ctx.arc(200, 300, 75, 0, 360);
ctx.fill();
ctx.beginPath();
ctx.arc(200, 200, 50, 0, 360);
ctx.fill();
ctx.beginPath();
ctx.arc(200, 125, 30, 0, 360);
ctx.fill();

// Snowman hilights
ctx.fillStyle = snow;
ctx.beginPath();
ctx.arc(185, 295, 60, 0, 360);
ctx.fill();
ctx.beginPath();
ctx.arc(190, 195, 40, 0, 360);
ctx.fill();
ctx.beginPath();
ctx.arc(195, 125, 25, 0, 360);
ctx.fill();

// Eyes
ctx.fillStyle = "black";
ctx.beginPath();
ctx.arc(190, 120, 5, 0, 360);
ctx.fill();
ctx.beginPath();
ctx.arc(210, 120, 5, 0, 360);
ctx.fill();

// Arms and mouth
ctx.beginPath();
ctx.moveTo(50, 180);
ctx.lineTo(160, 170);
ctx.moveTo(320, 130);
ctx.lineTo(240, 170);
ctx.strokeStyle = "black";
ctx.lineWidth = 4;
ctx.stroke();
ctx.beginPath();
ctx.arc(205, 130, 12, 0, Math.PI / 2);
ctx.stroke();

// Carrot Nose
ctx.fillStyle = "orange";
ctx.beginPath();
ctx.moveTo(205, 135);
ctx.lineTo(200, 125);
ctx.lineTo(180, 135);
ctx.closePath();
ctx.fill();