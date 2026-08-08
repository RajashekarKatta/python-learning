# Python Basic Math Problems or using maths in python problem to find the solution
# # Check prime number
class Solution:
    def check_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
s = Solution()
print(s.check_prime(7))

class Solution:
    def check_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def find_primes(self,nums):
        primes = []
        for num in nums:
            if self.check_prime(num):
                primes.append(num)
        return primes

s = Solution()
nums = [1, 2, 3, 4, 5, 10, 11, 15]
print(s.find_primes(nums))

print("\n")
