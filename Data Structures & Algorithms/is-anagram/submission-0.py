class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        store1 = {}
        store2 = {}

        for i in s:

            if i in store1:
                store1[i] += 1
            else:
                store1[i] = 1
        
        for i in t:

            if i in store2:
                store2[i] += 1
            else:
                store2[i] = 1
        
        if store1 == store2:
            return True
        else:
            return False