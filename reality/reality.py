from plyer import notification
import time
import sys

def main():
    if len(sys.argv) == 3:
    
        validate(sys.argv[1] , sys.argv[2])
        time = get_time(sys.argv[1] , sys.argv[2])
        generate_notif(time)
    
    elif len(sys.argv) == 2:
        sys.exit('Too few command-ine arguments.')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments.')
    else:
        generate_notif()


def validate(digit , suffix):
    valid_suffixes = [
       
        's',
        'm',
        'h',
        'sec',
        'secs',
        'min',
        'mins',
        'hr',
        'hrs',
        'seconds',
        'second',
        'minute',
        'minutes',
        'hour', 
        'hours'
    ]

    try:
        if (int(digit) <= 0):
            sys.exit('Must input a positive integer.')
    except:
        sys.exit('First argument must be a positive integer.')

    if suffix not in valid_suffixes:
        sys.exit('Not a valid suffix.')


def get_time(digit , suffix):
    digit = int(digit)
    if suffix.startswith('s'):
        time = digit
    elif suffix.startswith('m'):
        time = digit * 60
    else:
        time = digit * 3600

    return time


def generate_notif(wait=900):
    while True:
        time.sleep(int(wait))

        notification.notify(
            title = 'Reality Check',
            message = 'This is your reminder to do a reality check!',
            timeout = 10
        )


if __name__ == '__main__':
    main()