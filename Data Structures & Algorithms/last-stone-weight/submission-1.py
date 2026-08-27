class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)

        while len(stones) > 1:
            last = heapq._heappop_max(stones)
            secondlast = heapq._heappop_max(stones)
            if last > secondlast:
                heapq._heappush_max(stones, last-secondlast)

        stones.append(0)
        return abs(stones[0]) 
