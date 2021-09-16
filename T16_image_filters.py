# Authors: Jeremy Trendoff, Adrian Commiso and Bryce Fritz
# Date Submitted: Apr 2nd, 2020
# Milestone #3, P8
# Description: All filter functions for the ECOR1051 project.
# Team Identifier: 16

# Imports
from Cimpl import choose_file, create_color, create_image, get_color,\
    set_color, show, copy, save_as, load_image, get_width,\
    get_height, Image

# Functions provided from the school for use


def grayscale(image: Image) -> Image:
    """
    PROVIDED BY ECOR1051 STAFF FOR USE

    Return a grayscale copy of image.

    >>> image = load_image(choose_file())
    >>> gray_image = grayscale(image)
    >>> show(gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:

        # Use the pixel's brightness as the value of RGB components for the
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.

        brightness = (r + g + b) // 3

        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int

        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)
    return new_image

# Personalized functions for more functionality


def get_individual_colors(pict: Image, x: int, y: int, rgb: str) -> int:
    """
    Author: Jeremy Trendoff

    Returns the individual red, green or blue value of the given pixel 
    in the given image.

    Takes an image, two integers and a string as parameters. 
    The Image parameter represents the image being analyzed. 
    The two ints are the x andy coordinates and the string represents which 
    color to extract. 
    'r' for red, 'b' for blue and 'g' for green. 

    >>> test = get_individual_colors(load_image('red_image.jpg'), 1, 1, 'r')
    >>> print(test)
    155

    >>> test = get_individual_colors(load_image('red_image.jpg'), 1, 1, 'g')
    >>> print(test)
    0

    >>> test = get_individual_colors(load_image('red_image.jpg'), 1, 1, 'b')
    >>> print(test)
    0
    """
    r, g, b = get_color(pict, x, y)

    if (rgb == 'r'):
        return r
    elif (rgb == 'b'):
        return b
    elif (rgb == 'g'):
        return g


def adjust_component(color: int) -> int:
    """
    Returns the centre value of preset intervals of rgb colors.
    to be used in conjunction with the posterize filter.

    >>>adjust_component(61)
    31
    >>>adjust_component(100)
    95
    >>>adjust_component(150)
    159
    >>>adjust_component(200)
    223
    """
    if 0 <= color <= 63:
        return(31)
    if 64 <= color <= 127:
        return(95)
    if 128 <= color <= 191:
        return(159)
    if 192 <= color <= 255:
        return(223)


def tone_filter_color_assigner(color_list: list) -> list:
    """
    Author: Jeremy Trendoff

    Returns the RGB values of the colors selected in the 
    two, three tone filters.

    Accepts a list of colors inputed by the user and assigns the related RGB 
    value to the coorisponding position in a list.

    >>> tone_filter_color_assigner(['red', 'blue'])
    [(255,0,0), (0,255,0)]
    """

    # Variables
    colors = ['black', 'white', 'red', 'lime', 'blue', 'yellow', 'cyan',
              'magenta', 'gray']
    rgbs = [(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255),
            (255, 255, 0), (0, 255, 255), (255, 0, 255), (128, 128, 128)]

    return_list = []

    # Color Processing
    for color in color_list:
        for i in range(len(colors)):
            if (color == colors[i]):
                return_list.append(rgbs[i])

    return return_list


# Red Channel
def red_channel(image: Image) -> Image:
    """
    Author: Jeremy Trendoff

    Returns a new image where the color of each pixel has been changed to 
    just the red value. 

    Takes an Image parameter. This Image represents the image tht will 
    be passed through the filter.

    >>> image = load_image(choose_file())
    >>> red = red_channel(image)
    >>> show(red)
    returns image

    or

    >>> show(red_channel(load_image(choose_file())))
    returns image
    """

    new_image = copy(image)  # Creates a copy of the image to filter
    for x, y, (r, g, b) in image:
        # Creates the new color of the pixel
        filtered_red = create_color(r, 0, 0)
        # Sets the new color to the pixel
        set_color(new_image, x, y, filtered_red)

    return new_image

# Green Channel


def green_channel(image: Image) -> Image:
    """
    Author: Jeremy Trendoff

    Returns a new image where the color of each pixel has been changed to 
    just the green value. 

    Takes an Image parameter. This Image represents the image tht will be passed 
    through the filter.

    >>> image = load_image(choose_file())
    >>> green = green_channel(image)
    >>> show(green)
    returns image

    or

    >>> show(green_channel(load_image(choose_file())))
    returns image
    """

    new_image = copy(image)  # Creates a copy of the image to filter
    for x, y, (r, g, b) in image:
        # Creates the new color of the pixel
        filtered_green = create_color(0, g, 0)
        # Sets the new color to the pixel
        set_color(new_image, x, y, filtered_green)

    return new_image

# Blue Channel


def blue_channel(image: Image) -> Image:
    """ 
    Author: Jeremy Trendoff

    Returns a new image where the colour of each pixel has been changed to only 
    have its blue value, when given a image. 

    >>> image = load_image(choose_file())
    >>> blue = blue_channel(image)
    >>> show(blue)
    returns image

    or

    >>> show(blue_channel(load_image(choose_file())))
    returns image
    """
    new_image = copy(image)  # Creates a copy of the image to filter
    for x, y, (r, g, b) in image:
        # Creates the new color of the pixel
        filtered_blue = create_color(0, 0, b)
        # Sets the new color to the pixel
        set_color(new_image, x, y, filtered_blue)

    return new_image

# Combine


def combine(red: Image, green: Image, blue: Image) -> Image:
    """
    Author: Adrian Comisso

    Retrun and image called combined_image that contains the combination 
    of the 3 channels.

    >>>combine(load_image("red_image.jpg"),load_image("green_image.jpg"), \ 
    load_image("blue_image.jpg")))
    returns full color image called combined_image
    """
    combined_image = copy(red)  # Copies the image
    for x, y, (r, g, b) in red:
        # Assigns the RGB values to variables
        red_pix = r
        green_pix = get_individual_colors(green, x, y, 'g')
        blue_pix = get_individual_colors(blue, x, y, 'b')

        # Sets the color of the new image
        set_color(combined_image, x, y, create_color(
            red_pix, green_pix, blue_pix))

    save_as(combined_image, 'combined_image.png')  # Saves the image
    return combined_image

# Two-tone


def two_tone(image: Image, color_1: str, color_2: str) -> Image:
    """
    Author: Jeremy Trendoff

    Note: To use this filter, the Cimpl file must be saved in the same 
    location as this filter.

    Returns a two-tone version of the image. 

    Takes an Image parameter to represent the image and two strings to 
    represent the two colors. 

    >>> image = load_image(choose_file())
    >>> new_image = two_tone(image)
    >>> show(new_image)
    Returns a three-toned image and displays it

    or

    >>> show(two_tone(load_image(choose_file())))
    Returns three-toned image and displays it
    """

    # Variables needed to execute the filters
    color_values = tone_filter_color_assigner([color_1, color_2])

    color_1_rgb = color_values[0]
    color_2_rgb = color_values[1]

    # Image Processing
    new_image = copy(image)  # Makes a copy of the image
    for x, y, (r, g, b) in new_image:
        avg = (r + g + b) // 3  # Calculates the average of the RGB values

        # Chooses what RGB value to use for each pixel based on the average RGB
        if (avg >= 0 and avg <= 127):
            set_color(new_image, x, y,
                      create_color(color_1_rgb[0],
                                   color_1_rgb[1], color_1_rgb[2]))
        elif (avg >= 128 and avg <= 255):
            set_color(new_image, x, y,
                      create_color(color_2_rgb[0],
                                   color_2_rgb[1], color_2_rgb[2]))

    return new_image  # Returns the image

# Three-tone


def three_tone(image: Image, color_1: str, color_2: str, color_3: str) -> Image:
    """
    Author: Jeremy Trendoff

    Note: To use this filter, the Cimple file must be saved in the same place 
    as the filter.

    Returns a three-tone version of the image. 

    Takes an Image parameter to represent the image and three strings to 
    represent the three colors. 

    >>> image = load_image(choose_file())
    >>> new_image = three_tone(image)
    >>> show(new_image)
    Returns a three-toned image and displays it

    or

    >>> show(three_tone(load_image(choose_file())))
    Returns three-toned image and displays it
    """

    # Variables needed to execute the filter
    color_values = tone_filter_color_assigner([color_1, color_2, color_3])

    color_1_rgb = color_values[0]
    color_2_rgb = color_values[1]
    color_3_rgb = color_values[2]

    # Image Processing
    new_image = copy(image)  # Creates a copy of the image
    for x, y, (r, g, b) in new_image:
        avg = (r + g + b) // 3  # calculates the average color value

        # Chooses which color to use for each pixel based on the average value
        if (avg >= 0 and avg <= 84):
            set_color(new_image, x, y,
                      create_color(color_1_rgb[0],
                                   color_1_rgb[1], color_1_rgb[2]))
        elif (avg >= 85 and avg <= 170):
            set_color(new_image, x, y,
                      create_color(color_2_rgb[0],
                                   color_2_rgb[1], color_2_rgb[2]))
        elif (avg >= 171 and avg <= 255):
            set_color(new_image, x, y,
                      create_color(color_3_rgb[0],
                                   color_3_rgb[1], color_3_rgb[2]))

    return new_image  # Returns the image

# Sepia Tinting


def sepia_tinting(image: Image) -> Image:
    """
    Author: Jeremy Trendoff

    Note: To use this filter, the Cimpl file must be saved in the same place as 
    this filter.

    Returns a sepia tinted version of the image.

    Takes an Image parameter to represent the image being tranformed. 

    >>> image = load_image(choose_file())
    >>> new_image = sepia_tinting(image)
    >>> show(new_image)
    Returns sepia tinted image and displays it

    or

    >>> show(sepia_tinting(load_image(choose_file())))
    Returns sepia tinted image and displays it
    """

    new_image = copy(image)  # Makes a copy of the image
    new_image = grayscale(new_image)  # Puts the image through the grayscale
    # filter in order to then do sepia tinting

    # Image Processing
    for x, y, (r, g, b) in new_image:
        avg = (r + g + b) // 3  # Calculates the average color value

        # Selects the degree of change with the rgb values based on the average
        # value
        if (avg < 63):
            col = create_color(r * 1.1, g, b * 0.9)
            set_color(new_image, x, y, col)
        elif (avg >= 63 and avg <= 191):
            col = create_color(r * 1.15, g, b * 0.85)
            set_color(new_image, x, y, col)
        elif (avg > 191):
            col = create_color(r * 1.08, g, b * 0.93)
            set_color(new_image, x, y, col)

    return new_image  # returns the image

# Posterize


def posterize(image: Image) -> Image:
    """
    Return an image with a smaller range of color than the original 
    aka posterized.

    Requires adjust_component function.

    >>>posterize(p2-original.png)
    returns posterized image
    """
    poster = copy(image)  # Copies the image

    # Image Processing
    for x, y, (r, g, b) in image:
        set_color(poster, x, y, create_color(adjust_component(r),
                                             adjust_component(g),
                                             adjust_component(b)))

    return(poster)

# Extreme Contrast


def extreme_contrast(image: Image) -> Image:
    """
    Author: Bryce Fritz

    Returns a extreme contrasted version of the image 

    >>> image = load_image(chose_file())
    >>> new_image = extreme_contrast(image)
    >>> show(new_image)
    returns an image
    """

    new_image = copy(image)  # Makes a copy of the image
    for x, y, (r, g, b) in image:  # Extreme contrasts each pixel
        if 0 <= r <= 127:
            r = 0
        else:
            r = 255
        if 0 <= g <= 127:
            g = 0
        else:
            g = 255
        if 0 <= b <= 127:
            b = 0
        else:
            b = 255

        # Creates the new pixels by combining rgb values
        filtered = create_color(r, g, b)
        set_color(new_image, x, y, filtered)  # Creates filtered image

    return new_image  # Returns the image

# Edge Detection


def detect_edges(image: Image, threshold: int) -> Image:
    """
    Author: Jeremy Trendoff

    Note: To use this filter, the Cimple file must be saved in th same place 
    as the filter.

    Returns a version of the image that looks like a pencil sketch. 

    Takes an Image parameter to represent the image and an integer to represent 
    a threshold. 

    >>> image = load_image(choose_file())
    >>> new_image = detect_edges(image)
    >>> show(new_image)
    Returns a pencil sketch image and displays it

    or

    >>> show(detect_edges(load_image(choose_file())))
    Returns pencil sketch image and displays it
    """

    height = get_height(image)  # Gets the height of the image.
    new_image = copy(image)  # Copies the image

    # Image Processing
    for x, y, (r, g, b) in new_image:
        brightness = (r + g + b) // 3  # Calculates the brightness

        if ((y + 1) < height):  # If there is a pixel below...
            # Gets the color of the pixel below
            color_below = get_color(new_image, x, y + 1)
            # Calculates the brightness of the pixel below
            brightness_below = (
                color_below[0] + color_below[1] + color_below[2]) // 3

            # Calculates the contrast of the two pixels
            contrast = abs(brightness - brightness_below)

        else:  # If there is no pixel below...
            # Set the pixel's color to white.
            set_color(new_image, x, y, create_color(255, 255, 255))
            contrast = 0  # Sets contrast to 0

        # If the contrast is greater than the threshold...
        if (contrast > threshold):
            # Set the pixel's color to black
            set_color(new_image, x, y, create_color(0, 0, 0))
        else:  # Otherwise...
            # Set the pixel's color to white
            set_color(new_image, x, y, create_color(255, 255, 255))

    return new_image

# Improved Edge Detection


def detect_edges_better(image: Image, threshold: int) -> Image:
    """
    Author: Adrian Comisso

    Note: To use this filter, the Cimple file must be saved in th same place 
    as the filter.

    Returns a version of the image that looks like a pencil sketch. 

    Takes an Image parameter to represent the image and an integer to 
    represent a threshold. 

    >>> image = load_image(choose_file())
    >>> new_image = detect_edges(image)
    >>> show(new_image)
    Returns a pencil sketch image and displays it

    or

    >>> show(detect_edges(load_image(choose_file())))
    Returns pencil sketch image and displays it
    """
    new_image = copy(image)  # Copies the image
    height = get_height(new_image)  # Gets the height of the image
    width = get_width(new_image)  # Gets the width of the image

    # Image Processing
    for x, y, (r, g, b) in new_image:
        brightness = (r + g + b) // 3  # Calculates the brightness

        # Statemaents for pixel below
        if ((y + 1) < height):  # If there is a pixel below...
            # Gets the color of the pixel below
            color_below = get_color(new_image, x, y + 1)
            # Calculates the brightness of the pixel below
            brightness_below = (
                color_below[0] + color_below[1] + color_below[2]) // 3

            # Calculates the contrast of the two pixels
            contrast_below = abs(brightness - brightness_below)

        else:  # If there is no pixel below...
            # Set the pixel's color to white.
            set_color(new_image, x, y, create_color(255, 255, 255))
            contrast_below = 0  # Sets contrast to 0

        # Statements for pixel to the right
        if ((x + 1) < width):  # If there is a pixel to the right...
            # Gets the color of the pixel to the right
            color_right = get_color(new_image, x + 1, y)
            # Calculates the brightness of the pixel to the right
            brightness_right = (
                color_right[0] + color_right[1] + color_right[2]) // 3

            # Calculates the contrast of the two pixels
            contrast_right = abs(brightness - brightness_right)

        else:  # If there is no pixel to the right...
            # Set the pixel's color to white.
            set_color(new_image, x, y, create_color(255, 255, 255))
            contrast_right = 0  # Sets contrast to 0

        # Statements to change the colors based on contrast
        # If the contrast is greater than the threshold...
        if (contrast_below > threshold or contrast_right > threshold):
            # Set the pixel's color to black
            set_color(new_image, x, y, create_color(0, 0, 0))
        else:  # Otherwise...
            # Set the pixel's color to white
            set_color(new_image, x, y, create_color(255, 255, 255))

    return new_image

# Flip Vertical


def flip_vertical(image: Image) -> Image:
    """
    Author: Jeremy Trendoff

    Note: To use this filter, the Cimple file must be saved in th same 
    place as the filter.

    Returns a vertically flipped version of the image. 
    The vertical flip switches the pixels across an invisble, 
    vertical line through the center of the image. 

    Takes an Image parameter to represent the image. 

    >>> image = load_image(choose_file())
    >>> new_image = flip_vertical(image)
    >>> show(new_image)
    Returns a pencil sketch image and displays it

    or

    >>> show(flip_vertical(load_image(choose_file())))
    Returns pencil sketch image and displays it
    """

    new_image = copy(image)  # Copies the image
    height = get_height(new_image)  # Gets the height
    width = get_width(new_image)  # Gets the width

    # Image Processing
    for x in range(width // 2):
        for y in range(height):
            # If the pixel opposite is in bounds...
            if ((width - x) < width):
                # The the color of the pixels
                pixel_color = get_color(new_image, x, y)
                other_pixel_color = get_color(new_image, width - x, y)

               # Flip the color values
                set_color(new_image, x, y,
                          create_color(other_pixel_color[0],
                                       other_pixel_color[1],
                                       other_pixel_color[2]))
                set_color(new_image, width - x, y,
                          create_color(pixel_color[0],
                                       pixel_color[1],
                                       pixel_color[2]))

    return new_image

# Horizontal Flip


def flip_horizontal(image: Image) -> Image:
    """
    Author: Bryce Fritz

    Note: To use this filter, the Cimple file must be saved in th same place 
    as the filter.

    Returns a horizontally flipped version of the image. The horizontal flip 
    switches the pixels across an invisble, horizontal line through 
    the center of the image. 

    Takes an Image parameter to represent the image. 

    >>> image = load_image(choose_file())
    >>> new_image = flip_horizontal(image)
    >>> show(new_image)
    Returns a pencil sketch image and displays it

    or

    >>> show(flip_horizontal(load_image(choose_file())))
    Returns pencil sketch image and displays it
    """

    new_image = copy(image)  # Copies the image
    height = get_height(new_image)  # Gets the height
    width = get_width(new_image)  # Gets the width

    # Image Processing
    for y in range(height // 2):
        for x in range(width):
            # If the pixel opposite is in bounds...
            if ((height - y) < height):
                # The the color of the pixels
                pixel_color = get_color(new_image, x, y)
                other_pixel_color = get_color(new_image, x, height - y)

               # Flip the color values
                set_color(new_image, x, y,
                          create_color(other_pixel_color[0],
                                       other_pixel_color[1],
                                       other_pixel_color[2]))
                set_color(new_image, x, height - y,
                          create_color(pixel_color[0],
                                       pixel_color[1], pixel_color[2]))

    return new_image

# This is a test program script if you would like to test the filter code.
# If you choose to do this, please save the 'p2-original.jpg' image with this.
# This sved image method is used so that all the filters can run quickly.
# Except for the combine filter, select the red, green and blue images in P2
# to run that.

# show(red_channel(load_image('p2-original.jpg')))
# show(green_channel(load_image('p2-original.jpg')))
# show(blue_channel(load_image('p2-original.jpg')))
# show(combine(load_image(choose_file()),load_image(choose_file()),load_image(choose_file())))
# show(two_tone(load_image('p2-original.jpg'), 'black', 'white'))
# show(three_tone(load_image('p2-original.jpg'), 'black', 'white', 'red'))
# show(sepia_tinting(load_image('p2-original.jpg')))
# show(posterize(load_image('p2-original.jpg')))
# show(extreme_contrast(load_image('p2-original.jpg')))
# show(detect_edges(load_image('p2-original.jpg'), 10))
# show(detect_edges_better(load_image('p2-original.jpg'), 10))
# show(flip_vertical(load_image('p2-original.jpg')))
# show(flip_horizontal(load_image('p2-original.jpg')))
