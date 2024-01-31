class Solution:
    def countKeyChanges(self, s: str) -> int:
        prev_char = s[0].lower()
        res = 0
        for char in s:
            res += prev_char != char.lower()
            prev_char = char.lower()
        return res
