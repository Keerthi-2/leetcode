# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:
import random
class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        #APPROACH2
        #Since we may find secret word after 10 guesses,
        #1. Stop aiming to find secret word
        #2. Think of algorithm to make 10 calls fully to master.guess or until we find secret word, whichever comes first  
        #Match count between guess word and every candidate in wordslist
        def guessMatches(guessWord, candidate, count):
            matches = 0
            for g,c in zip(guessWord, candidate):
                if g == c:
                    matches += 1
            return count == matches

        matches = 0
        i = 0
        #Iterate until 10 guesses
        while i < 10 and matches != 6:
            word = words[random.randint(0, len(words)-1)]
            matches = master.guess(word)
            candidates = []
            #Eliminate candidates that won't match with guessed word (which have common chars with secret)
            for cand in words:
                if guessMatches(word, cand, matches):
                    candidates.append(cand)
            words = candidates
        # return word
    
        #APPROCH 1
        #BRUTEFORCE - Cannot pass all testcases with 10 guesses
        # for word in words:
        #     res = master.guess(word)