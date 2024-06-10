class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res=heights[:]
        res.sort()
        ans=0

        for i in range(len(heights)):
            if heights[i]!=res[i]:
                ans+=1


        return ans