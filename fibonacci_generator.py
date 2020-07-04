# ## Using Generators in Fibbonaci Sequence

# In[39]:


def fibb():
    fibb_1 = 0
    fibb_2 = 1
    while True:
        _next = fibb_1 + fibb_2
        yield _next
        fibb_1 = fibb_2
        fibb_2 = _next