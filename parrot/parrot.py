import pyttsx3
import sys

def main():
    cli()

def cli():
    
    if sys.argv[1] == '-h':
        help_menu()
    
    try:
        is_valid = validation(sys.argv[1] , sys.argv[2] , len(sys.argv) , sys.argv[3] , sys.argv[4] , sys.argv[5])
    except IndexError:
        is_valid = validation(sys.argv[1] , sys.argv[2] , len(sys.argv))
    
    if is_valid[0] == '0':
        sys.exit(f'{error_messages(is_valid[1])}. Use "-h" for help menu.')

    try:
        words = text(sys.argv[1])
        tts(words , sys.argv[2] , sys.argv[3] , sys.argv[4] , sys.argv[5])
    except FileNotFoundError:
        sys.exit('File not found.')
    except IndexError:
        tts(words , sys.argv[2])

    

    

def validation(filename ,  output_file ,  arg_length ,voice='-f' , rate='60' , volume='100'):
    if filename.endswith('.txt') == False:
        return '0' , '0'
    
    if output_file.endswith('.mp3') == False:
        return '0' , '1'
    
    voices = ['-f' , '-m']
    if voice not in voices:
        return '0' , '2'
    
    try:
        if int(rate) < 0:
            return '0' , '3'
    except:
        return '0' , '4'
    
    try:
        if not (0 < int(volume) <= 100):
            return '0' , '5'
    except:
        return '0' , '6'
    
    valid_lengths = [3 , 6]
    if (arg_length not in valid_lengths):
        return '0' , '7'
    
    return '1'
    

def text(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content


def tts(words_to_say , output_file , voice='-f' , rate='60' ,  volume='100'):
    voicesss = {'-f' : 1 , '-m' : 0}
    engine = pyttsx3.init()
    engine.setProperty('rate' , rate)
    voices = engine.getProperty('voices')      
    engine.setProperty('voice', voices[voicesss[voice]].id)   
    engine.setProperty('volume', int(volume) / 100)
    engine.save_to_file(words_to_say , output_file)
    engine.runAndWait()


def error_messages(n):
    messages = {
        '0' : 'Text file must end in ".txt".',
        '1' : 'Output file must end in ".mp3".',
        '2' : 'Voice can only be "-f" or "-m".',
        '3' : 'Rate must be greater than 0.',
        '4' : 'Rate must be an integer.',
        '5' : 'Volume must be between 0 and 100.',
        '6' : 'Volume must be an integer.',
        '7' : 'Invalid number of command-line arguments.',
    }

    return messages[n]

def help_menu():
    lines = [
        '\n-----------------------------| HELP MENU |-----------------------------\n',
        '\nUSAGE:',
        '\npython parrot.py [input file] [output file] [voice] [rate] [volume]',
        '(Last three arguments are optional)\n',
        '\nInput file must end in ".txt"',
        '\nOutput file must end in ".mp3"',
        '\nVoice can either be male or female. Use -f for female and -m for male.',
        '\nVolume must be a number between 1 and 100 inclusive.',
        '\n------------------------------------------------------------------------\n'
    ]

    for line in lines:
        print(line)
    


if __name__ == '__main__':
    main()

