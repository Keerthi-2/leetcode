class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        
        return sum(all(map(le,map(abs,(v-u,u-w,v-w)),(a,b,c))) for v,u,w in combinations(arr,3))

