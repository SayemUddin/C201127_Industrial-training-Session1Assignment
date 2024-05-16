
matrix = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]

# Accessing elements in the matrix
print("Element at row 2, column 3:", matrix[1][2])  # Prints 6

# Modifying elements in the matrix
matrix[0][0] = 10
print("Updated matrix after modification:")
for row in matrix:
    print(row)

# Iterating through the matrix
print("Iterating through the matrix:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()




# Create a tuple with mixed data types
mixed_tuple = ("apple", 10, True, 3.14)

# Create a dictionary with mixed data types using the tuple
mixed_dict = {
    mixed_tuple: "This is a mixed tuple",
    "key": "value",
    42: ["a", "b", "c"]
}
print(mixed_dict)
