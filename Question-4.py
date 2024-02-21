"""Write a Python program to read a file line by line store it into a variable."""

def file_read(file_name):
        # Open the file in read ('r') mode using the with statement
        with open (file_name, "r") as myfile:
                data=myfile.readlines()   # Read all lines from the file into a list
                if not data:
                        print(f"Error: File '{file_name}' is empty.")  # Check if the file is empty
                else:
                        print(data)
               
file_read('sample.txt')