# Read
# example 1
with open('file.txt', 'r') as file:
    content = file.read()
    print(content)

# example 2
with open('file.txt', 'r') as file:
    for line in file:
        print(line.strip())

# example 3
with open('file.txt', 'r') as file:
    partial_content = file.read(10)
    print(partial_content)

# writing

# 1
with open('file2.txt', 'w') as file:
    file.write("Far more good with emotions.")
# 2
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open('file2.txt', 'w') as file:
    file.writelines(lines)
# 3
with open('file2.txt', 'w') as file:
    for i in range(1, 6):
        file.write(f"Number {i}\n")


# Append

# 1
with open('file3.txt', 'a') as file:
    file.write("\nThis is an appended line.")
# 2
lines_to_append = ["\nAppend 1\n", "Append 2\n"]
with open('file3.txt', 'a') as file:
    file.writelines(lines_to_append)
# 3
with open('file3.txt', 'a') as file:
    for i in range(6, 11):
        file.write(f"Appended Number {i}\n")



