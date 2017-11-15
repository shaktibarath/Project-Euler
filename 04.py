'''
Largest palindrome product:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

Author: Shakti Barath <shakti.barath[at]gmail.com>
'''


def reverse(n):
    reverse = 0
    while (n > 0):
        reminder = n % 10
        reverse = (reverse * 10) + reminder
        n = n // 10
    return reverse


def isPalindrome(x):
    str1 = str(reverse(x))
    str2 = str(x)
    if str1 == str2:
        return True
    else:
        return False


def largest_palindrome():
    a = 999
    palindrome_arr = []
    while a > 100:
        b = 990
        if b > a:
            b = a - (a%11)
        while b > 109:
            if isPalindrome(a * b):
                palindrome_arr.append(a * b)
            b -= 11
        a -= 1

    palindrome_arr.sort()
    return palindrome_arr[len(palindrome_arr) -1]

print("The largest palindrome made from the product of two 3-digit numbers is:", largest_palindrome())