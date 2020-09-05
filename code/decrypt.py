# define a function that finds the truth by shifting the letter by the specified amount
def lassoLetter( letter, shiftAmount ):
    # invoke the ord function to translate the letter to its ASCII code 
    # and save it to the variable called letterCode
    letterCode = ord(letter.lower())
    
    # the ASCII number representation of lowercase a
    aAscii = ord('a')

    # the number of letters in the alphabet
    alphabetSize = 26

    # the formula to calculate the ASCII number for the decoded letter
    # taking into account looping around the alphabet
    trueLetterCode = aAscii + (((letterCode - aAscii) + shiftAmount) % alphabetSize)

    # converting the ASCII number to the character/letter
    decodedLetter = chr(trueLetterCode)

    # sending the decoded letter back
    return decodedLetter

# define a function that finds the truth by shifting the letters in an entire word by 
# the specified amount to discover the new word
def lassoWord( word, shiftAmount ):

    # this variable will be updated each time another letter is decoded
    decodedWord = ""

    # this for loop iterates through each letter in the word parameter
    for letter in word:
        # the lassoLetter() function is invoked with each letter and the shit amount
        # the result (decoded letter) is stored in a variable called decodedLetter
        decodedLetter = lassoLetter(letter, shiftAmount)

        # the decodedLetter is added to the end of the decodedWord
        decodedWord = decodedWord + decodedLetter

    # The decodedWord is sent back to the line of code that invoked this function
    return decodedWord

print( "Shifting WHY by 13 gives: \n" + lassoWord( "WHY", 13 ) )
print( "Shifting oskza by 13 gives: \n" + lassoWord( "oskza", -18 ) )
print( "Shifting ohupo by 13 gives: \n" + lassoWord( "ohupo", -1 ) )
print( "Shifting ED by 13 gives: \n" + lassoWord( "ED", 25 ) )