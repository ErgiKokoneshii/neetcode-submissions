class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(', '}':'{', ']':'['}
        res = []
        for c in s:
            if c in brackets.values():
                res.append(c)
            elif c in brackets.keys():
                if not res:
                    return False
                if brackets.get(c) != res.pop():
                    return False
        if not res:
            return True
        return False