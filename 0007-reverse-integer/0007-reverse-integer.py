class Solution(object):
    def reverse(self,x):
        word = str(x)
        if word[0] == '-' :
            reversed = "-" + word[1:][::-1]
        else : reversed = word[::-1]
        jj = 0
        for i in range(len(reversed)) :
            if reversed[i] != "0" :
                jj = i
                break
        num = int(reversed[jj:])
        if num >= (2**31) -1 or num <= (-2 ** 31) : return 0
        else : return num