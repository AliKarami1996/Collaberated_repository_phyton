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
