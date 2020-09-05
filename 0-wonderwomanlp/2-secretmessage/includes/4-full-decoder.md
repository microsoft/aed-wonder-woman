We’ll need to invoke it on every letter in a word, so let’s give the Python another power (and command it to use the lassoLetter power as part of this new one). Copy the following and put it after the lassoLetter power.

```python
# define a power (function) that finds the truth
# by shifting all the letters in a word by the specified amount
def lassoWord( word, shiftAmount ):
    # this codename (variable) will be updated to store the true phrase after shifting
    trueWord = ""
    
    # for each letter in the word
    for letter in word:
        # invoke the power (function) lassoLetter to reveal the true letter
        # and update the codename trueWord
        trueWord = trueWord + lassoLetter( letter, shiftAmount )

    # return the truth
    return trueWord
```
With these powers, your code should look like this:

<img width="960" alt="screenshot" src="https://user-images.githubusercontent.com/12758612/89686385-233a7280-d8b3-11ea-9172-1eb0cda90e80.png">

Press the Play Button, and … nothing should happen … We only endowed the Python with the power, but didn’t invoke it. We will test it by invoking the lassoWord power on the word terra—shifting by 13 should reveal the true word “green.”

```python
# try out the power on the phrase
print( "Shifting terra by 13 gives: \n" + lassoWord( "terra", 13 ) )
```
Press the Play Button, and you should see the truth revealed for "terra"!

<img width="960" alt="screenshot" src="https://user-images.githubusercontent.com/12758612/89686573-757b9380-d8b3-11ea-857d-6fc2ee84a210.png">