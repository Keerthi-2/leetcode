class Solution:
    def knightProbability(self, n: int, k: int, r: int, c: int) -> float:
        queue = defaultdict(int)
        queue[r,c] = 1.0
        p = 1
        for _ in range(k):
            p = 0
            next_queue = defaultdict(int)
            for (r,c),rcp in queue.items():
                for dr,dc in (-1,-2),(1,-2),(2,-1),(2,1),(-1,2),(1,2),(-2,-1),(-2,1):
                    if n > (nr := r + dr) >= 0 <= (nc := c + dc) < n:
                        next_queue[nr,nc] += rcp / 8
                        p += rcp / 8
            queue = next_queue
        return p