# Authors: Jeremy Trendoff and Bryce Fritz
# Date Submitted: Apr 2nd, 2020
# Milestone #3, P8
# Description: The interactive UI for the ECOR1051 project.
# Student Numbers: 101160306, 101154817
# Team Identifier: 16

# Imports
from T16_image_filters import *


def ui_output() -> str:
    """
    Author: Bryce Fritz 
    Edited By: Jeremy Trendoff

    Prints out the UI and returns theinput given by the user.

    >>> ui_output()
    L)oad image  S)ave as
    2)-tone  3)-tone  X)treme contrast  T)int sepia  P)osterize  
    E)dge detect  I)mproved edge detect  V)ertical flip  H)orizontal flip
    Q)uit

    : 
    """
    print('L)oad Image ' + ' S)ave-as')
    print('2)-tone  ' + '3)-tone  ' + 'X)treme contrast  ' +
          'T)int sepia  ' + 'P)osterize')
    print('E)dge detect  ' + 'I)mproved edge detect  ' +
          'V)ertical flip  ' + 'H)orizontal flip  ')
    print('D)isplay Image  ' + 'Q)uit' + '\n')

    return input(': ')


def shell_clear() -> None:
    """
    Author: Bryce Fritz
    Edited By: Jeremy Trendoff

    Clears up some space in the python shell.
    """
    for i in range(1):
        print('\n')


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
                    'i', 'I', 'v', 'V', 'h', 'H', 'l', 'L', 's', 'S', 'q', 'Q', 'd', 'D']

    # Checks if the input is valid and returns
    if letter in vaild_inputs:
        return True
    else:
        print('No such command!')
        return False


def two_tone_action(col: str, col2: str) -> bool:
    colors = ['black', 'white', 'red', 'lime',
              'blue', 'yellow', 'cyan', 'magenta', 'gray']
    incorrect = []

    if (col in colors and col2 in colors):
        return True
    else:
        if (col not in colors):
            incorrect.append(col)
        if (col2 not in colors):
            incorrect.append(col2)

        print('Color inputs ' + str(incorrect) + ' are not valid!')
        print('Valid inputs include: ' + str(colors))

        return False


def three_tone_action(col: str, col2: str, col3: str) -> bool:
    colors = ['black', 'white', 'red', 'lime',
              'blue', 'yellow', 'cyan', 'magenta', 'gray']
    incorrect = []

    if (col in colors and col2 in colors and col3 in colors):
        return True
    else:
        if (col not in colors):
            incorrect.append(col)
        if (col2 not in colors):
            incorrect.append(col2)
        if (col3 not in colors):
            incorrect.append(col3)

        print('Color inputs ' + str(incorrect) + ' are not valid!')
        print('Valid inputs include: ' + str(colors))

        return False


def apply_filter(letter: str, image: Image) -> Image:
    """
    Author: Jeremy Trendoff

    Returns the Image changed by the filter or the response of a desired action.
    Takes a string to represent the input and the image to be changed.

    >>> image = apply_filter('t', image)
    >>> show(image)
    Returns disired action.
    """

    # Chooses what action to do based on input
    if (letter == 'l' or letter == 'L'):
        return load_image(choose_file())
    elif (image == None):
        print("No image loaded!")
        return None
    else:
        if (letter == '2'):
            col = input('Please type a color! ')
            col2 = input('Please type a color! ')

            if (two_tone_action(col, col2) == True):
                return two_tone(image, col, col2)
            else:
                return image
        elif (letter == '3'):
            col = input('Please type a color! ')
            col2 = input('Please type a color! ')
            col3 = input('Please type a color! ')

            if (three_tone_action(col, col2, col3) == True):
                return three_tone(image, col, col2, col3)
            else:
                return image
        elif (letter == 'x' or letter == 'X'):
            return extreme_contrast(image)
        elif (letter == 't' or letter == 'T'):
            return sepia_tinting(image)
        elif (letter == 'p' or letter == 'P'):
            return posterize(image)
        elif (letter == 'e' or letter == 'E'):
            return detect_edges(image, int(input('Please type a threshold value: ')))
        elif (letter == 'i' or letter == 'I'):
            return detect_edges_better(image, int(input('Please type a threshold value: ')))
        elif (letter == 'v' or letter == 'V'):
            return flip_vertical(image)
        elif (letter == 'h' or letter == 'H'):
            return flip_horizontal(image)
        elif (letter == 's' or letter == 'S'):
            save_as(image, input(
                "Please type in the filename and extension you'd like to use: "))
            return image
        elif (letter == 'd' or letter == 'D'):
            show(image)  # Display image
            return image
        else:
            return image


def image_processing() -> None:
    """
    Author: Jeremy Trendoff

    The function to run the interactive UI.

    >>> image_processing()
    Displays the UI and runs the rest of the program.
    """
    # Variables
    stop: bool = False
    counter: int = 0
    loaded_image: Image = None

    # While the user does not want to stop...
    while (stop == False):
        if (counter != 0):  # If it is not the first run...
            shell_clear()  # Clear some space.

        letter = ui_output()  # Take the users input

        if (check_input(letter) == True):  # If the input is valid...
            # If the user wants to quit...
            if (letter == 'q' or letter == 'Q'):
                stop = True  # Quit
            else:  # Otherwise
                loaded_image = apply_filter(
                    letter, loaded_image)  # Apply Action

        counter += 1  # Increase counter to show the amount of runs.


# Main Script
image_processing()










