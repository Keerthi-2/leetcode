class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l=[]
        for i in tokens:
            if i=="+":
                x=l.pop()
                y=l.pop()
                l.append((x+y))
            elif i=='-':
                x=l.pop()
                y=l.pop()
                l.append((y-x))
            elif i=='*':
                x=l.pop()
                y=l.pop()
                l.append((x*y))
            elif i=='/':
                x=l.pop()
                y=l.pop()
                
                l.append((int(y/x)))
            else:
                i=int(i)
                l.append(i)
        return l[0]