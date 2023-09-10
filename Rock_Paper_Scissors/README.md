# Rock Paper Scissors

### Description:

## Program:

    This is a program that plays rock paper scissors with you. If the match ends in a draw, you are prompted to play again.

## main:

    This function prompts the user to play and then randomly chooses "rock", "paper" or "scissors"using the Random module.
    It then validates the user's choice by using the "validate" function. If the user input is not a valid choice, the user is prompted again. 
    Otherwise, it ditermines if the user has won, lost or if a draw has occoured. If a draw happenes, the user is prompted again.
    the result of the match is printed on the screen using the "pyfiglet" module. If at any point in the program the user sends
    an EOF signal, the program exits.

## validate:

    This function validates the user input by checking if it is in the list of valid inputs called "CHOICES". If the input
    is indeed in the list, the function returns True. If not, then it returns False.

## win:

    This function takes as input the user's choice aswell and the computer's randoml generated choice and ditermines if the
    user has won, lost, or entered a draw. It does this using a dictionary whose keys are the choices that are made by the 
    computer and the values are the user's choice that can beat the computer. If the user's choice beats the computer, the
    function returns True, if the choice does not beat the computer, it returns Fase. If a draw happens, the function returns None. 
