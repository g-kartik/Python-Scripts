#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random
num = random.randint(1, 100)
guess = []
flag = 0
guess_count = 0
while True:
    x = int(input("Enter your guess integer between 1 and 100\n"))
    if x in range(1, 101):
        guess.append(x)
        guess_count = 1
        if guess[0] == num:
            print("Hurray! You have guessed it correctly in %d guesses" %guess_count)
            flag = 1
            break
        if guess[0] in range(num-10,num+11):
            print("Warm")
        else:
            print("Cold")   
        break
    else:
        print("OUT OF BOUNDS")
        
if flag != 1:
    while True:
        x = int(input("Guess Again\n"))
        if x in range(1, 101):
            guess.append(x)
            guess_count += 1
            if guess[-1] == num:
                print("Hurray! You have guessed it correctly in %d guesses" %guess_count)
                break
            elif abs(num - guess[-1]) < abs(num - guess[-2]):
                print("Warmer")
            else:
                print("Colder")
        else:
            print("OUT OF BOUNDS")


# In[ ]:




