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
