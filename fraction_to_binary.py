# ## Fractional number to binary number conversion

# In[ ]:


# In decimal number system, a fractional number say, 0.625 is evaluated as
# 0.625 = 6*10^-1 + 2*10^-2 + 5*10^-3
# Multiply the number by the highest power of 10 such that it becomes a whole number
# 0.623 * 10^3 = 625
# Get the decimal digits of 625
# Divide the number by the same power of 10 to get back the fractional number

# Similarly in binary
# Multiply the number by highest power of 2 such that it becomes a whole number
# Convert that whole number to binary
# Divide the binary number by same power of 2 or right shift the binary bits by the highest power
# to get the binary representation of fractional number

num = float(input('Enter a decimal number between 0 and 1: '))
result = ''
if num == 0:
    result = '0'

i = 0

while (num * 2 ** i) % 1 > 0:
    num *= 2
    i += 1

num = int(num * 2 ** i)

while num > 0:
    result += str(num % 2)
    num //= 2

result = result[::-1].zfill(2 ** i)

print(f".{result}")