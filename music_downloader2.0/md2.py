from pytube import YouTube, Playlist
import sys
import re
import os
from youtubesearchpython import VideosSearch
import csv


def main():
    try:
        if validation(sys.argv) == True:
            # Display help menu
            if sys.argv[1] in ['-h', '--help']:
                help()
                sys.exit()
            # Download from a file
            if sys.argv[1] in ['-f' , '--file']:    
                file_down(sys.argv[2])
            # searching and downloading a song
            if sys.argv[1] in ['-d', '--down', '--download']:
                search_down(sys.argv[2])

            else: 
                try:
                    download(sys.argv[1], sys.argv[2])

                    
                except:
                    sys.exit('An unexpected error occoured. Please check your URL')

        else:
            print('Invalid usage. Type -h for the help menu.')
    except IndexError:
        sys.exit('Invalid usage. Type -h for the help menu.')


def validation(cla):
    inputs = [
        '-v',
        '--video',
        '-p',
        '--playlist',

    ]

    try:
        # If the user wants the help menu
        if cla[1] in ['-h', '--help'] and len(cla) == 2:
            return True
        # If the user wants to download from a file
        if cla[1] in ['-f', '--file'] and len(cla) == 3 and (str(cla[2]).endswith('.txt') or str(cla[2]).endswith('.csv')):
            return True
        if cla[1] in ['-d', '--down', '--download'] and len(cla) == 3:
            return True

        # If the user wants to download a playlist or a video
        try:
            match = re.match(r'^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$', sys.argv[2])
        except:
            pass
        # If everything checks out
        if (len(cla) == 3) and (sys.argv[1] in inputs) and (match):
            return True
    except IndexError:
        pass


def download(type , url):
    # Downloading a single video
    if type in ['-v', '--video']:
        
        try:
            video = YouTube(url)
            stream = video.streams.filter(only_audio=True).first()
            print(f'\nDownloading {video.title}')
            
            downloaded_file = stream.download()
            change_ext(downloaded_file)
            print('Download successful!\n')
            
            
        except KeyError:
            print('Unable to fetch video information. Please check the URL')

    # Downloading an entire playlist
    else:
        pl = Playlist(url)
        i = 1

        for vid in pl.videos:
                try:   
                    stream = vid.streams.filter(only_audio=True).first()
                    print(f'\n{i}- Downloading {vid.title}')
                    
                    downloaded_file = stream.download()
                    change_ext(downloaded_file)

                    print(f'Downloaded {vid.title}.\n')
                    i += 1
                    
                except KeyError:
                    print('Unable to fetch video information. Please check the URL')


def change_ext(down_file):
    
    # Changing the extention to MP#
    base, ext = os.path.splitext(down_file)
    new_file = base + '.mp3'
    os.rename(down_file, new_file)


def file_down(filename):
    # Reading song names from the text file
    if filename.endswith('.txt'):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            sys.exit('File does not exist.')
    # Reading song names from a csv file
    else:
        lines = []
        try:
            with open(filename , 'r') as file:
                read = csv.reader(file)
                for item in read:
                    for song in item:
                        lines.append(song)

        except:
            sys.exit('An error occoured. Please check the filemane.')
    # Getting the URL and downloading the songs one by one
    
    for item in lines:
        search_down(item)



def search_down(song):
        result = VideosSearch(song + 'song' , limit=1).result()

        id = (result['result'])[0]['id']
        url = f'https://www.youtube.com/watch?v={id}'
        download('-v' , url)



def help():

    # HELP MENUUUUUUUUUU
    help = [
        f"\n{'_ ' * 52}\n",
        
        'USAGE:',
        '\n     python3 md.py [options] ([youtube url] or [filename])\n',
        '\nOPTIONS:',
        '\n     "-v" or "--video": Used while downloading one video in MP3 format.',
        '\n     "-p" or "--playlist": Used while downloading a whole playlist in MP3 format.',
        '\n     "-h" or "--help": Used to display the help menu.',
        '\n     "-f" or "--file": Used to read the song names from a file (must be ".txt" or ".csv")',
        '\n     "-d" or "--down": Used to download the song specified in the next argument',
        '\n\n   If "-f" or "--file" is used, the next argument must be the filename',


        f"\n{'_ ' * 52}\n"

    ]

    for item in help:
        print(item)


if __name__ == '__main__':
    main()
