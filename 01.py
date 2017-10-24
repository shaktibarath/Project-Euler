
# Project Euler problem set 01 implementation.
# Problem 1: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Author: Shakti Barath <shakti.barath@gmail.com>

total_sum = 0
for i in range(1, 1000):
    if (i % 3 == 0 or i % 5 == 0):
        total_sum = total_sum + i
print("Sum of multiples of 3 and 5 (<1000) is:", total_sum)