# Factorial Of Number
# EasyAccuracy: 62.28%Submissions: 40639Points: 2
# Given a positive integer N. The task is to find factorial of N.
#
# Example 1:
#
# Input:
# N = 4
# Output: 24
# Explanation: 4! = 4 * 3 * 2 * 1 = 24

def factorial(N):
    if N <= 0 and N == 1:
        return 1
    f = 1
    for i in range(1, N + 1):
        f = f * i
    return f


print(factorial(4))
