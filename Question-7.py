"""Write a Python program to assess if a file is closed or not."""
import os
def assess_file_closed(file_path):
    if os.path.exists(file_path):   
        file = open(file_path, 'r')
        content = file.read()
        print(f"Content of '{file_path}': {content}")

        # Check if the file is closed
        if file.closed:
            print(f"File '{file_path}' is closed.")
        else:
            print(f"File '{file_path}' is open.")

        # Close the file explicitly
        file.close()

        # Check again after closing
        if file.closed:
            print(f"File '{file_path}' is closed.")
        else:
            print(f"File '{file_path}' is still open.")
    else:
        print(f"Error: File '{file_path}' not found.")

file_path =input("Enter a file to check it is closed or not!")
assess_file_closed(file_path)
