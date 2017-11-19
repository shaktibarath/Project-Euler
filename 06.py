'''
Sum square difference:
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and
the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Author: Shakti Barath <shakti.barath[at]gmail.com>
'''

# Function to calculate sum of the squares of first 'n' natural numbers.
def sum_of_squares(r):
	sos = (r*(r+1) * (2*r+1))/6
	return sos

# Function to calculate square of the sum of first 'n' natural numbers.

def square_of_sum(r):
	sum = (r*(r+1)/2)**2
	return sum

print(sum_of_squares(100) - square_of_sum(100))

