from functools import reduce

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        storelist = []

        copylist = arr.copy()

        for i in range(len(arr)):

            if i+1 < len(arr):

                del copylist[0]

                maxvalue = reduce(lambda acc,num : acc if acc>num else num,copylist)

                storelist.insert(i,maxvalue)
            
            else:
                storelist.insert(i,-1)
        
        return storelist
