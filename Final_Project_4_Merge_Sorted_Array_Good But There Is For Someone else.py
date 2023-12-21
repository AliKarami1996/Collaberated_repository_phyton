"""
Title: 88 – Merge Sorted Array
Category: MATH, Arrays
Source: LeetCode
Source Link: https://leetcode.com/problems/merge-sorted-array/

Problem Statement:
    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
    and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Constraints:
    - nums1.length == m + n
    - nums2.length == n
    - 0 <= m, n <= 200
    - 1 <= m + n <= 200
    - -109 <= nums1[i], nums2[j] <= 109

Example 1:
    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]

Example 2:
    Input: nums1 = [1], m = 1, nums2 = [], n = 0
    Output: [1]

Hints:
    - Merge nums1 and nums2 into a single array sorted in non-decreasing order.
    - The final sorted array should not be returned by the function, but instead be stored inside the array nums1
    - To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements
      that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

How it works?
    - Getting two list of numbers from input,with two values (m,n) that are representing the number of elements in list.
    - Merging the lists in a way that the length of the output list is m + n.
    -
"""


class MergeSortedNumberLists:

    def __init__(self, list_numbers_1, list_length_1, list_numbers_2, list_length_2):

        self.list_numbers_1 = list_numbers_1[:list_length_1] + [0] * list_length_2
        self.list_numbers_2 = list_numbers_2
        self.list_length_1 = list_length_1
        self.list_length_2 = list_length_2

    def merge_lists(self):

        i = self.list_length_1 - 1
        j = self.list_length_2 - 1
        k = self.list_length_1 + self.list_length_2 - 1

        while i >= 0 and j >= 0:

            if self.list_numbers_1[i] > self.list_numbers_2[j]:
                self.list_numbers_1[k] = self.list_numbers_1[i]
                i -= 1
            else:
                self.list_numbers_1[k] = self.list_numbers_2[j]
                j -= 1
            k -= 1

        while j >= 0:

            self.list_numbers_1[k] = self.list_numbers_2[j]
            j -= 1
            k -= 1

    def zero_removal(self):

        self.list_numbers_1 = [zero for zero in self.list_numbers_1 if zero != 0]
        print(self.list_numbers_1)


def main():

    list_numbers_1 = input("Enter the first list of numbers: ")
    list_numbers_1 = [int(num) for num in list_numbers_1]

    m = int(input("Enter the value of m: "))

    list_numbers_2 = input("Enter the second list of numbers: ")
    list_numbers_2 = [int(num) for num in list_numbers_2]

    n = int(input("Enter the value of n: "))

    merge_list = MergeSortedNumberLists(list_numbers_1, m, list_numbers_2, n)
    merge_list.merge_lists()
    merge_list.zero_removal()


main()
