"""
Title: 543 - Diameter Of Binary Tree
Category: MATH, Arrays
Source: LeetCode
Source Link: https://leetcode.com/problems/diameter-of-binary-tree/

Problem Statement:
    Given the root of a binary tree, return the length of the diameter of the tree.

Constraints:
    - The number of nodes in the tree is in the range [1, 104].
    - -100 <= Node.val <= 100

Example 1:
    Input: root = [1,2,3,4,5]
    Output: 3

Example 2:
    Input: root = [1,2]
    output: 1

Hints:
    - The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
    - This path may or may not pass through the root.
    - The length of a path between two nodes is represented by the number of edges between them.

How it works?
    -
    -
    -
"""



def calculate_height_and_diameter(tree, index):
    if index >= len(tree):
        return 0, 0  # Height and diameter are both 0 for leaf nodes

    # Using the recursive formula to be able to find the next node value in my list
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    # Assigning height and diameter for each node using the funtion
    left_height, left_diameter = calculate_height_and_diameter(tree, left_index)
    right_height, right_diameter = calculate_height_and_diameter(tree, right_index)

    # Calculate height for the current node
    height = 1 + max(left_height, right_height)

    # Calculate diameter for the current node
    diameter_through_root = left_height + right_height
    # Taking the maximum number between left path, right path, and the path that may or my not pass through the root.
    diameter = max(left_diameter, right_diameter, diameter_through_root)

    # Conditioning our index if out index value is 0 or not
    if index == 0:
        return diameter
    else:
        return height, diameter


def main():
    # Taking inputs from the user to build the binary tree.
    node0 = int(input("Enter the root of the tree: "))
    elements = int(input("How many elements do you want in this tree: "))
    no_child = "Null"

    # Build and display the tree structure
    tree = [index for index in range(node0, node0 + elements)]
    print(f"Node0: root = {node0}")

    # Print the tree by calculating the left and right children at each index i
    for i in range(len(tree)):
        left_child_index = 2 * i + 1
        right_child_index = 2 * i + 2

        # Conditioning our left and right child. If there is a left or right child that is greater than zero,
        # if there is not, make them None
        left_child = tree[left_child_index] if left_child_index < len(tree) else no_child
        right_child = tree[right_child_index] if right_child_index < len(tree) else no_child

        print(f"Node {tree[i]}: Left Child = {left_child}, Right Child = {right_child}")

    # Calculate and display the diameter of the tree by calling our function with 2 objects as tree and index[0]
    diameter = calculate_height_and_diameter(tree, 0)
    print(f"Diameter of the tree: {diameter}")


# Calling the main function
main()




"""def calculate_height_and_diameter(tree, index):
    if index >= len(tree):
        return 0, 0  # Height and diameter are both 0 for leaf nodes

    left_index = 2 * index + 1
    right_index = 2 * index + 2

    left_height, left_diameter = calculate_height_and_diameter(tree, left_index)
    right_height, right_diameter = calculate_height_and_diameter(tree, right_index)

    # Calculate height for the current node
    height = 1 + max(left_height, right_height)

    # Calculate diameter for the current node
    diameter_through_root = left_height + right_height  # No need to add 1 for the root
    diameter = max(left_diameter, right_diameter, diameter_through_root)

    if index == 0:
        return diameter
    else:
        return height, diameter


'''def calculate_tree_diameter(tree):
    # Calculate the diameter of the tree starting from the root (index 0)
    return calculate_height_and_diameter(tree, 0)[1]'''


def main():
    node0 = int(input("Enter the root of the tree: "))
    elements = int(input("How many elements do you want in this tree: "))

    # Build and display the tree structure
    tree = [index for index in range(node0, node0 + elements)]
    print(f"Node0: root = {node0}")

    # Print the tree by calculating the left and right children at each index i
    for i in range(len(tree)):
        left_child_index = 2 * i + 1
        right_child_index = 2 * i + 2

        left_child = tree[left_child_index] if left_child_index < len(tree) else None
        right_child = tree[right_child_index] if right_child_index < len(tree) else None

        print(f"Node {tree[i]}: Left Child = {left_child}, Right Child = {right_child}")

    # Calculate and display the diameter of the tree
    diameter = calculate_height_and_diameter(tree, 0)
    print(f"Diameter of the tree: {diameter}")


# Run the main function
main()"""
"""node0 = int(input("Enter the root of the tree: "))
elements = int(input("How many elements do you want in this tree: "))

# Assuming a list to represent the tree
tree = [index for index in range(node0, node0 + elements)]
print(f"Node0: root = {node0}")

# Print the tree structure
for i, node in enumerate(tree):
    left_child_index = 2 * i + 1
    right_child_index = 2 * i + 2

    left_child = tree[left_child_index] if left_child_index < len(tree) else None
    right_child = tree[right_child_index] if right_child_index < len(tree) else None

    print(f"Node {node}: Left Child = {left_child}, Right Child = {right_child}")


# Calculate the height of the tree
def calculate_height(index):
    if index >= len(tree):
        return 0
    left_height = calculate_height(2 * index + 1)
    right_height = calculate_height(2 * index + 2)
    return 1 + max(left_height, right_height)


# Print the height of the tree
height = calculate_height(0)
print(f"Height of the tree: {height}")"""
"""def calculate_height(tree, i):
    if i >= len(tree):
        return 0

    left_child_index = 2 * i + 1
    right_child_index = 2 * i + 2

    left_height = calculate_height(tree, left_child_index)
    right_height = calculate_height(tree, right_child_index)

    # The height of the tree rooted at index i is the maximum of left and right subtree heights plus 1
    return max(left_height, right_height) + 1


node0 = int(input("Enter the root of the tree: "))
elements = int(input("How many elements do you want in this tree: "))

# Assuming a list to represent the tree
tree = [index for index in range(node0, node0 + elements)]
print(f"Node{node0}: root = {node0}")

# Print the tree structure
for i, node in enumerate(tree):
    left_child_index = 2 * i + 1
    right_child_index = 2 * i + 2

    left_child = tree[left_child_index] if left_child_index < len(tree) else None
    right_child = tree[right_child_index] if right_child_index < len(tree) else None

    print(f"Node {i}: Left Child = {left_child}, Right Child = {right_child}")

# Calculate and print the height of the tree
tree_height = calculate_height(tree, 0)
print(f"Height of the tree: {tree_height}")"""
""""node0 = int(input("Enter the root of the tree: "))
elements = int(input("How many elements do you want in this tree: "))

# Assuming a list to represent the tree
tree = [index for index in range(node0, node0 + elements)]
print(f"Node{node0}: root = {node0}")

# Print the tree structure
for i, node in enumerate(tree):
    left_child_index = 2 * i + 1
    right_child_index = 2 * i + 2

    left_child = tree[left_child_index] if left_child_index < len(tree) else None
    right_child = tree[right_child_index] if right_child_index < len(tree) else None


    print(f"Node {node}: Left Child = {left_child}, Right Child = {right_child}")"""
'''for i in tree:

    if i == node0:
        root = node0
        print("root",root)

    if i % 2 == 0 and i > 1:
        left_child = i
        print("left",[left_child])

    elif i % 2 == 1:
        right_child = i
        print("right",[right_child])

    else:
        print("The binary tree is broken")'''
