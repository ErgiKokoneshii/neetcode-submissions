class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            is_valid = op.isdigit() or (op.startswith("-") and op[1:].isdigit())
            if is_valid:
                stack.append(int(op))
            elif op == "+" and len(stack) > 1:
                val1 = stack[-1]
                val2 = stack[-2]
                stack.append(val1 + val2)
            elif op == "C" and stack:
                stack.pop()
            elif op == "D" and stack:
                val = stack[-1]
                stack.append(val * 2)
        print(stack)
        return sum(stack)