class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # BRUTE FORCE: speed = 1, increment the speed until the condition is reached
        # OPTIMAL: speed 1-maximum number of banana pile since koko cant eat more than one pile
        # since the search space is sorted, we can use binary search rather than searching through the piles
        min_speed, max_speed = 1, max(piles)

        while min_speed<=max_speed:
            mid = (min_speed+max_speed)//2
            total_hours = 0
            for p in piles:
                total_hours += math.ceil(float(p)/mid)
            if total_hours <=h:
                result = mid
                max_speed = mid-1
            else:
                min_speed = mid+1
        
        return result
            