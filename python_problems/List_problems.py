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


# Find second smallest element
class Solution:
    def second_smallest_element(self, nums):
        smallest = float('inf')
        second_smallest = float('inf')
        for num in nums:
            if num < smallest:
                second_smallest = smallest
                smallest = num
            elif num < second_smallest and num != smallest:
                second_smallest = num
                
        return second_smallest
        
s = Solution()
numbers = [10, 20, 4, 45, 99]
print(s.second_smallest_element(numbers))

print("\n\n\n")


# Find all pairs with a given sum numbers = [1,2,3,4,5] target = 5
class Solution:
    def pair_sum(self, numbers, target):
        pairs = []
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    pairs.append([i, j])
        return pairs
s = Solution()
numbers = [1,2,3,4,5]
target = 5
print(s.pair_sum(numbers, target))


# Finding all Pairs using Hash map
class Solution:
    def find_all_pairs(self, numbers, target):
        seen = set()
        for num in numbers:
            compliment = target - num
            if compliment in seen:
                print (compliment, num)
            seen.add(num)

s = Solution()
numbers = [1,2,3,4,5]
s.find_all_pairs(numbers, 5)

print("\n")
# Finding all Pairs with sorted list given
class Solution:
    def find_pairs(self, nums, target):
        left, right = 0, len(nums) -1
        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                print(nums[left], nums[right])
                left += 1
                right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1

s = Solution()
nums = [1,2,3,4,5]
s.find_pairs(nums, 5)

print("\n")

##### Right Rotation by k positions
class Solution:
    def right_rotate(self, nums, k):
        n = len(nums)
        k = k % n
        def revers(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        revers(0, n-1)
        revers(0, k-1)
        revers(k, n-1)
        return nums
s = Solution()
nums = [1,2,3,4,5]
print(s.right_rotate(nums, 2))

print("\n")


# left rotation
class Solution:
    def left_rotation(self, nums, k):
        n = len(nums)
        k = k % n
        def revers(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        revers(0, k-1)
        revers(k, n-1)
        revers(0, n-1)
        return nums
s = Solution()
nums = [1,2,3,4,5]
print(s.left_rotation(nums, 2))

print("\n")


# Merge two sorted lists
# Using Two Pointers (Classic Method)
def merge_sorted_lists(list1, list2):
    merged = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged
    
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print(merge_sorted_lists(list1, list2))

print("\n")

class Solution:
    def finding_duplicates(self, numbers):
        duplicate = []
        for num in set(numbers):
            if numbers.count(num) > 1:
                duplicate.append(num)
        return duplicate
s = Solution()
numbers = [1, 2, 2, 3, 3, 3, 4]
print(s.finding_duplicates(numbers))

print("\n")

# Another way to Find Duplicate Numbers
class Solution:
    def find_duplicates(self, arr):
        duplicates = []
        seen = set()
        for num in arr:
            if num in seen:
                duplicates.append(num)
            seen.add(num)
        return duplicates

s = Solution()
numbers = [1, 2, 2, 3, 3, 3, 4]
print(s.find_duplicates(numbers))

print("\n")

# Write a Python program to generate the next 15 leap years starting from a given year. Populate the leap years into a list and display the list. 
class Solution():
    def leap_years(self, given_year):
        leap_years = []
        current_year = given_year
        while len(leap_years) < 15:
            if (current_year % 4 == 0 and current_year % 100 != 0) or current_year % 400 == 0:
                leap_years.append(current_year)
            current_year += 1
        return leap_years

s = Solution()
print(s.leap_years(2002))