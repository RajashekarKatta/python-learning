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


# Problem 4: Remove duplicates from a list numbers = [1, 2, 2, 3, 4, 4, 5]
class Solution:
    def remove_duplicate(self, numbers):
        i = 0
        for j in range(len(numbers)):
            if numbers[j] != numbers[i]:
                i += 1
                numbers[i] = numbers[j]
        return numbers[:i+1]

s = Solution()
numbers = [1, 2, 2, 3, 4, 4, 5]
print(s.remove_duplicate(numbers))      # output is [1, 2, 3, 4, 5]



print("\n\n\n")

# Problem 5: Find all even numbers in a list numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def even_numbers(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens
numbers = [1, 2, 3, 4, 5, 6]
print(even_numbers(numbers))


print("\n\n\n")


# Find odd numbers = [1,2,3,4,5,6,7,8,9]
def finding_odd_numbers(numbers):
    odd = []
    for num in numbers:
        if num % 2 != 0:
            odd.append(num)
    return odd
numbers = [1,2,3,4,5,6,7,8,9]
print(finding_odd_numbers(numbers))

print("\n\n\n")


# Count elements in a list
def count_elements(numbers):
    count = 0
    for i in range(len(numbers)):
        count += 1
    return f'numbers of elements: {count}'
numbers = [1, 2, 3, 4, 5, 6]    
print(count_elements(numbers))

print("\n\n\n")



# Check if an target element exists in a list
class Solution:
    def check_target_element(self, numbers, target):
        for num in numbers:
            if num == target:
                return True
        return False

s = Solution()
numbers = [10, 20, 30, 40, 50]
print(s.check_target_element(numbers, 40))

print("\n\n\n")


# Slice a list witout using Built in method
class Solution:
    def slicing_list(self, numbers, start, stop):
        result = []
        for i in range(len(numbers)):
            if i >= start and i < stop:
                result.append(numbers[i])
        return result

s = Solution()
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
start = 2
stop = 6
print(s.slicing_list(numbers, start,stop))


print("\n\n\n")
# Flatten a nested list convert it into a list
class Solution:
    def flattern_list(self, numbers):
        result = []
        for num in numbers:
            if isinstance(num, list):
                result.extend(self.flattern_list(num))
            else:
                result.append(num)
        return result
s = Solution()
numbers = [1, [2, [3, 4], 5], [6, 7]]
print(s.flattern_list(numbers))

print("\n\n\n")


# Multiply each element by 2
class Solution:
    def multiply_each_item(self, numbers):
        result = []
        for num in numbers:
            result.append(num * 2)
        return result

s = Solution()
numbers = [1, 2, 3, 4, 5, 6, 7]
print(s.multiply_each_item(numbers))

print("\n\n\n")


# Find index of an element Problem: Find index of 30 in [10,20,30,40].
class Solution:
    def index_of_ele(self,numbers, target):
        result = []
        for i in range(len(numbers)):
            if numbers[i] == target:
                result.append(i)
        return f'index of an {target} element is {result}'
s = Solution()
numbers = [10,20,30,40]
target = 30
print(s.index_of_ele(numbers, target))

print("\n\n\n")


# Count occurrences Problem: [1,2,2,3,2,4] → count 2
class Solution:
    def count_occurrence(self, numbers, target):
        count = 0
        for num in numbers:
            if num == target:
                count += 1
        return f'Count of 2 is: {count}'
s = Solution()
numbers = [1,2,2,3,2,4]
num = 2
print(s.count_occurrence(numbers, num))    


print("\n\n\n")
# Finding Count Using Dictionary
class Solution:
    def freq_count(self, nums):
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for i in freq:
            if freq[i] > 1:
                return freq[i]
s = Solution()
nums = [1,2,2,3,2,4]
print(s.freq_count(nums))


print("\n\n\n")


# Find Second Largest number
class Solution:
    def second_largest_element(self, nums):
        largest = float('-inf')
        second_largest = float('-inf')
        for num in nums:
            if num > largest:
                second_largest = largest
                largest = num
            elif num < second_largest and num != largest:
                second_largest = num
        return second_largest

s = Solution()
nums = [10, 20, 4, 45, 99, 99]
print(s.second_largest_element(nums))


print("\n\n\n")


