import sys

def main():
    try:
        valid = validation(sys.argv[1] , sys.argv[2] , len(sys.argv))
        
        if valid != None:
            sys.exit(error_message(valid))
   
        common_words = common(sys.argv[1] , sys.argv[2])
        
    except IndexError:
        sys.exit(error_message(2))
    except FileNotFoundError:
        sys.exit(error_message(4))


    i = 1
    for key , val in common_words:
        print(f'{i}- {val} : {key} ')
        i += 1

    print('\n')
 

def common(file , n):
    counts = {}
    with open(file , 'r' , encoding='utf-8' , errors='ignore') as file:
        for line in file:
            words = line.split()
            for word in words:
                counts[word] = counts.get(word , 0) + 1 
    
    wordlist = []
    for key , value in counts.items():
        wordlist.append((value , key))
    
    wordlist = sorted(wordlist , reverse=True)
    
    return wordlist[:int(n)]


def validation(filename , n , length):
    if not (str(filename).endswith('.txt')):
        return 0
    if not (str(n).isnumeric()):
        return 1
    if length > 3:
        return 3
    
    return None


def error_message(n):
    error = {
        0 : 'File must end in ".txt"\n' ,
        1 : 'Second command-line argument must be a number\n' ,
        2 : 'Too few command-line arguments\n' ,
        3 : 'Too many command-line arguments\n' ,
        4 : 'File does not exist\n' ,
    }

    return error[n]


if __name__ == '__main__':
    main()