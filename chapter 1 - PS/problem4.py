import os

# Specify the directory path
directory_path = "C:\\Harshit\\python\\chapter 1 - ps"

# List and print the contents
try:
    contents = os.listdir(directory_path)
    print("Contents of the directory:")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")