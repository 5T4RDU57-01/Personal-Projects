### Music Downloader

## Description:

    This is a program that takes two command line arguments (except when displaying the help menu) with the first one being 
    either video ('-v' or '--video') or playlist ('-p' or '--playlist') and the second one being the video or playlist URL.
    It then uses those arguments to download the video or playlist and lastly, it converts the files which were orignally
    in MP4 format to the MP3 format.


## Functions:

# main:

    This function first validates the command-line-arguments given to it by the user and then checks of the user has requested
    the help menu. Then, it uses the download function to download the video or playlist. If the download could not be done
    the program exits and informs the user of the failed download.


# validation:

    This function validates the command-line-arguments given to the program by the user. It does this by first checking if the
    user has entered the correct commands for displaying the help menu. If not then it checks if the first command-line-argument
    is a valid input and then uses a regex to check if the second command-line argument is a valid YouTube URL. Lastly, the number
    of the command-line arguments is checked. If everything passes, the function returns the value of True. The default return value
    is None


# download:

    This function takes as input two values, the type of download and the URL of the video or playlist to download.
    If the type is video then it uses the pytube library to get the first audio only stream of the requested video
    and downloads it. After the download is finished, it uses the os library to rename the file extention to MP3.

    Downloading a playlist does the same thing except it just gets the videos in a playlist and then, using a for 
    loop, downloads and changes their file extentions one by one. If any download fails. It gives the user an error 
    and moves to the next video to download.


# help:

    Displays the help menu.