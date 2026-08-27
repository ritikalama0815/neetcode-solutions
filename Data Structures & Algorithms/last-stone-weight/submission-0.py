class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)

        while len(stones) > 1:
            first = heapq._heappop_max(stones)
            second = heapq._heappop_max(stones)
            if first > second:
                heapq._heappush_max(stones, first-second)

        stones.append(0)
        return abs(stones[0]) 
