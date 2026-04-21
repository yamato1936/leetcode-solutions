class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for i in s:
            count[i] = count.get(i,0) + 1
        for i in t:
            count[i] = count.get(i,0) - 1
        
        for v in count.values():
            if v != 0:
                return False
        return True




#Hashmap        
        