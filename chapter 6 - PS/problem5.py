# 5. Write a program which finds out whether a given name is present in a list or not.
names = ["Alice", "Bob", "Charlie", "David", "Eva"]
name_to_check = input("Enter a name to check: ")
if name_to_check in names:
    print(f"{name_to_check} is present in the list.")
else:
    print(f"{name_to_check} is not present in the list.")
    