from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename agian:")
file_again = input("> ")

text_again = open(file_again)

print(text_again.read())
