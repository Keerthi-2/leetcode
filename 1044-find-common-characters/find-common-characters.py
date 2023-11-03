class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        d1=[]
        for i in words:
            cur=i
            d={}
            for j in cur:
                if j in d:
                    d[j]+=1
                else:
                    d[j]=1
            d1.append(d)
        print(d1) 
        first=words[0]
        res=[]
        for i,val in  d1[0].items():
            key=i
            mn=val
            flag=1
            for j in range(1,len(d1)):
               # print(d1[j])
                if key in d1[j]:
                    
                    mn=min(mn,d1[j][key])
                else:
                    flag=0
                    mn=10**6
                    break
          #  print(key,mn)
            if flag==0:
                continue
            else:
                res+=[key]*mn
        return res
                


        