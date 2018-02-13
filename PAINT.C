//Ana lucia Diaz Leppe
#include <stdio.h>
#include <stdlib.h>
#include <dos.h>
#include <math.h>

#define MAX_VERTICES 100
int vertex[MAX_VERTICES][2];
int undoCounter = 0;
int redoCounter = 0;
#include "paint/GRAFICAS.H";
#include "paint/MOUSE.H";
#include "paint/BMPFILES.H";
#include "paint/BOTONES.H";
#include "paint/SHAPES.H";
#include "paint/PALETTE.H";
#include "paint/TOOLS.H";
#include "paint/CPBOARD.H";
#include "paint/TEXTO.H";

// Imprimir integer en modo texto printf("%d\n", MAX_X);

void main() {
	int z, x, y, clicked, xtemp, ytemp, edgesCount;
	int button, selectedBtn, tempColor, actualColor1, actualColor2;
	int actualWidth, actualPattern;
	int radio, rdX, rdY;
	int x1, y1, x2, y2, tempx, tempy;
	int sX1, sX2, sY1, sY2;
	char font[58][16*16];
	FILE *fontF;
	int selectedWidth, colorFill; //select width of line
	
	BITMAP bitmap;

	//el primer parametro es el modo
	//del registro BX
	if (SVGA(0x103, MAX_X, MAX_Y)) {
		printf("\r\n SVGA Error\r\n");
		return;
	}
	
	initMouse();
	adaptMouse(MAX_X, MAX_Y);
	
	if((fontF = fopen ("paint/fuente.fnt","rb"))== NULL){
	return;
	}
	for(x=0; x<58; x++){
	fread(&font[x], 1, 16*16, fontF);
	}
	fclose(fontF);
	
	openFileBMP(0, 0, "paint/pfondo.bmp", &bitmap);
	clicked = 0;
	//paintCanvas();
	paintPalette(FULL_PALETTE);
	colorFill = 1;   //initialize selected color pane
	actualColor1 = COLOR_FILL_1;  //initialize paint color
	actualColor2 = COLOR_FILL_2; //initialize paint color
	actualWidth = 1;  //initialize width
	actualPattern = 0; //initialize pattern
	
	while (1) {
		repaintMouse(&x, &y, &clicked, &xtemp, &ytemp);
		
		if (clicked == 1) {
		//listo
		//LINE BUTTON SELECTED
		if (x >= 130 && x <= 155 && y >= 40 && y < 60) {
		button = LINE;
		
		}
		//RECTANGLE SELECTED
		if (x >= 180 && x <= 200 && y >= 40 && y <= 60) {
		button = RECTANGLE;
		} 
		//CIRCLE CLICKED
		if (x >= 155 && x <= 175 && y >= 40 && y <= 60) {
		button = CIRCLE;
		}
		//ELLIPSE CLICKED
		if (x >= 205 && x <= 238 && y >= 40 && y <= 60) {
		button = ELLIPSE;
		}
		//POLYGON
		if (x >= 240 && x <= 270 && y >= 40 && y <= 60) {
		button = POLYGON;
		}
		
		//CIRCLE PAINT
		if (x >= 155 && x <= 175 && y >= 70 && y <= 90) {
		button = PAINT_CIRCLE;
		}
		//RECTANGLE PAINT
		if (x >= 180 && x <= 200 && y >= 70 && y <= 90) {
		button = PAINT_RECTANGLE;
		}
		//OVAL PAINT
		if (x >= 205 && x <= 238 && y >= 70 && y <= 90) {
		button = PAINT_ELLIPSE;
		}
		//STAR PAINT
		if (x >= 240 && x <= 270 && y >= 65 && y <= 90) {
		button = PAINT_POLYGON;
		}
		
		//PENCIL
		if (x >= 430 && x <= 445 && y >= 40 && y <= 55) {
		button = PENCIL;
		}
		
		//GET COLOR
		if (x >= 450 && x <= 472 && y >= 70 && y <= 90) button = PICKER;
		
		//SPRAY TOOL
		if (x >= 385 && x <= 425 && y >= 40 && y <= 82) button = SPRAY;
		
		//width1
		if (x >= 15 && x <= 105 && y >= 40 && y <= 50) actualWidth = WIDTH1;
		
		//width 2
		if (x >= 15 && x <= 105 && y >= 55 && y <= 65) actualWidth = WIDTH2;
		
		//width 3
		if (x >= 15 && x <= 105 && y >= 70 && y <= 80) actualWidth = WIDTH3;
		
		//width 4
		if (x >= 15 && x <= 105 && y >= 85 && y <= 95) actualWidth = WIDTH4;
		
		//NEW
		if (x >= 85 && x <= 113 && y >= 5 && y <= 30) {
		paintCanvas();
		}
		
		//ERASER
		if (x >= 430 && x <= 445 && y >= 70 && y <= 90) {
		button = ERASER;
		}
		
		//COLOR FILL SELECTED 1
		if (x >= 526 && x <= 565 && y >= 95 && y <= 130) colorFill = 1;
		
		//COLOR FILL SELECTED 2     
		if (x >= 568 && x <= 620 && y >= 95 && y <= 130) colorFill = 2;
		
		//BUCKET FILL
		if (x >= 450 && x <= 470 && y >= 40 && y <= 58) button = BUCKET;
		
		if (x >= 480 && x <= 498 && y >= 40 && y <= 58) button = TEXT;
		
		//SAVE IMAGE
		if (x >= 5 && x <= 32 && y >= 5 && y <= 30) {
		mouseHide(x, y);
		saveImage(0, 140, 800, 460, "paint/image.bmp");
		mouseShow(x, y);
		}
		
		//LOAD IMAGE
		if (x >= 45 && x <= 79 && y >= 2 && y <= 30) {
		mouseHide(x, y);
		loadImage(0, 140, "paint/image.bmp", &bitmap);
		openFileBMP(0, 0, "paint/header.bmp", &bitmap);
		paintPalette(FULL_PALETTE);
		mouseShow(x, y);
		
		}
		
		//COPY
		if (x >= 334 && x <= 370 && y >= 60 && y <= 75) button = COPY;
		
		//PASTE
		if (x >= 300 && x <= 325 && y >= 40 && y <= 90) button = PASTE;
		
		//CUT
		if (x >= 334 && x <= 370 && y >= 40 && y <= 55) button = CUT;
		
		//REDO
		if (x >= 130 && x <= 165 && y >= 5 && y <= 30) {
		mouseHide(x, y);
		saveUndo();
		redo();
		mouseShow(x, y);
		}
		
		//HELP
		if (x >= 480 && x <= 495 && y >= 70 && y <= 90) {
		openFileBMP(0, 0, "paint/help.bmp", &bitmap);
		paintPalette(FULL_PALETTE);
		}
		
		//PATTERN 1
		if (x >= 678 && x <= 710 && y >= 94 && y <= 130) actualPattern = 1;
		//PATTERN 2
		if (x >= 718 && x <= 756 && y >= 94 && y <= 130) actualPattern = 2;
		//PATTERN 3
		if (x >= 758 && x <= 795 && y >= 95 && y <= 130) actualPattern = 3;
		//undo
		if (x >= 224 && x <= 260 && y >= 81 && y <= 119) {
		mouseHide(x, y);
		saveRedo();
		undo();
		mouseShow(x, y);
		}
		
		//COLOR PICKER 
		if (x >= 526 && x <= 794 && y >= 30 && y <= 90) {
		mouseHide(x, y);
		tempColor = getPixel(x, y);
		if (colorFill == 1) {
		actualColor1 = tempColor;
		paintColorPickerOne(tempColor);
		}
		else {
		actualColor2 = tempColor;
		actualPattern = 0;
		paintColorPickerTwo(tempColor);
		}
		mouseShow(x, y);
		}
		
		
		if (button != selectedBtn) {
		mouseHide(x, y);
		selectedBtn = button;
		mouseShow(x, y);
		clicked = 0;
		}
		if (y > y1_Draw) {
		switch(selectedBtn) {
		case LINE:
		x1 = x;
		y1 = y;
		mouseHide(x, y);
		saveUndo();
		mouseShow(x, y);
		getMouse(&x,&y,&clicked);
		while(clicked==1) {
		  repaintMouse(&x, &y, &clicked, &xtemp, &ytemp);
		  //this could repaint the line in real time
		  //but it ereases everything else
		  savePixel(x1, y1, x, y, actualWidth);
		  drawLine(x1, y1, x, y, actualColor1, actualWidth);
		  reDrawLine(x1, y1, x, y, actualWidth);
		}
		mouseHide(x, y);
		drawLine(x1,y1,x,y, actualColor1, actualWidth);
		//delete file for animation
		remove("paint/pixels.txt");
		mouseShow(x, y);
		x1 = x; y1 = y; 
		break;
		case RECTANGLE:
		x1 = x;
		y1 = y;
		mouseHide(x, y);
		saveUndo();
		mouseShow(x, y);
		while (clicked == 1) {
		  repaintMouse(&x, &y, &clicked, &xtemp, &ytemp);
		  //savePixelRectangle(x1, y1, x, y, actualWidth);
		  //drawRectangle(x1, y1, x, y, actualColor1, actualWidth);
		  //reDrawRectangle(x1, y1, x, y, actualWidth);
		}
		mouseHide(x, y);
		drawRectangle(x1, y1, x, y, actualColor1, actualWidth);
		saveRedo();
		//remove("paint/pixels.txt");
		mouseShow(x, y);
		break;
		case CIRCLE:
		x1 = x;
		y1 = y;
		mouseHide(x, y);
		saveUndo();
		mouseShow(x, y);
		while (clicked == 1) {
		  radio = sqrt(pow(x-x1, 2) + pow(y-y1, 2));
		  repaintMouse(&x, &y, &clicked, &xtemp, &ytemp);
		}
		radio = radio/2;
		if (x1 < x ) {
		  x1 = x1 + radio;
		}
		if (x1 > x)  {
		  x1 = x1 - radio;
		}
		if (y1 < y ) {
		  y1 = y1 + radio;
		}
		if (y1 > y ) {
		  y1 = y - radio;
		}
		mouseHide(x, y);
		drawCircle(x1, y1, radio, actualColor1, actualWidth);
		saveRedo();
		mouseShow(x, y);
		break;
		case ELLIPSE:
		x1 = x;
		y1 = y;
		mouseHide(x, y);
		saveUndo();
		mouseShow(x, y);
		while (clicked == 1) {
		  rdX = fabs(x - x1);
		  rdY = fabs(y - y1);
		  repaintMouse(&x, &y, &clicked, &xtemp, &ytemp);
		}
		mouseHide(x, y);
		drawEllipse(x1, y1, rdX, rdY, actualColor1, actualWidth);
		saveRedo();
		mouseShow(x, y);
		break;
		case PAINT_RECTANGLE:
		x1 = x; y1 = y;
		mouseHide(x, y);
		saveUndo();
		mouseShow(x, y);
		while (clicked == 1) {
		  repaintMouse(&x, &y, &clicked, &xtemp, &ytemp);
		  //savePixelRectangle(x1, y1, x, y, actualWidth);
		  //drawRectangle(x1, y1, x, y, actualColor1, actualWidth);
		  //reDrawRectangle(x1, y1, x, y, actualWidth);
		}
		mouseHide(x, y);
		paintRectangle(x1, y1, x, y, actualColor1, actualColor2, actualWidth);
		saveRedo();
		//remove("paint/pixels.txt");
		mouseShow(x, y);
		break;
		case PAINT_CIRCLE:
		x1 = x;
		y1 = y;
		mouseHide(x, y);
		saveUndo();
		mouseShow(x, y);
		while (clicked == 1) {
		  radio = sqrt(pow(x-x1, 2) + pow(y-y1, 2));
		  repaintMouse(&x, &y, &clicked, &xtemp, &ytemp);
		}
		radio = radio/2;
		if (x1 < x ) {
		  x1 = x1 + radio;
		}
		if (x1 > x)  {
		  x1 = x1 - radio;
		}
		if (y1 < y ) {
		  y1 = y1 + radio;
		}
		if (y1 > y ) {
		  y1 = y - radio;
		}
		mouseHide(x, y);
		paintCircle(x1, y1, radio, actualColor1, actualColor2, actualWidth);
		saveRedo();
		mouseShow(x, y);
		break;
		case PAINT_ELLIPSE:
		x1 = x;
		y1 = y;
		mouseHide(x, y);
		saveUndo();
		mouseShow(x, y);
		while (clicked == 1) {
		  rdX = fabs(x - x1);
		  rdY = fabs(y - y1);
		  repaintMouse(&x, &y, &clicked, &xtemp, &ytemp);
		}
		mouseHide(x, y);
		paintEllipse(x1, y1, rdX, rdY, actualColor1, actualColor2, actualWidth);
		saveRedo();
		mouseShow(x, y);
		break;
		case POLYGON:
		x1 = x; y1 = y;
		x2 = x; y2 = y;
		mouseHide(x, y);
		saveUndo();
		mouseShow(x, y);
		while(clicked != 2) {
		  repaintMouse(&x, &y, &clicked, &xtemp, &ytemp);
		  while(clicked !=1 && clicked !=2 ) { 
		    repaintMouse(&x, &y, &clicked, &xtemp, &ytemp);
		  }
		  if(clicked == 1) {
		    mouseHide(x, y);
		    drawLine(x1, y1, x, y, actualColor1, actualWidth);
		    mouseShow(x, y);
		  }else{
		    mouseHide(x, y);
		    drawLine(x2, y2, x1, y1, actualColor1, actualWidth);
		    mouseShow(x, y);
		  }
		  x1 = x;
		  y1 = y;
		}
		break;
		case PAINT_POLYGON:
		//saveUndo();
		x1 = x; y1= y;
		x2 = x; y2 = y;
		edgesCount = 0;

		while (clicked != 2) {
			  repaintMouse(&x, &y, &clicked, &xtemp, &ytemp);
			  while(clicked != 1 && clicked != 2){
			    repaintMouse(&x, &y, &clicked, &xtemp, &ytemp);
			  }
			 if(clicked == 1) {
			    mouseHide(x, y);
			    //edgesCount is the vertex number
			    if (searchCoord(x, y) == 0) {
			      vertex[edgesCount][0] = x; //original position
			      vertex[edgesCount][1] = y; //original position
			      edgesCount++;
			    }
			    drawLine(x1, y1, x, y, actualColor1, 1);
			    mouseShow(x, y);
			    
			  } else {
			    mouseHide(x, y);
			    if (searchCoord(x2, y2) == 0) {
			      vertex[edgesCount][0] = x2; //final position
			      vertex[edgesCount][1] = y2; //final position
			    }
			    drawLine(x2, y2, x1, y1, actualColor1, 1);
			    mouseShow(x, y);
			  }
			  x1 = x;
			  y1 = y;
			}
			mouseHide(x, y);
			scanLine(edgesCount, actualColor2, actualWidth);
			mouseShow(x, y);
			xtemp = x; ytemp = y;
			break;
			case ERASER:
			xtemp = x;
			ytemp = y;
			mouseHide(x, y);
			saveUndo();
			while (clicked == 1 && y >= 140) {
			  drawLine(x, y, xtemp, ytemp, 255, actualWidth);
			  xtemp = x; ytemp = y;
			  getMouse(&x, &y, &clicked);
			}
			saveRedo();
			mouseShow(x, y);
			xtemp = x; ytemp = y;
			break;
			case BUCKET:
			mouseHide(x, y);
			saveUndo();
			bucket(x, y, actualColor2, getPixel(x, y), actualPattern);
			saveRedo();
			mouseShow(x, y);
			break;
			case PENCIL:
			mouseHide(x, y);
			saveUndo();
			x1 = x; y1 = y;
			while(clicked == 1 && y >= 140) {
			  drawLine(x, y, x1, y1, actualColor1, actualWidth);
			  x1 = x; y1 = y;
			  getMouse(&x, &y, &clicked);
			}
			saveRedo();
			mouseShow(x, y);
			xtemp = x; ytemp = y;
			break;
			case PICKER:
			mouseHide(x, y);
			tempColor = getPixel(x, y);
			if (colorFill == 1) {
			actualColor1 = tempColor;
			paintColorPickerOne(tempColor);
			}
			else {
			actualColor2 = tempColor;
			paintColorPickerTwo(tempColor);
			}
			mouseShow(x, y);
			break;
			case SPRAY:
			mouseHide(x, y);
			saveUndo();
			while(clicked == 1){
			  getMouse(&x, &y, &clicked); 
			  paintSpray(x, y, actualColor1, actualWidth);
			}
			saveRedo();
			mouseShow(x, y);
			xtemp = x; ytemp = y;
			break;
			case COPY:
			x1 = x; y1 = y;
			while (clicked == 1) {
			  repaintMouse(&x, &y, &clicked, &xtemp, &ytemp);
			}
			mouseHide(x, y);
			copyPixels(x1, y1, x, y);
			mouseShow(x, y);
			break;
			case PASTE:
			mouseHide(x, y);
			saveUndo();
			pastePixels(x, y);
			mouseShow(x, y);
			break;
			case CUT:
			x1 = x; y1 = y;
			mouseHide(x, y);
			saveUndo();
			mouseShow(x, y);
			while (clicked == 1) {
			  repaintMouse(&x, &y, &clicked, &xtemp, &ytemp);
			}
			mouseHide(x, y);
			cutPixels(x1, y1, x, y);
			mouseShow(x, y);
			break;
			case TEXT:
			mouseHide(x, y);
			saveUndo();
			showText(x, y, actualColor1, font);
			mouseShow(x, y);
			break;
			}
			}
			
			//close button
			if (x >= 768 && x <= 795 && y >= 0 && y <= 26 ) {
				clicked = 0;
				exitSVGA();
				break;
			}
		}
	}
}
