#### PARROT

### Description:

    This is a program that takes as input a text file and an output mp3 file and three other command-line arguments
    which correspond to the voice, rate of speaking and volume. It uses the "pyttsx3" library to convert the text in 
    the text file into an audio output and saves it to an mp3 file with the desired name.

## Usage:

    python parrot.py [input file] [output file] [voice] [rate] [volume]

    The name of the input file must end in ".txt" and the name of the output file must end in ".mp3".
    The last three arguments are optional but if you do choose to use them then the voice must be 
    either male of female. Use "-m" for male and "-f" for female. The volume must be a number betwen
    1 and 100 inclusive.

### Functions:

## main:

    This function just calls the "cli" function. Yup, that's it...

## cli:

    This function looks at the command-line arguments and sends them to the validate function in order to be validated,
    after which it sends them to the "tts" function to generate an audio output. If the input file is not found or the
    input fails the validation checks, function exits the program and gives the user an error message.

## validation:

    This function validates the command-line arguments given by the user.
    First, it checks if the input file and output file end with ".txt" and ".mp3" respectively, after which it checks
    if the voice argument is either "-m" or "-f" and then it checks if the rate of speaking is a postive integer and if
    the volume is a postive integer between 1 and 100 inclusive. Lastly, it checks of the number of the command-line
    arguments is either 3 or 6. If the input fails any of these checks, the function returns the "0" (in place of the 
    boolean False as it was causing problems in the main function [bool object is not subscriptable]) and another number
    that is used to generate error codes in the cli function.

## text:

    This function takes in as input the name of the input file and returns the text in the file.

## tts:

    This function takes as input the words to be said, the output file and three optional arguments (voice , rate of speaking
    and the volume). It sets the propeties of the pyttsx3 engine and then outputs the words to be said into an mp3 file as
    audio.

## error_messages:

    This function takes in as input a number "n" (second value of the validation function) and returns the corresponding error
    message.

## help:

    This function prints the help menu that specifies the usage instructions.