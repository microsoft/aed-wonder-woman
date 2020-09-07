# Decoding Word with a Ceasar Cipher

Now that you know how to decode one letter given a shift amount, you can decode entire words and phrases!

To do this decipher a word, you need to invoke the `lassoLetter()` function for each letter in the word, and then put all of the decoded letters together into a decoded word. 

This time you will write a function called `lassoWord()` that has two parameters; `word` and `shiftAmount`. 

```python
def lassoWord( word, shiftAmount ):
```

## Words are Collections of Letters

One way to think of words is that they are really just collections of letters! For example, you could think of the word "Hello" as:

'H' - 'e' - 'l' - 'l' - 'o'

While a variable can be a name for one piece of data (i.e. one word, one letter, one forumla, one function), Python also has ways of representing collections of data. One way is with a "list". 

A list is exactly what it sounds like. So, for example, you could imagine a word is a list of letters. 

Even better? Python has a way to loop through each item in a list one at a time! 

## List Iteration with a For Loop

Since you want to invoke the `lassoLetter()` function on each letter, you will need to loop through each letter in the word you're trying to decode. 

The syntax for a `for loop` is this:
```python
for item in list:
    do something
```

Since the word passed in as a parameter can be considered a list of letters, you can write:

```python
def lassoWord( word, shiftAmount ):

    for letter in word:
```

And with this, you now will be able to do something to each letter (e.g. invoke `lassoLetter()`!)

## Invoke the `lassoLetter()` Function

Invoking the l`assoLetter()` function on each letter in the word is fairly straightforward:

```python
def lassoWord( word, shiftAmount ):

    for letter in word:
        lassoLetter( letter, shiftAmount )
```

Do you recall when you wrote the `lassoLetter()` function the last line of code in that function was:

```python
# sending the decoded letter back
return decodedLetter
```

This is called a `return statement` and what it does is send the value back to the line that invoked the function. To capture that return value, you just have to use a variable!

```python
def lassoWord( word, shiftAmount ):

    for letter in word:
        decodedLetter = lassoLetter(letter, shiftAmount)
```

Now you are invoking a function your wrote (`lassoLetter()`) from a new function you're writing (`lassoWord()`).

## String Letter Together

With the code you just wrote, you will have one value in the decodedLetter variable, and then when the loop runs again, the variable will get updated. 

You can trace the code to see how that would work:  
`word` = "hello"  
`shiftAmount` = 1

| Loop Iteration | `letter` | `decodedLetter` |
|----------------|--------|---------------|
| 1 | 'h' | 'i' |
| 2 | 'e' | 'f' |
| 3 | 'l' | 'm' |
| 4 | 'l' | 'm' |
| 5 | 'o' | 'p' |

So what you're left with is a variable `decodedLetter` with just the letter 'p'. But what you wanted was a variable `decodedWord` to have the value "ifmmp". Recall from the Python basics recap earlier in this module you can use `+` between two words or letters to combine them together!

```python
def lassoWord( word, shiftAmount ):

    decodedWord = ""
    
    for letter in word:
        decodedLetter = lassoLetter(letter, shiftAmount)
        decodedWord = decodedWord + decodedLetter

    return decodedWord
```

With this code, you're left with the entire word stored in the variables `decodedWord`, which you can send back to the place where this function was invoked. You can trace the code like before:

| Loop Iteration | `letter` | `decodedLetter` | `decodedWord` |
|----------------|----------|-----------------|--------------|
| 1 | 'h' | 'i' | "i" |
| 2 | 'e' | 'f' | "if" |
| 3 | 'l' | 'm' | "ifm" |
| 4 | 'l' | 'm' | "ifmm" |
| 5 | 'o' | 'p' | "ifmmp" |

### Comment your Code

Don't forget to add comments so that you know exactly what is happening, even if you come back to this years later, without having to decipher the code (pun intended).

```python
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
```

**NOTE**: Make sure you have your tabbing correct!


## Test your Functions

Press the Play Button, and … nothing should happen … You've written your two functions, and `lassoWord()` does invoke `lassoLetter()`, but nothing invokes the `lassoWord()` function! 

Test your new code by invoking the `lassoWord()` function with "terra" as the value for the `word` paratmeter and 13 as the parameter for the `shiftAmount` variable. 

```python
# try decoding the word "terra"
print( "Shifting terra by 13 gives: \n" + lassoWord( "terra", 13 ) )
```

Now, when you press the Play button, You should see the word "green" printed in the console:

![Testing lasso function calls]()

# Checkin: Entire decrypt.py file

Now that you have your two functions have been written, your entire decrypt.py file should look like this:

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

# try decoding the word "terra"
print( "Shifting terra by 13 gives: \n" + lassoWord( "terra", 13 ) )
```

And now...You're ready to decode the secret message!

WONDER WOMAN 1984 TM & © DC and WBEI. RATED PG-13