class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        current_num = 0
        longest_count, current_count = 0, 0
        for num in hashSet:
            if num - 1 not in hashSet:
                current_num = num
                current_count = 1
            while current_num + 1 in hashSet:
                current_num = current_num + 1
                current_count += 1
            longest_count = max(longest_count, current_count)
        return longest_count
            
