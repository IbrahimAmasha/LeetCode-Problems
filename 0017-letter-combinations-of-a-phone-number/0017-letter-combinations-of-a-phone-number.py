class Solution(object):
    def letterCombinations(self,digits):
                list1 = ["abc","def", "ghi" , "jkl","mno","pqrs","tuv","wxyz" ]
                list2 = []
                if len(digits) == 1  :
                    num = int(digits)
                    return list(list1[num-2])
                elif len(digits) == 0 :
                        return ""

                elif len(digits) == 2 or len(digits) == 3 :
                    for i in range(len(digits)) :
                        num = int(digits[i])
                        list2.append(list1[num-2])
                    list1 = []
                    first = list2[0]
                    n = 0
                    for i in range(len(first)) :
                        # n = 0
                        word = first[i]

                        for k in range(len(list2[1])) :
                            word += list2[1][k]
                            if len(digits) == 2 : list1.append(word)
                            jj = word
                            if len(digits) > 2 :
                                for d in range(len(list2[2])) :
                                    word += list2[2][d]
                                    list1.append(word)
                                    word = jj
                                word = first[i]
                            word = first[i]
                else :
                    for i in range(len(digits)) :
                        num = int(digits[i])
                        list2.append(list1[num-2])
                    list1 = []
                    first = list2[0]
                    n = 0
                    for i in range(len(first)) :
                        word = first[i]

                        for k in range(len(list2[1])) :
                            word += list2[1][k]
                            jj = word
                            for d in range(len(list2[2])) :
                                    word += list2[2][d]
                                    gg = word
                                    # word = jj
                                # word = first[i]
                                    for f in range(len(list2[3])) :
                                            word += list2[3][f]
                                            list1.append(word)
                                            word = gg
                                    word = jj
                            word = first[i]
                return list1