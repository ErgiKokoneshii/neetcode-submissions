class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        max_area = 0
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][0] >= heights[i]:
                h, j = stack.pop()
                w = i - j
                a = h * w
                max_area = max(max_area, a)
                start = j
            stack.append([heights[i], start])

        while stack:
            h, j = stack.pop()
            w = n - j
            max_area = max(max_area, h * w)
        print(stack)
        return max_area