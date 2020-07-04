# ### Class Fractions

# #### Things learnt from this code
# - Calling methods inside class
# - GCF and LCM code
# - Some dunder methods

# In[81]:


class fract:
    def __init__(self, p, q):
        gcf = fract.gcf(p, q)
        self.p = p//gcf
        self.q = q//gcf
    
    def __str__(self):
        return(f"{self.p}/{self.q}")

    def __add__(self, other):
        sum_p = self.p * other.q + other.p * self.q
        sum_q = self.q * other.q
        gcf = fract.gcf(sum_p, sum_q)
        return(fract(sum_p//gcf, sum_q//gcf))
    
    def __sub__(self, other):
        diff_p = self.p * other.q - other.p * self.q
        diff_q = self.q * other.q
        gcf = fract.gcf(diff_p, diff_q)
        return(fract(diff_p//gcf, diff_q//gcf))
    
    def gcf(p, q):
        lst = list(range(1, min(p, q)+1)) 
        lst.reverse()
        for num in lst:
            if p%num == 0 and q%num == 0:
                return(num)
            
    def tofloat(self):
        return(self.p/self.q)


# In[86]:


x = fract(3, 12)
y = fract(2, 15)
print(x)
print(x+y)
print(x-y)
print(x.tofloat())