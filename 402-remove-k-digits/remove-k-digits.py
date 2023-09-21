class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        # 14328679  #  18679  14329s
        s=[]
        if len(num)==k:
            return "0"
        for i in range(len(num)):
            #s.append(num[i])
            while(len(s)>0 and s[-1]>num[i]):
                s.pop()
                k-=1
                print(s)
                if k==0:
                    
                   
                    res="".join(s)+"".join(num[i:])
                    
                    temp=res
                    count=0
                    while(len(res)>0 and res[0]=='0'):
                        res=res[1:]
                        count+=1
                    if count==len(temp):
                        return "0"
                    return res
            s.append(num[i])
        #print(s)
        if k>0:
            s=s[:len(s)-k]
        temp=s
        count=0
        while(len(s)>0 and s[0]=='0'):
            s=s[1:]
            count+=1
        if count==len(temp):
            return "0"

        
        return "".join(s)
