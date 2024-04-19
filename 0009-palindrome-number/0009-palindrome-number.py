class Solution(object):
    def isPalindrome(self,x):
        s = str(x)
        s2 = ""
        for i in range(len(s)-1,-1,-1) :
            s2 += s[i]
        return s == s2
        