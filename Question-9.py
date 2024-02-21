"""Write a Python program that takes a text file as input and returns the number of words of a given text file.
Note: Some words can be separated by a comma with no space."""


# Import the os module 
import os

def count_words(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"File '{file_path}' not found.")
        return

    # Check if the file is empty
    if os.path.getsize(file_path) == 0:
        print(f"File '{file_path}' is empty.")
        return

    with open(file_path, 'r') as file:
        data = file.read()

        # Replace commas without space with space and then split into words
        words = data.replace(',', ' ').split()

        print(f"Number of words in '{file_path}': {len(words)}")


# Input file path from the user
file_path = input("Enter the file path: ")
count_words(file_path)
