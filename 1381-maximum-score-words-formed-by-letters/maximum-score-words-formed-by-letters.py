class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        W=len(words)
        freq=[0]*26
        
        for c in letters:
            freq[ord(c)-97]+=1
        
        
        def sub_score(sub,score,freq):
            total_sum=0
            
            for c in range(26):
                total_sum+=sub[c]*score[c]
                
                if sub[c]>freq[c]:
                    return 0
            
            return total_sum
        
        
        max_score=0
        
        for mask in range(1<<W):
            subset_letters=[0 for i in range(26)]
            
            for i in range(W):
                if (mask&(1<<i))>0:
                    l=len(words[i])
                    
                    for j in range(l):
                        subset_letters[ord(words[i][j])-97]+=1
            
            max_score=max(max_score,sub_score(subset_letters,score,freq))
        
        return max_score
            
                        
        
        