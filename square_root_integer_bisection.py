# ## Square root of an integer using bisection method

# In[ ]:

# ## Bisection Search Convergence
# - Search space
#     - first guess: N/2
#     - second guess: N/4
#     - gth guess: N/2^g
# - Guess converges on the order of log base 2 of N steps
# - Bisection search works when value of the function varies monotonically with input
#
# ### Observations
# - Bisection search radically reduces computation time
# - being smart about generating guesses is important
# - Should work well on problems with 'ordering' property
# - value of function being solved varies monotonically with input value
# - Here function is g**2, which grows as g grows

num = int(input("Enter a positive integer: "))
Li = 0
Ri = num
flag = False
iter_count = 0

while Ri - Li != 1:
    iter_count += 1
    Mi = (Li + Ri) // 2
    if Mi ** 2 == num:
        flag = True
        break
    elif Mi ** 2 > num:
        Ri = Mi
    else:
        Li = Mi

print(f"Iteration Count: {iter_count}")

if flag == True:
    print(f"The square root of {num} is close to {Mi}")
else:
    print(f"{num} has no perfect square root")
