class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(heights) - 1

        while l <= r:
            width = r-l
            currentA = width * min(heights[l], heights[r]) # not cause overflow
            max_area = max(max_area, currentA)

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1        
        return max_area