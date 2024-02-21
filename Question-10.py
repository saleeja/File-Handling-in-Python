"""Write a Python program to create a file where all letters of English alphabet are listed by specified number of letters on each line."""


def create_letter_file(filename, letters_per_line):
# Open the file in write ('w') mode using the with statement
  with open(filename, 'w') as file:
    alphabet = "abcdefghijklmnopqrstuvwxyz" # Define the alphabet
    start_index = 0      #

    if letters_per_line > len(alphabet):
            print("Error: Number of letters per line exceeds the length of the alphabet.")
    else:
    # Iterate through the alphabet
        while start_index < len(alphabet):
            end_index = min(start_index + letters_per_line, len(alphabet))
            line = alphabet[start_index:end_index] + "\n"
            file.write(line)
            start_index = end_index
        print(f"File '{filename}' created with {letters_per_line} letters per line.")


filename = "letters.txt"
# get user input
letters_per_line =int(input("enter number of letters on each line:"))
create_letter_file(filename, letters_per_line)

