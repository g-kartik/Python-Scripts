# ### Is Palindrome

# In[1]:


def isPalindrome(s):
    """
    Input: String, s
    Returns: True if s is a palindrome, else false
    Declarative Statement: s is a palindrome if s[0] == s[-1] and the remaining string is a
    palindrome.
    """

    def toChar(s):
        s = s.lower()
        ans = ""
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChar(s))


isPalindrome('eve')
isPalindrome('Able was I, ere I saw Elba')