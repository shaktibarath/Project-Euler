'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.

Author: Shakti Barath <shakti.barath@gmail.com>
'''

LIMIT = 4*10**6
even_sum = 0
def fibonacci(n):
    if(n == 1 or n == 2):
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

i = 1
while fibonacci(i) <= LIMIT:
    if fibonacci(i) % 2 == 0:
        even_sum += fibonacci(i)
    i += 1
print(even_sum)