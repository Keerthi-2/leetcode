class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n=len(arr)
        for i in range(1,n-1):
            
            if arr[i-1]%2!=0 and arr[i]%2!=0 and (i+1<n and arr[i+1]%2!=0):
                return True
            
        False
                
            