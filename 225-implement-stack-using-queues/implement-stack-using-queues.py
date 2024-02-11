class MyStack:

    def __init__(self):
        self.q=[]

    def push(self, x: int) -> None:
        self.q.append(x)
        # for i in range(0,len(self.q)-1):
        #     temp=self.q.pop(i)
        #     self.q.append(temp)
        

    def pop(self) -> int:
       
        return self.q.pop()
        

    def top(self) -> int:
        return self.q[-1]
        

    def empty(self) -> bool:
        return len(self.q)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()