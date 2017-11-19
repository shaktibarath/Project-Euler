'''
10001st prime:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?

Author: Shakti Barath <shakti.barath[at]gmail.com>
'''
import time


def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if (n % i == 0):
            return False
    return True


def find_nth_prime(n):
    count = 1
    i = 2
    prime_list = []
    while (count <= n):
        if (isPrime(i)):
            prime_list.append(i)
            count += 1
        i += 1
    return prime_list


start = time.time()
answer = max(find_nth_prime(10001))
t_time = (time.time() - start)

print("The answer %s calculated in %s seconds" % (answer, t_time))
