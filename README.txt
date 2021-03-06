Photofilter(R) version 1.0 01/04/2020

The project leader can be reached at:
Voice: 647 960 3099
Website: www.sce.carleton.ca
Email: jeremytrendoff@cmail.carleton.ca

Description:
____________

- This project contains three python files that allow for basic photo editing through 9
photo filters. The project utilizes two user interfaces, a interactive UI and a batch UI. 
The interactive UI displays the user with a set of commands. When a filter command is entered, 
the resulting image is displayed. The batch UI allows for a text file, with a specific layout, 
to be parsed through the program and saves the resulting image(s). Appling filters is accumulative.  


- The project is made up of three files:
	T16_interactive_ui.py	- The interactive UI python script.	
	T16_batch_ui.py		- The batch UI python script.
	T16_image_filters.py	- The filter puthon script.


Installation:
_____________

Python 3.7.4 or later must be installed.

Uses the python library Pillow and, therefore, this library must be installed.

Uses functions from Cimpl.py therefore Cimpl.py must be installed for the program to run.
Cimpl.py is provided in this repository, make sure that this file is saved in the same directory
the code is in.


Usage:
______

- All python files must be saved in the same location.


- In order to use the batch UI, a text file must be created in the format that can be parsed.
The format is: 

1) Name of the image to be edited. Include extension.
2) The desired filename of the saved image. Include extension.
3) The desired filter commands.

Example:

test_image.png test.png 2 3 X
test_image.png test1.png T P V 


- To run the program from the command line, navigate to the directory where the project files
have been saved and depending on the UI, use one of these commands:

> python T16_interactive_ui.py

When prompted, enter any of the on-screen commands. Commands are the letters designated 
with a ')' next to them. Commands can be upper or lowercase.

Example:
L)oad image, L/l is the command. 

> python T16_batch_ui.py

When prompted, select the text file you'd like to use. Make sure that this file has met 
the format stated eariler. 


- The project can also be run through an IDE. To do this, install a python capable IDE, 
open the desired UI code and run. The python files must still be saved in the same place.  
  

- Valid commands for the interactive UI are the ones shown. Valid filter commands for 
the batch UI are, both upper and lower case: '2', '3', 'x', 't', 'p', 'e', 'i', 'v', 'h'.


- When using the interactive UI, filters cannot be executed when no image is loaded.


Credits: 
________

Jeremy Trendoff - Noted Author

Adrian Comisso - Noted Author

Bryce Fritz - Noted Author


Copyright 2020-2021 Carleton University Corporation. All rights reserved.

Photofilter and its use are subject to a license agreement and are also subject to copyright,
trademark, patent and/or other laws.
