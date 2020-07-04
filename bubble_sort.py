# ## Bubble Sort

# In[17]:


def bubble_sorted(L):
    while True:
        flag = True  # Assuming input list to be sorted
        for i in range(len(L) - 1):
            if L[i] > L[i + 1]:
                flag = False  # List is not sorted
                (L[i + 1], L[i]) = (L[i], L[i + 1])  # swap operation
        print(L)
        if flag:
            break


Lst = [4, 9, 5, 3, 1, 2, 0, 4]
Lst = bubble_sorted(Lst)
Lst
# Note the pattern: The numbers are sorted from the last index to the first index

