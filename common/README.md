### Description:

    This is a program that uses command-line arguments to read from a file and dispalys the n most common items,
    with n being the second command-line argument and the file to read from being the first command-line argument.

### Usage:

    python common.py [filename.txt] [n]

    Filename must end in ".txt" and n must be a number.

### Functions:

## main:

    This function first uses the validate function to validate the command-line arguments and then uses the common
    function to get the specified number of the most common words. If the number of command-line arguments is less
    than two, or the file specified does not exist, it exits the program and prints an error message.

    Then, the function prints the most common words and the number of times they occoured.

## common:

    This function finds the most common words in the file and the number of times they occour and the returns them as
    a list of tuples. First, it opens the file in the utf-8 encoding and then cycles through the lines of the file.
    It then gets the words on the lines using the split() method and adds them to a dictionary along with the number
    of times they occour. Lastly, it returns the specified amount of the most common words.

## validation:

    This function takes as input the first and seconds command-line arguments and the length of the command-line
    arguments and validates them. If the filename does not end in ".txt", the function returns 0 (numbers used for
    generating error messages.) , if the second command-line argument is not a number then it returns 1 and lastly if
    the number of command line arguments is more than three, it returns 3. The default return value of this function
    is None.

## error_message:

    This function takes in as input a number and returns an error message based on that.
    