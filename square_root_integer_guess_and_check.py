# ## Square root of any positive number using approximations

# In[ ]:


square = int(input("Enter a postive number: "))
guess = 0
epsilon = 1e-5
increment = 1e-2
iter_count = 0

while abs(square - guess**2) >= epsilon and guess < square:
    guess += increment
    iter_count += 1

print(f"Iteration Count: {iter_count}")
if guess > square:
    print(f"Failed to find the square root")
else:
    print(f"The square root of {square} is close to {guess}")