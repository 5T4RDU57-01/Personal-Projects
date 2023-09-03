import random
import sys
from pyfiglet import Figlet


CHOICES = ['rock' , 'paper', 'scissors']

def main():
    f = Figlet()
    f.setFont(font='slant')
    
    while True:

        try:

            play = input('Start: ').lower()
            computer = choice()

            if validation(play):
                pass
            else:
                print('Not a valid choice.')
                continue

            

            if win(play , computer) == True:
                print(f'{f.renderText("You won!")}\nThe computer chose {computer}')
                break
            elif win(play , computer) == False:
                print(f'{f.renderText("You lost!")}\nThe computer chose {computer}')
                break
            else:
                print(f'{f.renderText("Draw!")}\nThe computer chose {computer}\n')
        
        except EOFError:

            sys.exit()


def validation(usr_input):
    global CHOICES

    if usr_input in CHOICES:
        return True
    else:
        return False


def choice():
    global CHOICES
    return (random.choice(CHOICES))


def win(usr , comp):

    beats = {'rock' : 'paper' , 'paper' : 'scissors' , 'scissors' : 'rock'}

    if usr == comp:
        return None
    elif beats[comp] == usr:
        return True
    else:
        return False
    

if __name__ == '__main__':
    main()
