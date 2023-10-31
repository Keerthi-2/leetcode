class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        list=[0]*(len(pref))
        list[0]=pref[0]

        for i in range(len(pref)-1):
            list[i+1]=pref[i]^pref[i+1]
        return list