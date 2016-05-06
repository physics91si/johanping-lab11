import string
alphabet = string.ascii_lowercase


#Returns a list of the first 10 letters of the alphabet
[letter for letter in alphabet[:10]]

#Returns a list of the first 10 letters of the alphabet except the sixth one.
[letter for letter in alphabet[:5]] + [letter for letter in alphabet[6:10]]

#Returns a list of the first 10 letters of the alphabet except the sixth one, each repeated
#each 1 , 2, and 3 times:

first = [letter + "," + letter*2 + "," + letter*3 for letter in alphabet[:5]] 
last = [letter + "," + letter*2 + "," + letter*3 for letter in alphabet[6:10]]
print(first+last)
    
#Returns a list of the first 10 letters of the alphabet except the sixth one, each repeated
#each 1 , 2, and 3 times in a grid:
first = [[letter + "," + letter*2 + "," + letter*3] for letter in alphabet[:5]] 
last = [[letter + "," + letter*2 + "," + letter*3] for letter in alphabet[6:10]]
print(first+last)


#Returns a list like the above, but if the number matches the index of the character mod 3 (e.g. 'c'	
#and	3, instead print a single capitalized version of that character:

[str[0].upper() if (sublist.index(str)== alphabet.index(str[0])%3) else str for sublist in list for str in sublist]
