# REALITY

### Description:

## Program:

    This is a program that reminds you to do reality checks after a specified amount of time in order to 
    increase your chances of lucid dreaming. If no time is specified, it notifies you every fifteen minutes.

# main:

    This function checks the number of command-line arguments given by the user. If the number of command-line 
    arguments is more than three or is equal to two, it displays an error message and exits the program. Otherwise, 
    if the number of command line arguments is equal to three, it calls the "validate" function, "get_time" function 
    and then the "generate_notif" function passing in as input the return value of the "get_time" function.

# validate:

    This function takes in as a parameter the command-line arguments and validates them. If the first command-line 
    argument is not a positive integer or if the second command-line argument is not a valid input, the program exits 
    and displays an error message. The valid inputs are stored in the list called "valid_suffixes".

# get_time:

    This function converts the command-line arguments into a usable time by looking at the suffix and ditermining
    if the time given is in seconds, minutes or hours. If the time is in minutes, it is multiplyed by 60 to convert
    it into seconds and if the time is in hours, it is multiplyed by 3600. The value of time is then returned.

# generate_notif:

    This function takes in an optional parameter of time in seconds and generates a notification based on it
    until the program is closed.



