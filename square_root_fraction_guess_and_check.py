# ## Approximate square root of a fractional number

# In[ ]:


# For a fractional number the square root lies between 1 and the number
# and not 0 and the number

num = float(input("Enter a decimal number between 0 and 1: "))
epsilon = 1e-3
L = num
R = 1
M = (L + R) / 2.0
error = abs(M ** 2 - num)
iter_count = 0
print(f"L = {L}, R = {R}, error = {error}")

while error > epsilon:
    if M ** 2 > num:
        R = M
    else:
        L = M
    M = (L + R) / 2.0
    error = abs(M ** 2 - num)
    iter_count += 1
    print(f"L = {L}, R = {R}, error = {error}")

print(f"The square root of {num} is close to {M}")