"""Write a Python program to read a random line from a file."""


import random

def read_random(filename):
   with open(filename, 'r') as file:
            lines = file.readlines()

            if not lines:
                return "File is empty."

            return random.choice(lines).strip()


line = read_random("my_file.txt")
print(line)
