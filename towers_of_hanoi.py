# ### Towers of Hanoi

# In[ ]:


def tower(n, fr, to):
    """
    Input: d, number of discs; fr, from tower number; to, to tower number
    Returns: Sequence of instructions for moving each discs
    Declarative Statement:
    """
    tmp = 6 - fr - to
    if n == 1:
        print(f"Move disk from {fr} to {to}")
        return
    else:
        tower(n-1, fr, tmp)
        print(f"Move disk from {fr} to {to}")
        tower(n-1, tmp, to)
tower(3, 1, 2)