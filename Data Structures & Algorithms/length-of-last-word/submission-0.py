class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ls = s.split(" ")
        clean_ls = [w for w in ls if w]
        print(clean_ls)
        return len(clean_ls[-1])