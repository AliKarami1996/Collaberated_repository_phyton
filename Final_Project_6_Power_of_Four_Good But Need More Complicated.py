"""
Title: 342 - Power Of Four
Category: MATH
Source: LeetCode
Source Link: https://leetcode.com/problems/power-of-four/

Problem Statement:
    Given an integer n, return true if it is a power of four. Otherwise, return false.

Constraints:
    - -231 <= n <= 231 - 1

Example 1:
    Input: n = 16
    Output: true

Example 2:
    Input: n = 5
    Output: false

Hints:
    - An integer n is a power of four, if there exists an integer x such that n == 4x.

How it works?
    - Gets a number from input.
    - Check the input to see if it is a power of four.
    - If yes return True if not return False.
"""


def power_of_four(n):

    power_four = 4 * n
    power_two = 1

    while power_two < power_four:
        power_two *= 2

    if power_four > 0 and power_four >= power_two:
        return True
    else:
        return False


def main():
    x = int(input("Enter an Integer: "))
    result = power_of_four(x)
    print(result)


main()

""" 
x = int(input("Enter a number between 0 - 99: "))
    power_four = 4 * x
    power_two = 1
    
    while power_two < power_four:
    power_two *= 2

if power_four > 0 and power_four == power_two:
    formula = True
    print("n = 4 * x")
    print("4 *", x, "= ", power_four)
else:
    formula = False
    print("Result is not a power of four", "4 *", x, "= ", power_four)"""
