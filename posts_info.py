'''
Johnny Huynh, Dylan Ignacio
CST205
posts_info: has all the data for the images
4/16/21
'''
posts_info = [
	{
		"id" : "CommandLine",
		"vid" : "yz7nYlnXLfE",
		"week" : "1",
		"subject" : "Command Line",
		"description" : "Make use of the terminal emulator and its importance",
		"details" : """The command line aka terminal is a text-based interface that computers have that allow the users to input instructions into the computer. With the use of the command line, it allows the user to do various tasks such as create / delete files, run programs, and navigate through folders and files. 
		Before the introduction of Graphical User Interfaces (GUIs), computers used the command line to get most tasks done. By understanding and developing skills based on using the command line, it becomes much easier to develop and work on projects as well as increase developer efficiency. 
		For macOS it is called Terminal, while for Windows it is called PowerShell. Effectively they are the same thing, however, it is important to remember that the way to input instructions in the command line is different, varying based on the type of system you are using.
		There are a lot of different commands inside of the command line, therefore, we will just cover a few of the most important commands people should know when using it. For example: 
		cd - changes directories, 
		mkdir - creates a new directory, 
		mv - moves or rename files, 
		rm - remove files, 
		ls - list the files and folder inside of a directory, and
		cp - copy files.
		"""
	},
	{
		"id" : "PythonLanguage",
		"vid" : "Y8Tko2YC5hA",
		"week" : "2",
		"subject" : "Python Language",
		"description" : "Popular programming language, easy to learn and read",
		"details" : """One of the most popular and used programming languages out there by many developers in the field. Here is a link to the Python home page: https://www.python.org/.

		With Python, people are able to create a wide variety of different applications just like with any other language. The difference with Python is the fact that it comes across as a very beginner friendly language. The reason for this being the fact that it has a very short and simple syntax when writing as compared to other languages like Javascript. 

		Here are some of the basics:

		There are various types of data types, but the most basic and common data types are…
		int - integers,
		float - floating-point number (decimal numbers),
		str - strings (sequence of characters), and 
		bool - boolean values (True / False).

		Here are some operators in python that serve to add logic into programs…
		=  : assignment operator (allows user to assign variables a value), 
		==  : checks to see if two values are equal to one another, 
		> / >= : greater than / greater than or equal to, and 
		< / <= : less than / less than or equal to.

		There are various ways to store information, such as... 
		Lists - denoted with [], mutable, 
		Tuples - denoted with (), immutable, and 
		Dictionaries - holds various items using a key, value pair.

		With the use of loops, it allows programs to repeat code without having to write the same lines of code over and over again…
		For loop - runs specified code for a specific amount of times and 
		While loop - runs specified code while the condition for the loop stays true
		"""
	},
	{
		"id" : "DigitalImageFiltering",
		"vid" : "QMLbTEQJCaI",
		"week" : "3", 
		"subject" : "Digital Image Filtering",
		"description" : "Manipulating image data to change images",
		"details" : """Digital image processing is the use of different algorithms on image data in order to change the data for the image. These changes range from changing the brightness, size, and color levels of the image’s data.

		First, let’s start with color. The data for an image’s color come in a tuple of three values, (R, G, B). Each pixel in the image contains a tuple with different intensity values for Red, green, and blue that go into the tuple. By making changes to these values, the developer is able to change the color of the image however, they want.

		Another important thing to remember when working with images and image filtering is the way images are coordinated. Pixels are placed using an ordered pair (x, y), however, unlike a regular coordinate system, the origin (0,0) starts at the upper-left corner. Through these coordinates, the developer is able to change the image by the placement, size, and orientation.
		"""
	},
	{
		"id" : "DigitalImageColorManipulation",
		"vid" : "15aqFQQVBWU",
		"week" : "4", 
		"subject" : "Digital Image Color Manipulation",
		"description" : "Manipulating image data to change images",
		"details" : """Let’s start with the basics. The values used in the tuples that hold the color intensities range from 0 all the way to 255. With 0 being black and 255 being white. Each value in RGB contains a number from 0 - 255 that gives each pixel its color. Sidenote, there is also a value used to choose the transparency of the image in the format of RGBA.

		One filter for color manipulations is the negative of an image. In this manipulation, the user subtracts each value of RGB from 255 and sets each one as the new values. These images in turn produce an image with a very contrasting color scheme.

		Another color manipulation is how to convert an image to grayscale. By turning an image grayscale, it turns the image into a black and white image. It is important to remember when doing this that it is a lossy transformation. This means that when it is converted, it cannot be reverted into its color version. To get grayscale, you add the values of the RGB intensities and  divide them by three. Then set this value for all three color intensities.
		"""
	},
	{
		"id" : "ImageTransformations",
		"vid" : "dkp4wUhCwR4",
		"week" : "5", 
		"subject" : "Image Transfomrations",
		"description" : "Manipulating image data to change images",
		"details" : """We have gone over some of the basics of image manipulations such as converting an image to grayscale as well as getting the negative of an image. Here we will focus on the different uses of manipulating the position of pixels. By doing this we are able to do various manipulations such as collages, cropping, and scaling. 

		First we let’s talk about the pixels and where we are getting them from. There are two types of variables that we should try to keep track of: source and target index variables. Source refers to the pixels straight from the image, while target refers to the coordinates where the pixels are being placed. 

		By changing the x and y values or even the source values, many changes are able to be created. For example, to place an image in a different location, you just need to change the target x and y values. In order to crop an image, you just need to change the source x and y ranges. For rotating an image, all you need to do is swap the target x and y values to have it sideways. Finally, in order to grow or shrink an image, you just need to change the source x and y of the image data by increasing or decreasing it.
		"""
	},
	{
		"id" : "ObjectOrientedProgramming",
		"vid" : "pTB0EiLXUC8",
		"week" : "6", 
		"subject" : "Object Oriented Programming",
		"description" : "Way of programming that focuses on creating classes and objects",
		"details" : "Object oriented programming is a way of programming that focuses on utilizing classes and objects in order to create simpler programs that reuses code for different objects. By doing this, the developer is able to create complex objects built on reusable and simple structures. The way this is done is that, through object oriented programming, the developer creates their own custom data types aside from the ones such as strings, int, and floats. These are called classes. Through classes, it is able to store data and methods for the class. Then, with the classes, the user would create objects, which are just instances of the class. "
	},
	{
		"id" : "PLACEHOLDER3",
		"week" : "8", 
		"subject" : "API",
		"description" : "Application Programming Interface that defines interactions between software applications.",
		"details" : "A defined set of instructions you can send to a web service.  APIs allows developers to write programs to work with 3rd party programs.  Every API is different and has its own documentation.  JSON data typically has the data organized by its attributes and values, sepearted by colons.  Python supports JSON."
	},
	{
		"id" : "PLACEHOLDER4",
		"week" : "8",
		"subject" : "Web Scraping",
		"description" : "Web scraping is data extraction from websites",
		"details" : "Web scraping"
	}
]