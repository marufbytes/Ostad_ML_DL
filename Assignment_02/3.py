my_tuple = (101, "Maruf", 3.88, True)

student_id, name, cgpa, status = my_tuple

print("Student ID:", student_id)
print("Name:", name)
print("CGPA:", cgpa)
print("Status:", status)

another_tuple = (102, "Rahim", 3.75, False)

print("my_tuple == another_tuple:", my_tuple == another_tuple)
print("my_tuple != another_tuple:", my_tuple != another_tuple)
print("my_tuple < another_tuple:", my_tuple < another_tuple)
print("my_tuple > another_tuple:", my_tuple > another_tuple)

# Main difference between Lists and Tuples:
# List: Mutable, meaning its elements can be changed, added, or removed.
# Example:
# my_list = [1, 2, 3]
# my_list[0] = 10

# Tuple: Immutable, meaning its elements cannot be changed after creation.
# Example:
# my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # This will cause an error