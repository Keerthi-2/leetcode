class Solution:
    from collections import defaultdict, deque
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(deque)

        for word in words:
            waiting[word[0]].append((word, 0))  # store word and current index

        count = 0

        for c in s:
            old_bucket = waiting[c]
            waiting[c] = deque()

            while old_bucket:
                word, index = old_bucket.popleft()
                index += 1
                if index == len(word):
                    count += 1
                else:
                    waiting[word[index]].append((word, index))

        return count

