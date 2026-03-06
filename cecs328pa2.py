def max_trees_sum(tree_array: list[int], grinder_count: int):
    n = len(tree_array) # the length of the tree array
    k = grinder_count # the number of grinders available

    # checks if there are less trees than grinders
    if n < k: return "You cannot send less trees than there are grinders."
    
    current_sum = sum(tree_array[:k])   # calculate sum of the first k trees
    max_sum = current_sum               # initialize max_sum with the sum of the first k trees

    # sliding window, used to find the maximum sum of k contiguous trees
    for i in range(n - k):
        current_sum += tree_array[i + k] - tree_array[i] # removes "sliding out" element (left side)
        if current_sum > max_sum: max_sum = current_sum  # adds "sliding in" element (right side), checks if new sum is greater than current

    return max_sum

if __name__ == "__main__":
    try:
        tree_input = input("Enter the tree heights separated by spaces: ")
        trees = [int(x) for x in tree_input.split()]

        grinders = int(input("Enter the number of grinders available: "))

        print(f"\nTree heights: {trees}\nGrinders: {grinders}\n")

        result = max_trees_sum(trees, grinders)
        print(f"Maximum sum of trees that can be processed: {result}")

    except ValueError:
        print("Invalid input. Please enter integers.")