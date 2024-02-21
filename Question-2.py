"""Write a Python program to read first n lines of a file."""

# my_file = open("sample.txt", "r") 
# print(my_file.read(10))


def read_n_characters(file_path, num_chars):
    my_file = open(file_path, "r")
    content = my_file.read(num_chars)
    print(content)
    my_file.close()

    if not content:
        print(f"File '{file_path}' is empty.")
    else:
        print(content)

# Get user input for file path and number of characters
file_path = input("Enter the file path: ")
num_characters = int(input("Enter the number of characters to read: "))

read_n_characters(file_path, num_characters)
