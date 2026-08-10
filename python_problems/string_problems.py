# Basic striing problems in python
# Find Length of string Without Using len()
class Solution:
    def length_str(self, s):
        length = 0
        for char in s:
            length += 1
        return length

c = Solution()
print(c.length_str("Gemini"))


# # Count Frequency of Each Character problem
class Solution:
    def character_count(self, s):
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        return freq
c = Solution()
print(c.character_count("banana"))


# Fing the first Non-repeated character
class Solution:
    def non_repeted_char(self, s):
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        for char in freq:
            if freq[char] == 1:
                return char
c = Solution()
print(c.non_repeted_char("rajashekar"))


# Find the second Non repeateed character
class Solution:
    def second_non_repeated_char(self, s):
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        non_repeated_chars = []
        for char in freq:
            if freq[char] == 1:
                non_repeated_chars.append(char)
        return non_repeated_chars[1]

c = Solution()
print(c.second_non_repeated_char("rajashekar"))

# Check if Two Strings are Anagrams

class Solution:
    def check_anagrams(self, s1, s2):
        if len(s1) != len(s2):
            return False
        freq = {}
        for char in s1:
            freq[char] = freq.get(char, 0) + 1

        for char in s1:
            if char not in freq:
                return False
            freq[char] -= 1

            if freq[char] < 0:
                return False
        return True

c = Solution()
print(c.check_anagrams("Silent", "listen"))


# Capitalize First Letter of Each Word (Title Case) in the fiven sentence
class Solution:
    def first_letter_capital_in_each_word(self, text):
        words = text.split()
        result = []
        for word in words:
            result.append(word.capitalize())
        return ' '.join(result)

c = Solution()
print(c.first_letter_capital_in_each_word("hello eveery one"))

# Replace All Digits with *
class Solution:
    def replace(self, text):
        result = ''
        for char in text:
            if char.isdigit():
                result += '*'
            else:
                result += char
        return result
c = Solution()
print(c.replace("a1b2c3"))