# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a sample text file.\n")
    file.write("This file is created and written using Python.\n")
    file.write("You can write multiple lines to a file.\n")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)
