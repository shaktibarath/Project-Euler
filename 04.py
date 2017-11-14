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
    num1 = 999
    palindrome_arr = []
    while num1 > 100:
        num2 = 990
        if num2 > num1:
            num2 = num1 - (num1 % 11)
        while num2 > 109:
            if isPalindrome(num1 * num2):
                palindrome_arr.append(num1 * num2)
            num2 -= 11
        num1 -= 1
    palindrome_arr.sort()
    return palindrome_arr[len(palindrome_arr) -1]

print("The largest palindrome made from the product of two 3-digit numbers is:", largest_palindrome())