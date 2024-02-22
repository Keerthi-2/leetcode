class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        i=0
        j=0
        st=[]
        n1=len(pushed)
        n2=len(popped)
        while(i<n1 and j<n2):
                 # pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
            while(i<n1 and (len(st)==0 or st[-1]!=popped[j])):
                st.append(pushed[i])
                i+=1
            
            while(j<n2 and len(st)>0 and st[-1]==popped[j]):
                st.pop()
                j+=1
        
        if len(st)==0:
            return True
        return False