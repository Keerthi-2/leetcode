class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        def generate(curr):
            if len(curr)==len(nums):
                if curr not in nums:
                    return curr
                
                return ""
            
            zero=generate(curr+"0")
            if zero:
                return zero
            return generate(curr+"1")

        nums=set(nums)

        return generate("")