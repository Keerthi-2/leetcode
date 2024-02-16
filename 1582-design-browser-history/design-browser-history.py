class Node:
    def __init__(self,s:str,prev=None,next=None):
        self.val=s
        self.prev=prev
        self.next=next

class BrowserHistory:
    def __init__(self, homepage: str):
        
        self.cur=Node(homepage,None,None)

    def visit(self, url: str) -> None:
        new_node=Node(url,None,None)
        new_node.prev=self.cur
        self.cur.next=new_node
        self.cur=new_node
        
    
    def back(self, steps: int) -> str:
        while(steps>0 and self.cur.prev!=None):
            self.cur=self.cur.prev
            steps-=1
        return self.cur.val

       

    def forward(self, steps: int) -> str:
        while(steps>0 and self.cur.next!=None):
            self.cur=self.cur.next
            steps-=1
        return self.cur.val
        
        
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)