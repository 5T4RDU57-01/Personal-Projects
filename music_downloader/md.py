from pytube import YouTube, Playlist
import sys
import re
import os


def main():
    try:
        if validation(sys.argv) == True:
            if sys.argv[1] in ['-h', '--help']:
                help()
                sys.exit()
            
            try:
                download(sys.argv[1], sys.argv[2])
                print(f'Download successful!\nExiting now...')  
                
            except:
                sys.exit('An unexpected error occoured. Please check your URL')

        else:
            print('Invalid usage. Type -h for the help menu.')
    except IndexError:
        sys.exit('Invalid usage. Type -h for the help menu.')


def validation(command_line_arguments):
    inputs = [
        '-v',
        '--video',
        '-p',
        '--playlist',

    ]
    try:
        if command_line_arguments[1] in ['-h', '--help'] and len(command_line_arguments) == 2:
            return True
        try:
            match = re.match(r'^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$', sys.argv[2])
        except:
            pass
        if (len(command_line_arguments) == 3) and (sys.argv[1] in inputs) and (match):
            return True
    except IndexError:
        pass


def download(type , url):
    if type in ['-v', '--video']:
        
        try:
            video = YouTube(url)
            stream = video.streams.filter(only_audio=True).first()
            print(f'Downloading {video.title}\n')
            
            downloaded_file = stream.download()
            base, ext = os.path.splitext(downloaded_file)
            new_file = base + '.mp3'
            os.rename(downloaded_file, new_file)
            
            
        except KeyError:
            print('Unable to fetch video information. Please check the URL')

    else:
        pl = Playlist(url)
        i = 1
        for vid in pl.videos:
                try:
                    
                    stream = vid.streams.filter(only_audio=True).first()
                    print(f'\n{i}- Downloading {vid.title}')
                    downloaded_file = stream.download()
                    
                    base, ext = os.path.splitext(downloaded_file)
                    new_file = base + '.mp3'
                    os.rename(downloaded_file, new_file)
                    
                    print('Downloaded in MP3 format.\n')
                    i += 1
                    
                except KeyError:
                    print('Unable to fetch video information. Please check the URL')


def help():
    help = [
        f"\n{'_' * 82}\n",
        
        'USAGE:',
        '\n     python3 md.py [options] [youtube url]\n',
        '\nOPTIONS:',
        '\n     "-v" or "--video": Used while downloading one video in MP3 format.',
        '\n     "-p" or "--playlist": Used while downloading a whole playlist in MP3 format.',
        '\n     "-h" or "--help": Used to display the help menu.',

        f"\n{'_' * 82}\n"

    ]

    for item in help:
        print(item)


if __name__ == '__main__':
    main()
