class Trie:
    def __init__(self):
        self.child={}
        self.count=0
        
class Solution:
    def __init__(self):
        self.root=Trie()
    
    
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        t=self.root
        a=ord('a')
        
        for word in words:
            node=self.root
            for ch in word:
                cur=ch
                
                if cur not in node.child:
                    node.child[cur]=Trie()
                node=node.child[cur]
                
                node.count+=1
         


        ans=[]
        for x in words:
            node,res=self.root,0
            for ch in x:
                if ch in node.child:
                    node=node.child[ch]
                    #print(x,ch,node.child,node.count)
                    res+=node.count
                    
                
                    
            ans.append(res)
        
        return ans