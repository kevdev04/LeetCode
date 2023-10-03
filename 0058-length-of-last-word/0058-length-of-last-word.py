class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #first approach string split
        if s.split():
            return len(s.split()[-1])
        return 0