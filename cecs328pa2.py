def max_trees_sum(tree_array: list[int], grinder_count: int):
    n = len(tree_array) # the length of the tree array
    k = grinder_count # the number of grinders available

    # checks if there are less trees than grinders
    if n < k:
        return "You cannot send less trees than there are grinders."
    
    return 0 # placeholder

if __name__ == "__main__":
    try:
        tree_input = input("Enter the tree heights separated by spaces: ")
        trees = [int(x) for x in tree_input.split()]

        grinders = int(input("Enter the number of grinders available: "))

        result = max_trees_sum(trees, grinders)
        print(result)

    except ValueError:
        print("Invalid input. Please enter integers.")