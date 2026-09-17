class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        noDupes = list(dict.fromkeys(nums))
        if noDupes != nums:
            return True
        return False