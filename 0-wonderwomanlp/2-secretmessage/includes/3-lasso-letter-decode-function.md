## Okay, time to get cracking

I think the message might be encrypted with something called a “Caesar cipher,” where all the letters are shifted in the alphabet by some amount. Similar to Wonder Woman’s golden lasso, I’ll need you to give the Python the power to find the true meaning of the words "WHY", “oskza”, “ohupo”, and "ED".

Let’s start by giving the power to shift a single letter. You might notice some other commands in here, but we don’t have time to cover them all right now. Replace the code in your file with the following: 
```python
# define a power (function) that finds the truth by shifting the letter by the specified amount
def lassoLetter( letter, shiftAmount ):
    # use the ord power to translate the letter to a special number called its ASCII code 
    # and associate it codename letterCode
    letterCode = ord(letter.lower())
    
    # shift the ASCII code to find the true letter's ASCII code
    # (my team says that ASCII codes are in order, starting with the code for the letter a)
    trueLetterCode = ord("a") + ((letterCode - ord("a"))+shiftAmount) % 26
   
    # now reveal the true letter by using the chr power to translate back from ASCII
    # "return" this as a result of invoking the power lassoLetter
    return chr(trueLetterCode)
```