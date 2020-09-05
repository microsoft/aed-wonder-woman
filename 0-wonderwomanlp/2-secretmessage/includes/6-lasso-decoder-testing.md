# Use the Lasso Decoder to Decode the Secret Message

As a reminder, the secret message you're trying to decide is:

![Encoded Message]()

And what you know is:
1.	The word "WHY" needs to be shifted by 13,
2.	The word "oskza" needs to be shifted by -18,
3.	The word "ohupo" needs to be shifted by -1, and
4.	The word "ED" needs to be shifted by 25.

## Add Print Statements

Just like you did when you tested your `lassoWord()` function with the word "terra" shifted by 13, you can add additional `print()` statements to the bottom of your file to print all of the decoded words!

```python
print( "Shifting WHY by 13 gives: \n" + lassoWord( "WHY", 13 ) )
print( "Shifting oskza by 13 gives: \n" + lassoWord( "oskza", -18 ) )
print( "Shifting ohupo by 13 gives: \n" + lassoWord( "ohupo", -1 ) )
print( "Shifting ED by 13 gives: \n" + lassoWord( "ED", 25 ) )
```

Press the Play Button, and you should see the final clue to the true meeting place and time revealed.