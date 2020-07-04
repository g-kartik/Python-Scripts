# ## Decimal to Binary Conversion

# In[ ]:


# Declarative Statements:
# Decimal Number for example, 312 = 3*10^2 + 1*10^1 + 2*10^0
# Similarly, a binary number, 11010 = 1*2^4 + 1*2^3 + 0*2^2 + 1*2^1 + 0*2^0

num = int(input("Enter an integer: "))
result = ''

if num < 0:
    num = abs(num)
    isNeg = True
else:
    isNeg = False

if num == 0:
    result = '0'

while num > 0:
    result += str(num % 2)
    num = num // 2

if isNeg:
    print(f"-{result[::-1]}")
else:
    print(f"{result[::-1]}")