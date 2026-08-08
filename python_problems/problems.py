# List Basic Problems
# Problem 1: Sum of all elements in a list numbers = [10, 20, 30, 40, 50]
class Solution:
    def sum_of_elements(self, numbers):
        total = 0
        for num in numbers:
            total += num
        return f"Sum of the Numbers: {total}"
s = Solution()
numbers = [10, 20, 30, 40, 50]
print(s.sum_of_elements(numbers))           # Sum of the Numbers is 150


print("\n\n\n")
# Problem 2: Find the maximum and minimum in a list numbers = [5, 12, 3, 7, 1, 9]
class Solution:
    def max_min_values(self, numbers):
        max_value = numbers[0]
        min_value = numbers[0]
        for num in numbers:
            if num > max_value:
                max_value = num
            elif num < min_value:
                min_value = num
        return max_value, min_value

s = Solution()
numbers = [5, 12, 3, 7, 1, 9]
print(s.max_min_values(numbers))    # Max_value, Min_value is 12, 1


print("\n\n\n")


# Problem 3: Reverse a list numbers = [1, 2, 3, 4, 5]
class Solution:
    def reversing_a_list(self, numbers):
        left, right = 0, len(numbers) - 1
        while left < right:
            numbers[left], numbers[right] = numbers[right], numbers[left]
            left += 1
            right -= 1
        return numbers

s = Solution()
numbers = [1, 2, 3, 4, 5]
print(s.reversing_a_list(numbers))     # Reverse of a List -> [5, 4, 3, 2, 1]


print("\n\n\n")