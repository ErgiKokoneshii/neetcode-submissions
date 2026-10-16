class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0
        stack = []
        for digit in digits:
            res = res * 10 + digit
        res += 1
        for c in str(res):
            stack.append(int(c))
        return stack