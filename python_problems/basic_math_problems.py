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


# Printing all Prime Numbers up to N
class Solution:
    def Prime_numbers_upto_n(self, n):
        for num in range(2, n + 1):
            is_prime = True
            for i in range(2, int(num ** 0.5)+1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(num, end=" ")
s = Solution()
s.Prime_numbers_upto_n(50)

print("\n")
# generating first N prime numbers
class Solution:
    def first_n_primes(self, n):
        count = 0
        num = 2
        while count < n:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(num, end=" ")
                count += 1
            num += 1

s = Solution()
s.first_n_primes(10)             # It will print first n prime numbers

print("\n")

# Fing the Factorial of given number
class Solution:
    def Factorial(self, n):
        if n == 0 or  n == 1:
            return 1
        result = 1
        for i in range(2, n+1):
            result *= i
        return result

s = Solution()
print(s.Factorial(6))

print("\n")

#Finding the Factorial of the given number using recursion
class Solution:
    def factorial_recursion(self, n):
        if n == 0 or n == 1:
            return 1
        return n * self.factorial_recursion(n-1)

s = Solution()
print(s.factorial_recursion(5))

print("\n")

# Reverse a number
class Solution:
    def reverse_number(self, n):
        rev = 0
        while n > 0:
            rev = rev * 10 + (n % 10)
            n //= 10
        return rev
s = Solution()
print(s.reverse_number(1234))


# reverese a number
class Solution:
    def rev_number(self, n):
        rev = 0
        sign = -1 if n < 0 else 1
        n = abs(n)
        while n > 0:
            rev = rev * 10 + n % 10
            n //= 10
        rev *= sign

        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev
        
s = Solution() 
s.rev_number(-1234)

print("\n")

#GCD (HCF) – Euclidean Algorithm
class Solution:
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
s = Solution()
s.gcd(48, 18)

print("\n")

# LCM of Two Numbers
class Solution:
    def find_gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
    def lcm(self, a, b):
        return (a * b) // self.find_gcd(a, b)

s = Solution()
s.lcm(4,6)

print("\n")

# Count Digits
class Solution:
    def count_digit(self, n):
        count = 0
        while n > 0:
            count += 1
            n //= 10
        return count
s = Solution()
s.count_digit(12345)
print("\n")



# Armstrong Number
class Solution:
    def Armstrong_number(self, n):
        num = n
        power = len(str(n))
        total = 0         
        while n > 0:
            digit = n % 10
            total += digit ** power
            n //= 10
        return total == num
           
s = Solution()
print(s.Armstrong_number(153)) 



# Automorphic Number:
class Solution:
    def automorphic_number(self, n):
        square = n * n
        while n > 0:
            if n % 10 != square % 10:
                return False
            n //= 10
            square //= 10
        return True

s = Solution()
print(s.automorphic_number(25))

print("\n")
# Fibonacci Series
class Solution:
    def fibonacci(self, n):
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a+b
        return b
s = Solution()
print(s.fibonacci(8))


# Fibonacci Series the first n numbers
class Solution:
    def fibonacci_series(self, n):
        a, b = 0, 1
        
        for _ in range(n):
            print(a, end=' ')
            a, b = b, a+b
s = Solution()
s.fibonacci_series(8)


print("\n")
# fibonacci series --> upto n 
class Solution:
    def fibo_series(self, n):
        a, b = 0, 1
        while a <= n:
            print(a, end=' ')
            a, b = b, a + b
        
s = Solution()
s.fibo_series(10)
