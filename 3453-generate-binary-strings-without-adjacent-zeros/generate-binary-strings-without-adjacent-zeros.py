class Solution:
    def validStrings(self, n: int) -> List[str]:
        res=[]
        def form(prev,cur):
            if len(cur)==n:
                if cur not in res:
                    res.append(cur)
                return
            char=''
            if prev=='0':
                char='1'
                form(char,cur+char)
            else:
                form('0',cur+'0')
                form('1',cur+'1')

        
        s=''
        form('0',s)
        form('1',s)

        print(res)
        return res