'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
Author: Shakti Barath <shakti.barath[at]gmail.com>

Algorithm used:  Sieve of Eratosthenes
'''
import math

value = 600851475143


def prime_factors(value):
    p_list = []

# if value is divisible by 2, then divide it by 2.
    while value%2 == 0:
        p_list.append(2)
        val /=2
# Remove odd numbers
    for i in range(3, int(math.sqrt(value))+1, 2):
        while value%i == 0:
            p_list.append(i)
            value /= i
    if value > 2:
        p_list.append(value)

    return p_list

print(max(prime_factors(value)))