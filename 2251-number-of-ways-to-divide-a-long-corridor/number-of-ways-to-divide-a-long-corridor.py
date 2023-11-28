class Solution:
    def numberOfWays(self, corridor: str) -> int:

        ind=[]
        for i in range(0,len(corridor)):
            if corridor[i]=='S':
                ind.append(i)
            
        if len(ind)==0 or len(ind)%2==1:
            return 0
        

        current_pair_first=2
        previous_pair_last=1
        count=1
        while(current_pair_first<len(ind)):
            count*=(ind[current_pair_first]-ind[previous_pair_last])
            count=count%(10**9+7)

            current_pair_first+=2
            previous_pair_last+=2
        return count%(10**9+7)
