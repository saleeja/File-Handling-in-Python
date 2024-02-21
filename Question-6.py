"""Write a Python program to read a random line from a file."""


import random

def read_random(filename):
   # Open the file in read ('r') mode
   with open(filename, 'r') as file:
            lines = file.readlines() # Read all lines from the file
  # Check if the file is empty
            if not lines:
                return "File is empty."
            # Select a random line from the list
            return random.choice(lines).strip()


line = read_random("my_file.txt")
print(line)
