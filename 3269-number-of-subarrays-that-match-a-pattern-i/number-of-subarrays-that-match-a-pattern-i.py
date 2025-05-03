class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:

        def build_lps(s):
            n=len(s)
            lps=[0]*n
            i=1
            prev_ind=0
            while(i<n):
                if s[i]==s[prev_ind]:
                    lps[i]=prev_ind+1
                    prev_ind+=1
                    i+=1
                else:
                    if(prev_ind!=0):
                        prev_ind=lps[prev_ind-1]
                    else:
                        i+=1
            return lps

        def pattern_match(text,pat):
            lps=build_lps(pat)
            i=1
            j=0
            m=len(text)
            n=len(pat)
            ans=0
            while(i<m):
                if text[i]==pat[j]:
                    i+=1
                    j+=1
                    if j==n:
                        ans+=1
                        j=lps[j-1]
                else:
                    if j!=0:
                        j=lps[j-1]
                    else:
                        i+=1
            return ans
        
        nums_pattern=[0]*len(nums)
        for i in range(1,len(nums)):
            
            if nums[i]>nums[i-1]:
                nums_pattern[i]=1
            elif nums[i]==nums[i-1]:
                nums_pattern[i]=0
            else:
                nums_pattern[i]=-1
        print("nums after chnage is :",nums_pattern)
        return pattern_match(nums_pattern,pattern)
        
        