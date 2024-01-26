### Description

Okay, this is a pretty simple program that just takes some text as input and then
converts it to morse code or really any other code you want if you specify a CSV file 
with each character and its code. But if no file is specified, it uses "morse.csv".
If any character is not in the file, a "?" will be used insetad of it.
* The letters in the CSV file must be lowercase * 


## CSV Headers

The headers for the CSV are: "letter,code"


### Functions

## main

This function first gets the key (Mapping of every letter to its code) using
the "get_key" function. IF the function returns None, main prints an error
message and returns. But if the return value for "get_key" is not None then
the user is prompted for the text they want to convert. The leading and 
trailing whitespace is removed and the text is converted to lowercase.
Finally, the legend and the converted text is printed.


## get_key

This function takes as an argument a csv file with each letter and its 
corresponding code and returns a dictionary with the key-value pairs being
the letter and its code. e.g {'a' : ".-"}. However if the file is not 
found, or the file is not a CSV, it returns None.

As for how it functions, if no file is specified, it uses the "morse.csv"
file. If the user did specify a file but it did not end in ".csv", the 
function returns None.

If everything goes smoothly, it opens the file and uses DictReader from the 
csv library to read it. It then goes through each row and adds new key-value
pairs to the dictionary called "key". The key is a letter and the value is 
its code. e.g {'a' : ".-"}. Finally, it returns the key.



## convert

This is the function that makes this entire thing work and it is quite 
simple. It takes as argument a "key", a dictionary with the keys being 
letters and their values being their codes and returns the encoded letters,
and the string that needs to be encoded

It does this by first initializing an empty string called "code". Then, for
every character in the given string, it looks up the code for the 
character and adds it to the "code" string. But if a character is not
in the key, It adds a "?" instead of it. Moreover "  /  " is adder after
each letter to act as a spererator.  

