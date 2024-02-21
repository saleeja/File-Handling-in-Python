"""Write a Python program to write a list to a file."""

def write_list_to_file(filename, data):
  
  with open(filename, 'w') as file:
    for item in data:
      file.write(str(item) + "\n")  # Convert items to strings and add newline
    print(f"Successfully wrote items to '{filename}'.")


data = [1, 2, 3, "hello"]
write_list_to_file("my_file.txt", data)
