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

# Check if a string is a Palindrome
class Solution:
    def check_palindrome(self, s):
        left, right = 0, len(s) -1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
c = Solution()
print(c.check_palindrome("malayalam"))



# Reverseing a string
class Solution:
    def revers_string(self, s):
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)
c = Solution()
print(c.revers_string("king"))

# ount vowels and consonants
class Solution:
    def count_vowels_consonants(self, s):
        vowels = "AEIOUaeiou"
        v_count = 0     
        c_count = 0
        for char in s:
            if char.isalpha():
                if char in vowels:
                    v_count += 1
                else:
                    c_count += 1
        return [v_count, c_count]
s = Solution()
print(s.count_vowels_consonants("HelloWorld"))


# Encode String with Run-Length Encoding (RLE)   Input: "aaabbcddd" → Output: "a3b2c1d3"
class Solution:
    def encode_string(self, text):
        result = ''
        count = 1
        for i in range(1, len(text)):
            if text[i] == text[i-1]:
                count += 1
            else:
                result += text[i-1] + str(count)
                count = 1
        result += text[-1] + str(count)
        return result
sol = Solution()
print(sol.encode_string("aaabbcccd"))


# Check if two strings are anagrams  O(n), O(1)
class Solution:
    def check_anagrams(self, s1, s2):
        if len(s1) != len(s2):
            return False
        freq = [0] * 26
        for i in range(len(s1)):
            freq[ord(s1[i]) - ord('a')] += 1
            freq[ord(s2[i]) - ord('a')] -= 1
        return all(c == 0 for c in freq)
s = Solution()
print(s.check_anagrams("listen", "silent"))


# Remove duplicate characters
class Solution:
    def remove_duplicates(self, s):
        seen = set()
        result = []
        for char in s:
            if char not in seen:
                result.append(char)
                seen.add(char)
        return ''.join(result)
s = Solution()
print(s.remove_duplicates("programming"))

# Check if string contains only digits
class Solution:
    def only_digits(self, s):
        if len(s) == 0:
            return False
        for char in s:
            if char < '0' or char > '9':
                return False
        return True
s = Solution()
print(s.only_digits("12345"))


# Remove spaces from a string
class Solution:
    def remove_spaces(self, s):
        result = []
        for char in s:
            if char != ' ':
                result.append(char)
        return '' .join(result)
s = Solution()
print(s.remove_spaces("hello world welcome"))


# Find the subsequence of the given string
class Solution:
    def find_subsequence(self, s1, s2):
        result = []
        j = 0
        for char in s1:
            if j < len(s2) and char == s2[j]:
                result.append(char)
                j += 1
        return ''.join(result)

s = Solution()
print(s.find_subsequence("ABCDE","ACE"))

# Find Subsequence Characters Between Two Strings
class Solution:
    def is_substring(self, substring, main_string):
        it = iter(main_string)
        for char in substring:
            if char not in it:
                return False
        return True

    def find_subsquence(self, s1, s2):
        longest_match = ''
        for i in range(len(s1)):
            for j in range(i , len(s1)):
                substring = s1[i:j+1]
                if self.is_substring(substring, s2) and len(substring) > len(longest_match):
                    longest_match = substring
        return longest_match
s = Solution()
print(s.find_subsquence("Python", "typhoon"))


class Solution:
    def check_substring(self, s , sub):
        n = len(s)
        m = len(sub)
        for i in range(n - m + 1):
            j = 0
            while j < m and s[i+j] == sub[j]:
                j += 1

            if j == m:
                return True
        return False

c = Solution()
print(c.check_substring("python", "thon"))


# Advance Level Programs in String
# Longest Word in a Sentence --> Input: "I love programming in Python" → Output: "programming"
class Solution:
    def longest_word(self, text):
        words = text.split()  # split the sentence into words
        max_len = 0
        longest = ""
        for word in words:
            if len(word) > max_len:
                max_len = len(word)
                longest = word
        return f"Longest Word in a Given Sentence: '{longest}' \nlength is: {max_len}"
sol = Solution()
print(sol.longest_word("I love programming in Python"))