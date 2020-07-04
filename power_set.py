#!/usr/bin/env python
# coding: utf-8

# # Power set using recursion

# In[ ]:


def genSubset(lst):
    if len(lst) == 0:
        return [[]]
    else:
        subset_WO_last = genSubset(lst[:-1])
        last = [lst[-1]]
        subset_W_last = [x + last for x in subset_WO_last]
        #print(f"last: {last}")
        #print(f"subset_W_last: {subset_W_last}")
        #print(f"subset_WO_last: {subset_WO_last}")
        #print(f"subset_WO_last + subset_W_last: {subset_WO_last + subset_W_last}")
    return subset_WO_last + subset_W_last
lst = ['a','b']
print(genSubset(lst))


# # Memoization for reducing the complexity

# In[ ]:


def genSubset1(lst):
    memo = {}
    if len(lst) == 0:
        return [[]]
    else:
        if 
        


# # Power set using iteration

# In[ ]:


def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo

foo = powerSet(['a','b','c'])
foo.__next__()


# Generator that returns every arrangement of items such that each is in one or none of two different bags. Each combination should be given as a tuple of two lists, the first being the items in bag1, and the second being the items in bag2.

# In[ ]:


def trinary(n):
    lst = []
    for num in range(n):
        res = ''
        while num != 0:
            res += str(num%3)
            num //= 3
        lst.append(res[::-1])
    z = len(lst[-1])
    lst = [n.zfill(z) for n in lst]
    return(lst)  

def yieldAllCombos(items):
    N = len(items)
    num_lst = trinary(3**N)
    for num in num_lst:
        bag1, bag2 = [], []
        for i in range(len(num)):
            if num[-i-1] == '1':
                bag1.append(items[i])
            if num[-i-1] == '2':
                bag2.append(items[i])
        yield (bag1, bag2)      
          
sample = ['a', 'b', 'c']
foo = yieldAllCombos(sample)


# In[ ]:


for i in range(3**len(sample)):
    print(foo.__next__())


# # Concise Code

# In[ ]:


def yieldAllCombos(items):
    N = len(items)
    for i in range(3**N):
        bag1, bag2 = [], []
        for j in range(N):
            x = (i//3**j)%3 # Bit by bit base conversion
            if x == 1:
                bag1.append(items[j])
            if x == 2:
                bag2.append(items[j])
        yield (bag1,bag2)
sample = [1, 2, 3]
foo = yieldAllCombos(sample)                


# In[ ]:


for i in range(3**len(sample)):
    print(foo.__next__())

