# =========================
#        2D LISTS
# =========================
# A 2D list is basically a "list of lists".
# Think of it like a grid or a table with rows and columns.
# Example: Spreadsheet, Matrix, etc.

# Let's create a 2D list (a 3x3 matrix):
matrix = [
    [1, 2, 3],  # Row 0
    [4, 5, 6],  # Row 1
    [7, 8, 9]   # Row 2
]

# Accessing elements:
print("Top-left corner:", matrix[0][0])   # 1
print("Center element:", matrix[1][1])    # 5
print("Bottom-right corner:", matrix[2][2])  # 9

# Looping through each row and column:
for row in matrix:          # Outer loop → each row
    for item in row:         # Inner loop → each column item
        print(item, end=" ")
    print()  # Move to a new line after each row

# Using a 2D list to store student grades for 3 subjects.

grades = [
    ["Alice", 85, 90, 92],
    ["Bob",   78, 80, 85],
    ["Carol", 90, 95, 100]
]

# Print each student's grades
for student in grades:
    name = student[0] # Prints the value stored in the first cell of the first row
    marks = student[1:] # Prints the values stored in cell 1 and onwards in the second row
    print(f"{name}'s grades: {marks}")