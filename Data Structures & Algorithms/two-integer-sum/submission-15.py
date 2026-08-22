class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, n in enumerate(nums):
            hashmap[n] = i
        
        for i, n in enumerate(nums):
            j = target - n
            if j in hashmap and hashmap[j]!=i:
                return [i, hashmap[j]]

        return []