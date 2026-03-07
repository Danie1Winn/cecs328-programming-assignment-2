def max_sum_tree(tree_array: list[int], number_of_tree_grinders: int):
    n = len(tree_array) # the length of the tree array
    k = number_of_tree_grinders # the number of grinders available
    
    current_sum = sum(tree_array[:k])   # calculate sum of the first k trees
    max_sum = current_sum               # initialize max_sum with the sum of the first k trees

    # sliding window, used to find the maximum sum of k contiguous trees
    for i in range(n - k):
        current_sum += tree_array[i + k] - tree_array[i] # removes "sliding out" element (left side)
        if current_sum > max_sum: max_sum = current_sum  # adds "sliding in" element (right side), checks if new sum is greater than current

    return max_sum

if __name__ == "__main__":
    # while loop to ensure valid grinder input
    while True:
        try:
            grinders = int(input("Enter number of grinders: "))
            break   # breaks loop if input is valid

        except ValueError:
            print("Invalid input. Please enter an integer\n") # prompts grinder input again if not integer

    # while loop to ensure valid tree input
    while True:
        try:
            tree_input = input("Enter tree heights separated by spaces: ")
            trees = [int(x) for x in tree_input.split()]    # converts input into list (`trees`) of integers

            # checks if there at least as many trees as grinders, if not prompts tree input again
            if len(trees) < grinders:
                print(f"\nError: Enter at least {grinders} trees.")
                continue

            break   # breaks loop if input is valid

        except ValueError:
            print("\nInvalid input. Please enter integers separated by spaces.") # prompts tree input again if not integers

    result = max_sum_tree(trees, grinders) # calls max_sum_tree function with user inputs
        
    # prints the user's inputs and the result
    print(f"\nTree heights: {trees}\nGrinders: {grinders}")
    print(f"Maximum sum of trees that can be processed: {result}")