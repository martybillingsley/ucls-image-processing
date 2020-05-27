# Final Assignment: Image Processing
See the packet for the assignment


# How to Edit and Run Your Program
1) Choose the tab named *funcs.py*.<br>
2) Make changes to your program. <br>
3) In the bottom (terminal) window, type *python funcs.py*


# Function Reference

**makePicture (filename)**<br>			
Returns a Picture representation of the contents of the file. Use the files provided ("bear.jpg", "dog.jpg", "flower.jpg", etc.)<br>
Example:	img = makePicture("dog.jpg")<br>

**makeEmptyPicture (w, h c)**	<br>
Returns a Picture with the given width and height, filled with color c. <br>
Example:	img = makeEmptyPicture(640, 480, 'red')<br>
Example:	img = makeEmptyPicture(640, 480, (255, 0, 0))<br>

**show (img)**	<br>
Displays the specified Picture in its own window <br>
Example:	show(img)<br>

		
**getWidth (img)**	<br>
**getHeight (img)** 	<br>
Returns the width or height of the specified Picture. <br>
Examples:	w = getWidth(img)<br>
		      h = getHeight(img)<br>


**getRed (img, x, y)**	<br>
**getGreen (img, x, y)**<br>	
**getBlue (img, x, y)**<br>
Returns the amount of red or green or blue of the pixel at location x,y of the image.<br>
Example: 	r = getRed(img, 100, 100)<br>

**getColor (img, x y)**	<br>
Returns a three-tuple with the red, green, and blue of pixel at location x,y of the image.<br>
Example: 	r,g,b = getColor(img, 100, 100)<br>

**setRed (img, x, y, amount)**<br>
**setGreen (img, x, y, amount)**<br>	
**setBlue (img, x, y, amount)**	<br>
Sets the amount of red or green or blue of pixel at location x,y of the image.<br>
Examples: 	setRed(img, 100, 100, 255)<br>
            setBlue(img, 100, 100, 0)<br>

**setColor (img, x, y, r, g, b)**	<br>
Sets the color of pixel at location x,y of the image, given the red, green, and blue<br>
Example: 	setColor(img, 100 100, 255, 0, 255)<br>
