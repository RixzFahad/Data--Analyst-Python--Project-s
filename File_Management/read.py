# Reading a File

file = open('Candy.txt', 'r')
content = file.read()
file.close()
print(f"Sample of Candy.txt:\n{content}")