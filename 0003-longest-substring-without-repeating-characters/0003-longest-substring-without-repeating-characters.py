class Solution(object):
    def lengthOfLongestSubstring(self,s):
        word = "" 
        list = []
        for i in range(len(s)) :
                word = ""
                for k in range(i,len(s)) :
                        if s[k] not in word :
                                word += s[k] 
                        else :
                                break
                list.append(word)
        # j = list[0]
        jj = 0
        for i in range(len(list)) :
                if len(list[i]) > jj : jj = len(list[i])
        return jj