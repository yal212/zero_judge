def print_pattern(rows, cols):
    # Write your code here
    for r in range(rows):
        for c in range(cols):
            print("*", end="")
        print("")


# Get input for rows and columns
rows = int(input())
cols = int(input())

# Call the function
print_pattern(rows, cols)
