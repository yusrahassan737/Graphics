var ctx = document.getElementById("myCanvas").getContext("2d");
var skinClr = "rgb(237, 185, 173)";
var hairClr = "rgb(128, 91, 16)";
var lightYellow = "rgb(245, 208, 115)";
var darkYellow = "rgb(235, 173, 17)";

// Back Hair
ctx.fillStyle = hairClr;
ctx.fillRect(165, 120, 50, 36, 5);

// Face
ctx.arc(190, 100, 35, 0, 360);
ctx.fillStyle = skinClr;
ctx.fill();

//neck + shoulders
ctx.fillRect(182, 130, 15, 25, 2);
ctx.fillRect(150, 155, 80, 35, 5);
ctx.beginPath();
ctx.arc(145, 162, 10, 0, 360);
ctx.fill();
ctx.beginPath();
ctx.arc(232, 162, 10, 0, 360);
ctx.fill();

//ears
ctx.beginPath();
ctx.arc(160, 106, 10, 0, 360);
ctx.arc(220, 106, 10, 0, 360);
ctx.fill();

// Arms
ctx.beginPath();
ctx.moveTo(144, 160);
ctx.lineTo(157, 233);
ctx.moveTo(232, 160);
ctx.lineTo(225, 233);
ctx.strokeStyle = skinClr;
ctx.lineWidth = 18;
ctx.stroke();

// Hair
ctx.fillStyle = hairClr;
ctx.fillRect(160, 65, 10, 45);
ctx.fillRect(205, 65, 20, 50);
ctx.fillRect(155, 65, 69, 15);
ctx.fillRect(175, 50, 30, 15);

// Dress Bottom
ctx.beginPath();
ctx.arc(190, 330, 110, 0, 360);
ctx.fillStyle = lightYellow;
ctx.fill();
ctx.fillRect(80, 340, 220, 60);

// Dress Middle
ctx.fillStyle = darkYellow;
ctx.fillRect(162, 170, 55, 60);
ctx.beginPath();
ctx.moveTo(157, 183);
ctx.lineTo(170, 220);
ctx.moveTo(223, 183);
ctx.lineTo(212, 220);
ctx.moveTo(217, 220);
ctx.lineTo(185, 240);
ctx.moveTo(162, 220);
ctx.lineTo(195, 240);
ctx.strokeStyle = darkYellow;
ctx.lineWidth = 15;
ctx.stroke();

// Dress Top
ctx.beginPath();
ctx.moveTo(130, 165);
ctx.lineTo(260, 180);
ctx.moveTo(120, 180);
ctx.lineTo(250, 165);
ctx.strokeStyle = lightYellow;
ctx.lineWidth = 15;
ctx.stroke();