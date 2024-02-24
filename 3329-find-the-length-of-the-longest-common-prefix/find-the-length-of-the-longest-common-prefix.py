class TrieNode:
    
    def __init__(self):
        self.node=[0]*10
        self.flag=False
    
    def containskey(self,ch):
        
        if self.node[ord(ch)-48]!=0:
            return True
        return False
    
    def put(self,ch,reference_node):
        self.node[ord(ch)-48]=reference_node
    def get(self,ch):
        return self.node[ord(ch)-48]
    def setend(self):
        self.flag=True
    def isend(self):
        return self.flag


class Solution:
    def __init__(self):
        self.root=TrieNode()
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        ans=0
        
        
        for cur in arr1:
            s=str(cur)
            node=self.root
            for i in range(len(s)):
                if((node.containskey(s[i]))==False):
                    node.put(s[i],TrieNode())
                node=node.get(s[i])
            node.setend()
        
        
        for cur in arr2:
            s2=str(cur)
            node=self.root
            steps=0
            for i in range(len(s2)):
                
                if node.containskey(s2[i])==False:
                    break
                else:
                    node=node.get(s2[i])
                steps+=1
            print(cur,i,node.isend())
            
            ans=max(ans,steps)
            
        
        return ans
            
                
            
        