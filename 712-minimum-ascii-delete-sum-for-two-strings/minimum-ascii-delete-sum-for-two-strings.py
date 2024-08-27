class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        d={}
        def lcs(s1,s2,i,j):
            
            if i<0:
                cur=0
                while(j>=0):
                    cur+=ord(s2[j])
                    j-=1
                
                return cur
            if j<0:
                cur=0
                while(i>=0):
                    cur+=ord(s1[i])
                    i-=1
                
                return cur
             
            if (i,j) in d:
                return d[(i,j)]
            
            ans=0
            
            if s1[i]!=s2[j]:
                
                d[(i,j)]=min(ord(s2[j])+lcs(s1,s2,i,j-1),ord(s1[i])+lcs(s1,s2,i-1,j),ord(s1[i])+ord(s2[j])+lcs(s1,s2,i-1,j-1))
            else:
                
                d[(i,j)]=lcs(s1,s2,i-1,j-1)
            
            return d[(i,j)]
            
           
            
                
        return lcs(s1,s2,len(s1)-1,len(s2)-1)
    