# ## Approximate square root of any postive number using bisection method

# In[ ]:


num = float(input("Enter any positive number: "))
epsilon = 1e-3
L = 0
R = num
iter_count = 0
M = R/2.0
error = abs(M**2 - num)
print(f"L = {L}, R = {R}, M = {M}, error = {error}")

while error > epsilon:
    if M**2 > num:
        R = M
    else:
        L = M
    iter_count += 1
    M = (L + R)/2
    error = abs(M**2 - num)
    print(f"L = {L}, R = {R}, M = {M}, error = {error}")

print(f"Iteration Count: {iter_count}")
print(f"The square root of {num} is close to {M}")