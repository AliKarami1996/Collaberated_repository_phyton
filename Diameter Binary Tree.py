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
