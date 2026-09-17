class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}

        for i, n in enumerate(nums):
            indexes[n] = i

        for i, n in enumerate(nums):
            difference = target - n
            if difference in indexes and indexes[difference] != i:
                return [i, indexes[difference]]
        return []