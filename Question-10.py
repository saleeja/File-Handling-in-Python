"""Write a Python program to create a file where all letters of English alphabet are listed by specified number of letters on each line."""


def create_letter_file(filename, letters_per_line):
  """
  Creates a file where all letters of the English alphabet are listed
  by the specified number of letters on each line.

  Args:
      filename (str): The name of the file to create.
      letters_per_line (int): The number of letters to write on each line.
  """
  with open(filename, 'w') as file:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    start_index = 0
    while start_index < len(alphabet):
      end_index = min(start_index + letters_per_line, len(alphabet))
      line = alphabet[start_index:end_index] + "\n"
      file.write(line)
      start_index = end_index

# Example usage
filename = "letters.txt"
letters_per_line =int(input("enter number of letters on each line:"))
create_letter_file(filename, letters_per_line)
print(f"File '{filename}' created with {letters_per_line} letters per line.")
