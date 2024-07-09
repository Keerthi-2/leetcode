class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        idle_time=0
        wait_time=0

        for c in customers:
            idle_time=max(c[0],idle_time)+c[1]

            wait_time+=idle_time-c[0]
        
        avg=wait_time/len(customers)

        return avg
