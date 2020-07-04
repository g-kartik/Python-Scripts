# ## Cube root of any number using approximations

# In[ ]:


num = int(input("Enter any number: "))
cube = abs(num)
guess = 0
epsilon = 1e-3
increment = 1e-5
iter_count = 0

while abs(guess**3 - cube) >= epsilon and guess < cube:
    guess += increment
    iter_count += 1

print(f"Iteration count: {iter_count}")

if guess > cube:
    print("Failed to find the cube root")
else:
    if num < 0:
        print(f"The cube root of {cube} is close to -{guess}")
    else:
        print(f"The cube root of {cube} is close to {guess}")