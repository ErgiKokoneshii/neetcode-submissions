class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        current_num = 0
        longest_streak, current_streak = 0, 0
        for num in hashSet:
            if num - 1 not in hashSet:
                current_num = num
                current_streak = 1
            while current_num + 1 in hashSet:
                current_num += 1
                current_streak += 1
            longest_streak = max(longest_streak, current_streak)
        return longest_streak
