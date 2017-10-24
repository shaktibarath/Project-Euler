
# Project Euler problem set 01 implementation.
#
# Author: Shakti Barath <shakti.barath@gmail.com>

total_sum = 0
for i in range(1, 1000):
    if (i % 3 == 0 or i % 5 == 0):
        total_sum = total_sum + i
print("Sum of multiples of 3 and 5 (<1000) is:", total_sum)