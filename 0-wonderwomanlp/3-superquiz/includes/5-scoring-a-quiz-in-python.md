Now it’s time to really score the quiz. With five questions and different choices, we’ll use some variables to guide our response. We'll add and subtract points from each of the four characters depending on what you choose to answer. At the end we'll tally up all the points and tell you which character you are most like. Add the following commands to your file.
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
if weapon == "B":
    pass

# update scoring variables based on the job choice
if job == "A":
    diana_like = diana_like + 2
    barbara_like = barbara_like + 2
if job == "B":
    max_like = max_like + 2

# update scoring variables based on the value choice
if value == "A":
    diana_like = diana_like - 1
    max_like = max_like + 2
if value == "B":
    diana_like = diana_like + 1
    trevor_like = trevor_like + 1

# update scoring variables based on the decade choice
if decade == "A":
    trevor_like = trevor_like + 2
if decade == "B":
    pass

# update scoring variables based on the animal choice
if animal == "A":
    pass
if animal == "B":
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
 
<img width="960" alt="screenshot" src="https://user-images.githubusercontent.com/12758612/89692637-1e7cbb00-d8c1-11ea-85e6-c6bab0eac44c.png">

Check your code with the completed quiz code [**here**](https://github.com/microsoft/WW84-Python-Lessons/blob/master/quiz.py){:target="_blank"}.

### Credits
Special thanks to [Audrey St. John from Mount Holyoke College](https://www.mtholyoke.edu/people/audrey-stjohn){:target="_blank"} for this lesson, which was inspired by and adapted from the “active learning module” developed by Emily Craig and Sarah Robinson for the [MaGE](https://sites.google.com/a/mtholyoke.edu/mage/){:target="_blank"} inclusive peer mentoring program at Mount Holyoke College.