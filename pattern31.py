def print_pattern(rows):
    # Upper half of the pattern
    for i in range(1, rows):
        print("*" * i)

    # Middle line with extra asterisk
    print("*" * (2 * rows - 1))

    # Lower half of the pattern
    for i in range(rows - 1, 0, -1):
        print("*" * i)

# Number of rows in the pattern
rows = 5

# Call the function to print the pattern
print_pattern(rows)