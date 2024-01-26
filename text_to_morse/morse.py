from csv import DictReader

LEGEND = '\n"?" = Unknown letter\n"/" = Letter seperator\n'


def main():
    # Get the key which has morse or any other code
    key = get_key(input("File with code: "))
    
    # If the file with key does not exist or is not a csv
    if not key:
        print("The file specified does not exist or is not a csv!")
        return 1
    
    # Get the text, remove excess whitespace and convert to lowercase
    text = ((input("Text: ")).strip()).lower()

    # Print the legend and the converted text
    print(LEGEND)
    print(convert(text, key))

    return 0 


def get_key(file):
    # if no file specified, use the defaut file
    if not file:
        file = "morse.csv"

    # Make sure file is a csv
    if file.endswith(".csv") == False:
        return None

    try:
        # Open the file and read
        with open(file, 'r') as csvfile:
            reader = DictReader(csvfile)

            # Initialize a dictionary
            key = {}

            for row in reader:
                # The key of the dictionary is a letter and the value is the code
                # e.g {"a" : ".-"}
                key[(row["letter"])] = row["code"]

            return key
   
    except FileNotFoundError:
        return None


def convert(text, key):
    # Initialize empty string
    code = ""

    for letter in text:
        try:
            # Try to use the key to replace the letter 
            # and add it to the morse string
            # and add a seperator so people dont lose their minds tryina decode it...
            code += (key[letter] + ' / ')
        
        except KeyError:
            # If the letter is not in key, add a "?" instead
            code += '?  /  '

    return code


if __name__ == "__main__":
    main()