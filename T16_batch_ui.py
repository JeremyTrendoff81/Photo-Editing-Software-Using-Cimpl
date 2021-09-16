# Author: Adrian Comisso and Jeremy Trendoff
# Date Submitted: Apr 2nd, 2020
# Milestone #3, P8
# Description: The batch user interface for ECOR1051
# Student #: 101153609, 101160306
# Team Identifier: 16

# Imports
from T16_image_filters import *


def check_input(letter: str) -> bool:
    """
    Author: Jeremy Trendoff

    Returns the validity of an input. 
    Takes a str parameter representing the input.

    >>> check_input('t')
    True

    >>> check_input('z')
    False
    """

    # A list representing the valid inputs
    vaild_inputs = ['2', '3', 'x', 'X', 't', 'T', 'p', 'P', 'e', 'E',
                    'i', 'I', 'v', 'V', 'h', 'H']

    # Checks if the input is valid and returns
    if letter in vaild_inputs:
        return True
    else:
        print('Error: ' + "'" + letter + "'" +
              " does not correspond to a filter!")
        return False


def apply_filter(letter: str, image: Image) -> Image:
    """
    Author: Jeremy Trendoff

    Returns the Image changed by the filter.
    Takes a string to represent the input and the image to be changed.

    >>> image = apply_filter('t', image)
    >>> show(image)
    Displays filtered image.
    """

    # Selects and returns the desired image based on input.
    if (letter == '2'):
        return two_tone(image, 'yellow', 'cyan')
    elif (letter == '3'):
        return three_tone(image, 'yellow', 'magenta', 'cyan')
    elif (letter == 'x' or letter == 'X'):
        return extreme_contrast(image)
    elif (letter == 't' or letter == 'T'):
        return sepia_tinting(image)
    elif (letter == 'p' or letter == 'P'):
        return posterize(image)
    elif (letter == 'e' or letter == 'E'):
        return detect_edges(image, 10)
    elif (letter == 'i' or letter == 'I'):
        return detect_edges_better(image, 10)
    elif (letter == 'v' or letter == 'V'):
        return flip_vertical(image)
    elif (letter == 'h' or letter == 'H'):
        return flip_horizontal(image)
    else:
        return None


def image_processing(file: str) -> None:
    """
    Original Author: Adrian Comisso
    Edited By: Jeremy Trendoff

    The function to run the batch UI.
    Takes a string to represent the file selected by the user. 

    >>> image_processing(choose_file())
    Returns the results of the batch file commands.
    """

    # Opens the file
    txt = open(file)

    # Reads the file
    for line in txt:
        text = line.split(" ")
        if ('\n' in text[-1]):  # If there is an enter...
            text[-1] = text[-1][0:1]  # Take it out of the command.
        image_new = load_image(text[0])  # Assign the image.
        # Apply the filters
        for counter in range(2, len(text)):
            # If the input is valid...
            if (check_input(text[counter]) == True):
                # Apply filter.
                image_new = apply_filter(text[counter], image_new)
        save_as(image_new, text[1])  # Save final image


# Main Script
image_processing(choose_file())

