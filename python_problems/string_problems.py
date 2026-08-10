# Basic striing problems in python
# Find Length of string Without Using len()
class Solution:
    def length_str(self, s):
        length = 0
        for char in s:
            length += 1
        return length

s = Solution()
print(s.length_str("Gemini"))