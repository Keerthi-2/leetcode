class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        res=0
        char_dict=[0]*26
        for c in chars:
            char_dict[ord(c)-97]+=1

        for word in words:
            word_count=[0]*26

            for i in word:
                word_count[ord(i)-97]+=1
            
            good=True

            for i in range(26):
                if char_dict[i]<word_count[i]:
                    good=False
                    break

            if good:
                res+=len(word)
        
        return res