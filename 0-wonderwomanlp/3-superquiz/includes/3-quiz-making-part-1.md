## Okay, now let’s make that personality quiz

We’ll be asking a streamlined version of this quiz. We’ll use just five questions and two options for each: 

1. Which weapon? (A) Lasso (B) No weapons 
1. What’s your dream job? (A) Curator at the Smithsonian (B) Running a business
1. What’s more important? (A) Money (B) Love
1. What’s your favorite decade? (A) 1910s (B) 1980s
1. What’s your favorite big cat? (A) Tiger (B) Cheetah

We'll use these questions to determine which of the following four you are most like:

- Wonder Woman
- Barbara Minerva
- Steve Trevor
- Max Lord

---

Hmm, somehow the Python needs to ask the candidate a question. We can command it to do so using the input command; this gives back (returns) the candidate’s answer, which we can store in a variable. Try replacing the commands in your file with the following. (If you’re wondering what the \n is doing, it tells the Python to put in a new line or hit the “return” key.)
```python
# ask the candidate a question
weapon = input( "Which weapon?\n(A) Lasso\n(B) No weapon, thank you\n" )

# print out which weapon they chose
print( f"You chose {weapon}.")
```

Press the Play button, and you should see the question print out, along with the options. Click in the TERMINAL area and try typing A then “enter” to see what happens.

<img width="960" alt="screenshot" src="https://user-images.githubusercontent.com/12758612/89688177-81b52000-d8b6-11ea-98b1-b84b9e5f305e.png">
 
Notice that the weapon variable simply stores whatever you typed. Try typing lion instead and see what happens…

<img width="282" alt="screenshot" src="https://user-images.githubusercontent.com/12758612/89688296-b45f1880-d8b6-11ea-9611-d155de306764.png">
 
For now, let’s assume the candidate understands that they should type the letter of their choice (and capitalize it correctly). Then we can use a conditional to have the Python execute commands depending on what they chose. Try adding the following commands to your file:
```python
# if they chose the lasso
if weapon == "A":
    print( "Nice choice!" )
```
Press the Play button and try entering A as your choice. Be sure to type in a capital A.

<img width="960" alt="screenshot" src="https://user-images.githubusercontent.com/12758612/89688477-1fa8ea80-d8b7-11ea-8db1-e2315b82357f.png">

What happens if you enter B instead? Can you add another print out for the choice B?