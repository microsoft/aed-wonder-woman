# Decoding One Letter at a Time Part 2



## Calculating the Decoded Character: The right way 

With the mod operator in mind, you will need two new variables:
- `aAscii`: holds the ASCII value of 'a' by calling `ord('a')`
- `alphabetSize`: holds the number of letters in the alphabet, so 26!

Then, the formula for figuring out the `trueLetterCode` would be:
`aAscii` + (((`letterCode` - `aAscii`) + `shiftAmount`) % `alphabetSize`)

You can review this formula with a couple examples:

### Example 1: 'a' and 2

Start with:
- `letter` = 'a'
- `shiftAmount` = 2

| Variable | Formula | Value | 
|----------|---------|-------|
| letter | none | 'a' |
| shiftAmount | none | 2 |
| letterCode | `ord('a')` | 97 |
| aAscii | `ord('a')` | 97 |
| alphabetSize | none | 26 |
| trueLetterCode | 97 + (((97 - 97) + 2) % 26)  | 2 (see below) |
| decodedLetter | chr(99) | `c` |

You can review the formula for `trueLetterCode` just like you would any other math formula (remember PEMDAS):
`aAscii` + (((`letterCode` - `aAscii`) + `shiftAmount`) % `alphabetSize`)
97 + (((97 - 97) + 2) % 26) 
97 + ((0 + 2) % 26)
97 + (2 % 26)
97 + 2
99

### Example 2: 'W' and 13

Start with:
- `letter` = 'W'
- `shiftAmount` = 13

| Variable | Formula | Value | 
|----------|---------|-------|
| letter | none | 'W' |
| shiftAmount | none | 13 |
| letterCode | `ord('w')` | 119 |
| aAscii | `ord('a')` | 97 |
| alphabetSize | none | 26 |
| trueLetterCode | 97 + (((119 - 97) + 13) % 26)  | 106 (see below) |
| decodedLetter | chr(106) | `j` |

You can review the formula for `trueLetterCode` just like you would any other math formula (remember PEMDAS):
`aAscii` + (((`letterCode` - `aAscii`) + `shiftAmount`) % `alphabetSize`)
97 + (((119 - 97) + 13) % 26)
97 + ((22 + 13) % 26)
97 + (35 % 26)
97 + 9
106

## Final Code

Now that you have your decoder formula, you can put it all together in your function (make sure you add comments so you can remember what is happening!):

```python
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
```

Now that you have the `lassoLetter()` function you can call this on each letter in the secret message!

WONDER WOMAN 1984 TM & © DC and WBEI. RATED PG-13