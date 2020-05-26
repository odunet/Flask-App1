
function setup()
{
	//create a canvas for the robot
	createCanvas(windowWidth, windowHeight);
}

function draw()
{
	//image(img, 0, 0);
	strokeWeight(6);

	//robots head
	fill('pink');
	stroke('black');
	rect(1000, 250, 300, 300, 20);


	//robots antenna
	fill('chocolate');
	stroke('black');
	ellipse(1150, 220, 60, 60);

	fill(200, 0, 200);
	stroke('black');
	rect(1110, 230, 80, 30);

	//robots eyes
	stroke('black');
	fill(255);
	ellipse(1075, 350, 80, 80);
	point(1075, 350);
	ellipse(1225, 350, 80, 80);
	point(1225, 350);
	stroke('yellow');
	strokeWeight(4);
	ellipse(1075, 350, 60, 60);
	ellipse(1225, 350, 60, 60);
	stroke('blue');
	strokeWeight(4);
	ellipse(1075, 350, 40, 40);
	ellipse(1225, 350, 40, 40);
	stroke('red');
	strokeWeight(4);
	ellipse(1075, 350, 20, 20);
	ellipse(1225, 350, 20, 20);



	//robots nose
	stroke('black');
  fill(255, 0, 0);
	ellipse(1150, 390,30,20)
	//triangle(250, 220, 200, 300, 300, 300);

	//robots ears
	stroke('black');
	rect(980, 330, 30, 100);
	rect(1290, 330, 30, 100);

	//robots mouth
	stroke('black');
	noFill();
	beginShape();
	vertex(1075, 490);
	vertex(1100, 520);
	vertex(1125, 490);
	vertex(1150, 520);
	vertex(1175, 490);
	vertex(1200, 520);
	vertex(1225, 490);
	endShape();
}
