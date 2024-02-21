"""Write a Python program to read a file line by line store it into a variable."""

def file_read(file_name):
        with open (file_name, "r") as myfile:
                data=myfile.readlines()
                if not data:
                        print(f"Error: File '{file_name}' is empty.")
                else:
                        print(data)
               
file_read('sample.txt')