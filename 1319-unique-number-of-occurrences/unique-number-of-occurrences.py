from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d=Counter(arr)

        s=set()
        for i in d.values():
            if i not in s:
                s.add(i)
            else:
                return False
        
        return True
        