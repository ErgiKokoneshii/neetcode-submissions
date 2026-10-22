class Solution:
    def sumSquaredDigits(self, s: str) -> int:
        ls = [int(c) ** 2 for c in s]
        return sum(ls)

    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1:
            if n in visited:
                return False
            visited.add(n)
            n = self.sumSquaredDigits(str(n))
        return True