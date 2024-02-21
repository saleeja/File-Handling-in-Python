"""write a Python program to read an entire text file."""

# file_name = open("sample.txt", "r")
# content = file_name.read()
# print(content)
# file_name.close()

def read_file(file_path):
    file_name = open(file_path, "r")  # Open the file in read ('r') mode
    content = file_name.read()   # Read the entire content of the file
    file_name.close()   # Close the file after reading
 # Check if the content is empty
    if not content:
        print(f"File '{file_path}' is empty.")
    else:
        print(content)


file_path = "sample.txt"
read_file(file_path)
