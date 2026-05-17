class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp1 = {}
        temp2 = {}
        for i in s:
            if i in temp1:
                temp1[i] = temp1[i] + 1
                continue
            temp1[i] = 0
        for i in t:
            if i in temp2:
                temp2[i] = temp2[i] + 1
                continue
            temp2[i] = 0
        return temp1 == temp2
        