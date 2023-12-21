"""
Title: 234 - Palindrome Linked List
Category: MATH, Arrays
Source: LeetCode
Source Link: https://leetcode.com/problems/palindrome-linked-list/

Problem Statement:
    Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Constraints:
    - The number of nodes in the list is in the range [1, 105].
    - 0 <= Node.val <= 9

Example 1:
    Input: head = [1,2,2,1]
    Output: true

Example 2:
    Input: n = 5
    Output: false

Hints:
    - Enter some numbers, then numbers will be checked for palindrome.

How it works?
    - Gets some number from input, then puts them in the list.
    - Reverse the list, and compare the elements with the original list.
    - If elements are equal, returns True, if not returns False.
"""


class CheckLinearPalindrome:
    def __init__(self, node):
        self.node = node

    def is_palindrome(self):
        is_palindrome = True
        reverse_node = self.node[::-1]
        i = 0
        j = 0
        while is_palindrome and i < len(self.node) and j < len(reverse_node):
            if self.node[i] in range(10):
                if self.node[i] == reverse_node[j]:
                    i += 1
                    j += 1
                else:
                    is_palindrome = False
                    break
            else:
                print("The node value is not within the range of 0 - 9")
                print("Enter a valid number")
                break
        print(is_palindrome)


def main():
    node = [int(index) for index in input("Enter some numbers: ")]
    check_palindrome = CheckLinearPalindrome(node)
    check_palindrome.is_palindrome()


main()
