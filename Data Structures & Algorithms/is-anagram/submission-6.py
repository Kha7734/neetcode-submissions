class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t): return False 

        # countS, countT = {}, {}
        
        # for i in range(len(s)): 
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # return countS == countT

        # from collections import Counter
        # return Counter(s) == Counter(t)

        if len(s) != len(t): 
            return False 

        arrS = [0] * 26 
        arrT = [0] * 26 

        for i in range(len(s)): 
            arrS[ord(s[i]) - ord('a')] += 1 
            arrT[ord(t[i]) - ord('a')] += 1 
            
        return arrS == arrT
 