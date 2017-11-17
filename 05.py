'''
Smallest multiple:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Author: Shakti Barath <shakti.barath[at]gmail.com>
'''
import fractions

def find_smallest_multiple(n):
    result = 1
    for i in range(1, n+1):
        result = (result*i)/fractions._gcd(result,i)
    return result


print(find_smallest_multiple(20))

