"""Write a Python program to copy the contents of a file to another file."""

def copy_file(file_to_copy, copied_file):
    source_content = ""

    # Read the content from the source file
    file_to_copy_obj = open(file_to_copy, 'r')
    source_content = file_to_copy_obj.read()
    file_to_copy_obj.close()

    # Write the content to the destination file
    copied_file_obj = open(copied_file, 'w')
    copied_file_obj.write(source_content)
    copied_file_obj.close()

    print(f"Contents of '{file_to_copy}' copied to '{copied_file}' successfully.")

file_to_copy_path = input("Enter a file name need to copy:")
copied_file_path = input("where to copy this file:")

copy_file(file_to_copy_path, copied_file_path)



# another method
# import shutil

# def copy_file_shutil(file_to_copy, dst_filename):
 
#   shutil.copyfile(file_to_copy, dst_filename)

# copy_file_shutil("sample.txt", "destination.txt")
