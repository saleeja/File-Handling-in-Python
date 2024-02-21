"""Write a Python program to append text to a file and display the text."""

# # Open the file in append mode
# file = open('sample.txt', 'a')
# #Append content to the file
# file.write('\n This is a new line of text.')

# # Close the file
# file.close()


def append_and_display(filename, text):
  # Open the file in append ('a') m
  with open(filename, 'a') as file:
    file.write(text + "\n")  # Append the provided text to the file
    print(f"Appended text: {text}")
# Open the file in read ('r') mode
  with open(filename, 'r') as file:
    content = file.read()
    print(f"\nContents of {filename}:")
    print(content)


filename = "my_file.txt"
text_to_append = input("Enter text to add:")
append_and_display(filename, text_to_append)

    


