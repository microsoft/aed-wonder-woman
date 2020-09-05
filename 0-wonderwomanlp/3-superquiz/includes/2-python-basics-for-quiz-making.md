# Title matches yml

## Basics

Before you dive into the full personality quiz, let’s walk you through the basics for commanding the Python. If you already know how to use variables, functions, and conditionals, you can skip to the next part.

### [Skip basics >](quiz.md)

## Comments
First, we can write comments to ourselves that the Python will ignore. On any line where we use the # symbol, the Python ignores everything after.

Try adding the following to your file:
```python
# this is a comment that won’t be interpreted as a command
```
Press the Play button, and you should see the same behavior as before.

<img width="960" alt="screenshot" src="https://user-images.githubusercontent.com/12758612/89687712-8decad80-d8b5-11ea-8ab4-9022de9b54cc.png">
 
## Variables
If you want the Python to remember something, you can command it to “write it down” using a variable. 

The following command tells the Python to remember the value 1984 using a variable named “year” with the special assignment = sign operator. Any time after this command, when the Python sees “year”, it will substitute the current value.
```python
# use a variable named year to “remember” the value 1984
year = 1984
```
Try it out by replacing the commands in your file with the following. The print command can, if you put an f before what you want printed, use curly braces {} to surround a variable name -- this will make the Python print out the value of the variable.
```python
# use a variable named year to “remember” the value 1984
year = 1984

# print a message to see what year it is
print( f"The year is {year}..." )
```
Press the Play Button, and you should see the year print out.

<img width="960" alt="screenshot" src="https://user-images.githubusercontent.com/12758612/89687848-c68c8700-d8b5-11ea-81a5-b1ab2d9044b8.png">

We can update the value of a variable using the same assignment (= sign) operator. The Python will figure out the right-hand side before storing it in the variable. Since “year” already has a value, this command will ask the Python to first substitute the current value of “year” (which is 1984), add 36 to it, then store that value in the variable “year”. This effectively overwrites the value that was written down originally. Try it out by replacing the commands in your file with the following.
```python
# use a variable named year to “remember” the value 1984
year = 1984
        
# print a message to see what year it is
print( f"The year is {year}..." )

year = year + 36

# print a message to see what year it is now
print( f"The year is now {year}..." )
```
Press the Play Button, and you should see the years print out.

<img width="960" alt="screenshot" src="https://user-images.githubusercontent.com/12758612/89687921-f2a80800-d8b5-11ea-9cb2-08a12f88f65d.png">
 
## Conditionals
The Python can perform commands depending on some condition. We’re used to conditionals in the real world: “If you’ve been lassoed, then you're compelled to tell the truth.” The keyword here is if, which is followed by a condition, where we check whether or not the lasso of truth is around you. When the condition is met, the subsequent command must be followed. The Python only expects a condition to either be met or not—it’s either true or false.


To get a little more comfortable, consider the following strategy for how to spend a day _(the following is not code, it's just plain text to explain a scenario)_:
```
if it’s raining cats and dogs
find a cat
if the cat is hangry
        find some milk
        give the milk to the cat
    else
        pet the cat until it purrs or scratches you
else
be happy that it’s not raining animals
    frolic outside
```

Now, how could this play out? It could be the case that:
- It’s raining cats and dogs.
- The cat you find is hangry (hungry + angry).

In this scenario, you can do three things:
- You find a cat.
- You find some milk.
- You give the milk to the cat.

What if instead:
- It’s not raining cats and dogs?

In this scenario, you can do two things:
- You are happy that it’s not raining animals.
- You frolic outside.

There are a few more possible scenarios, but let’s move on to how we can use conditionals to command the Python in our year example.

The Python expects a particular “syntax” (formulation of the commands). We won’t go into depth here; instead, just try out this example by adding the following to your file. (If you’re wondering what the == is doing, that is how we test if two numbers are equal; remember that a single = means assignment of a variable, so the Python would be confused).
```python
# if we're in 1984
if year == 1984:
    print( "I left you a message on your answering machine!" )
# if we're in 2020
if year == 2020:
    print( "I left you a voicemail!" )
```
Press the Play button, and you should see the state-of-the-art in messaging.

<img width="960" alt="screenshot" src="https://user-images.githubusercontent.com/12758612/89688061-3e5ab180-d8b6-11ea-9ff6-7cbdc5c2536e.png">

How would you change the year so that you get a message on your answering machine instead?

### Booleans (extra)
The Python puts a special meaning on the words “true” and “false,” and calls them boolean values. It turns out that booleans are studied in computer science (and philosophy) and there is an entire subject called boolean logic. You might be comfortable with arithmetic, where numbers are operated on to produce other numbers; 1 + 2 is 3. The operands are the numbers 1 and 2, and the operator is the addition operator.  In boolean logic, boolean values (True or False) are operated on to produce other boolean values. We might say, “if it is cold outside AND it is raining, grab a parka.” Then both conditions must be met (must be True) for us to grab a parka. Here the operands are whether or not it is cold outside and whether or not it is raining; the AND operator

---

Now that we have the handle on some of the basics, let’s move on to making the quiz.