# ## Selection Sort

# In[19]:


def selection_sorted(L):
    for i in range(len(L)):
        min_val = L[i]
        min_index = i
        for j in range(len(L) - 1 - i):
            index = i + j + 1
            if L[index] < min_val:
                min_val = L[index]
                min_index = index
        if L[i] != min_val:
            (L[i], L[min_index]) = (L[min_index], L[i])
        print(L)

Lst = [4, 9, 5, 3, 1, 2, 0, 4]
selection_sorted(Lst)
Lst
# Note the pattern: The numbers are sorted from the first index to the last index
