# Final Assignment: Image Processing
See the packet for the assignment

# Function Reference

**makePicture (filename)**			
Returns a Picture representation of the contents of the file. Use the files provided ("bear.jpg", "dog.jpg", "flower.jpg", etc.)
Example:	img = makePicture("dog.jpg")

**makeEmptyPicture (w, h c)**	
Returns a Picture with the given width and height, filled with color c. 
Example:	img = makeEmptyPicture(640, 480, 'red')
Example:	img = makeEmptyPicture(640, 480, (255, 0, 0))

**show (img)**	
Displays the specified Picture in its own window 
Example:	show(img)

		
**getWidth (img)**	
**getHeight (img)** 	
Returns the width or height of the specified Picture. 
Examples:	w = getWidth(img)
		      h = getHeight(img)


**getRed (img, x, y)**	
**getGreen (img, x, y)**	
**getBlue (img, x, y)**
Returns the amount of red or green or blue of the pixel at location x,y of the image.
Example: 	r = getRed(img, 100, 100)

**getColor (img, x y)**	
Returns a three-tuple with the red, green, and blue of pixel at location x,y of the image.
Example: 	r,g,b = getColor(img, 100, 100)

**setRed (img, x, y, amount)**
**setGreen (img, x, y, amount)**	
**setBlue (img, x, y, amount)**	
Sets the amount of red or green or blue of pixel at location x,y of the image.
Examples: 	setRed(img, 100, 100, 255)
            setBlue(img, 100, 100, 0)

**setColor (img, x, y, r, g, b)**	
Sets the color of pixel at location x,y of the image, given the red, green, and blue
Example: 	setColor(img, 100 100, 255, 0, 255)
