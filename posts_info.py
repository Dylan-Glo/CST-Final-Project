'''
Johnny Huynh, Dylan
CST205
posts_info: has all the data for the images
4/16/21
CITED: 
https://www.parsehub.com/blog/what-is-web-scraping/
https://venngage.com/blog/data-visualization-infographic/
'''
posts_info = [
	{
		"id" : "week8api",
		"vid" : "s7wmiS2mSXY",
		"week" : "8", 
		"subject" : "API",
		"description" : "Application Programming Interface that defines interactions between software applications.",
		"details" : "A defined set of instructions you can send to a web service.  APIs allows developers to write programs to work with 3rd party programs.  Every API is different and has its own documentation.  JSON data typically has the data organized by its attributes and values, sepearted by colons.  Python supports JSON."
	},
	{
		"id" : "week8ws",
		"vid" : "Sjg4nI4svyk",
		"week" : "8",
		"subject" : "Web Scraping",
		"description" : "Web scraping is data extraction from websites",
		"details" : "This is essentail to the user to get data that more useful or easy to understand.  It can load the entire HTML code and search for user selected info.  Some will output into a spreadsheet or be used in an API.  In this class, we used beautifulSoup to get data out of HTMLs."
	},
	{
		"id" : "week11wapp",
		"vid" : "F7AK-WzpYdY",
		"week" : "11/12",
		"subject" : "Web Applications with Python",
		"description" : "Dive into the frameworks to help build applications",
		"details" : "Mainly used flask framwork to help build server side web apps.  The '@' is use to determine routes. We use templates so that it is easier to maintain html pages.  To prettify the pages, we use bootstrap to control the design."
	},
	{
		"id" : "week13cv",
		"vid" : "OcycT1Jwsns",
		"week" : "13",
		"subject" : "Computer Vision",
		"description" : "Automated extraction of information from images",
		"details" : "Processes image data with algorithms.  We used Numpy for vector and matrix representations.  OpenCV comes with a high level GUI modile.  Later, when we use classifiers to identify objects in images, we will always first convert the image to grayscale.  A classifier tells OpenCV what to look for in images.  "
	},
	{
		"id" : "week14dv",
		"vid" : "VyhLRJVoIrI",
		"week" : "14",
		"subject" : "Data Visualization",
		"description" : "Presenting data as pictures or graphs",
		"details" : "The goal is to make complex info easier to understand.  Raster graphics use a rectangular array of pixels.  Vector graphics are a series of geometric shapes.  Raster graphics describe which squares should be filled in.  Vector graphics describe grid points at which lines or curves should be drawn."
	},
	{
		"id" : "week15ds",
		"vid" : "VkXOzX73wJs",
		"week" : "15",
		"subject" : "Digital Sound",
		"description" : "Representation of sound recorded or converted into digital form.",
		"details" : "The rate of vibrations per second is the called the frequency.  The Sine wave is the simplest waveform.  One complete cycle of a 1 𝐻𝑧 sine wave starts at 0 on the y-axis and ends at 0 on the y-axis.  Waves in nature, including sounds waves, are continuous.  Computers cannot perfectly represet continuity.  Sampling rate describes how many sample rates per unit of time."
	}
]