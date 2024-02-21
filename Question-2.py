"""Write a Python program to read first n lines of a file."""

# my_file = open("sample.txt", "r") 
# print(my_file.read(10))

import os
def read_n_characters(file_path, num_chars):
    if os.path.exists(file_path):
        my_file = open(file_path, "r")  # Open the file in read ('r') mode
        content = my_file.read(num_chars)
        print(content)
        my_file.close()

        if not content:
            print(f"File '{file_path}' is empty.")
        else:
            print(content)
    else:
        print(f"Error: File '{file_path}' not found.")

# Get user input for file path and number of characters
file_path = input("Enter the file path: ")
num_characters = (input("Enter the number of characters to read: "))

if num_characters.isdigit():
    num_characters = int(num_characters)
    read_n_characters(file_path, num_characters)
else:
    print("Please enter a valid integer for the number of characters.")

