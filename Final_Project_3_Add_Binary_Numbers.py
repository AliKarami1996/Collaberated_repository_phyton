"""
Title: 67 – Add Binary
Category: MATH
Source: LeetCode
Source Link: https://leetcode.com/problems/add-binary/

Problem Statement:
    Given two binary strings a and b, return their sum as a binary string.

Constraints:
    - 1 <= a.length, b.length <= 104
    - a and b consist only of '0' or '1' characters.
    - Each string does not contain leading zeros except for the zero itself.

Example 1:
    Input: a = "11", b = "1"
    Output: "100"

Example 2:
    Input: a = "1010", b = "1011"
    Output: "10101"

Hints:
    - Takes a binary number in form of string from input. Evaluates each string and converts to its decimal number.
    - Sum up the decimal numbers.
    - Convert the sum to its binary number in form of string.

How it works?
    - Take a string number from the user and inserting them into an list of
    -
    -
"""


class BinaryNumbers:

    def __init__(self, bin_1, bin_2):
        self.bin_1 = bin_1
        self.bin_2 = bin_2
        self.result_1 = 0
        self.result_2 = 0
        self.sum_both_bin_numbers = 0
        self.binary_sum = " "

    def input_validation(self):

        # Validate input lengths
        if not (1 <= len(self.bin_1) <= 10 ** 4) or not (1 <= len(self.bin_2) <= 10 ** 4):
            print("Invalid input length. Please ensure 1 <= length <= 10^4.")
            exit()

        # Validate input characters
        if not all(element in '01' for element in self.bin_1) or not all(element in '01' for element in self.bin_2):
            print("Invalid characters in input. Please use only '0' or '1'.")
            exit()

    def conversion_binary_to_decimals(self):

        # Convert binary numbers to decimal
        for i in range(len(self.bin_1)):
            self.result_1 = self.result_1 * 2 + int(self.bin_1[i])

        for j in range(len(self.bin_2)):
            self.result_2 = self.result_2 * 2 + int(self.bin_2[j])

    def sum_numbers(self):

        self.sum_both_bin_numbers = self.result_1 + self.result_2
        print("Sum in decimal:", self.sum_both_bin_numbers)

    def conversion_decimal_to_binary(self):

        # Convert the sum back to binary

        while self.sum_both_bin_numbers > 0:
            remainder = self.sum_both_bin_numbers % 2
            self.binary_sum = str(remainder) + self.binary_sum
            self.sum_both_bin_numbers = self.sum_both_bin_numbers // 2

        # Ensure the binary sum is not an empty string (handles the case when the sum is 0)
        if not self.binary_sum:
            self.binary_sum = '0'

        print("Sum in binary:", self.binary_sum)


def main():

    bin_1 = input("Enter the first binary number: ")
    bin_2 = input("Enter the second binary number: ")

    summation = BinaryNumbers(bin_1, bin_2)

    summation.input_validation()
    summation.conversion_binary_to_decimals()
    summation.sum_numbers()
    summation.conversion_decimal_to_binary()


main()
