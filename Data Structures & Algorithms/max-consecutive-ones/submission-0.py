class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones_arr: List[int] = []
        temp = 0
        for num in nums:
            if num == 1:
                temp += 1
            else:
                ones_arr.append(temp)
                temp = 0
        ones_arr.append(temp)
        return max(ones_arr)