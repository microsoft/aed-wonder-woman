# Choosing a Wonder Woman Character Based on a Personality Quiz 

Now it’s time to really score the quiz and assign your user a character from Wonder Woman 1984! 

With five questions and different choices, you'll use some variables to guide the response. You'll add and subtract points from each of the four characters depending on what the user choose to answer. At the end you'll tally up all the points and tell the user which character they are most like. 

Add this code to the bottom of your file. Notice that this time you can use else-statments because in thse code you wrote in the last unit if the user chose something other than "A" or "B" you set each variable to "A". 

```python
# create some variables for scoring
diana_like = 0
trevor_like = 0
max_like = 0
barbara_like = 0

# update scoring variables based on the weapon choice
if weapon == "A":
    diana_like = diana_like + 1
    barbara_like = barbara_like - 1
else:
    pass

# update scoring variables based on the job choice
if job == "A":
    diana_like = diana_like + 2
    barbara_like = barbara_like + 2
else:
    max_like = max_like + 2

# update scoring variables based on the value choice
if value == "A":
    diana_like = diana_like - 1
    max_like = max_like + 2
else:
    diana_like = diana_like + 1
    trevor_like = trevor_like + 1

# update scoring variables based on the decade choice
if decade == "A":
    trevor_like = trevor_like + 2
else:
    pass

# update scoring variables based on the animal choice
if animal == "A":
    pass
else:
    barbara_like = barbara_like + 2

# print the results depending on the score
if diana_like >= 3:
    print( "You're most like Wonder Woman!" )
elif trevor_like >= 3:
    print( "You're most like Steve Trevor!" )
elif barbara_like >= 3:
    print( "You're most like Barbara Minerva!")
else:
    print( "You're most like Max Lord!")
```
Press the Play button and find out which WONDER WOMAN 1984 personality you’re most like!