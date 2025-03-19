with open("file1.txt") as file1:
    line_file1 = file1.readlines()
line_file1 = [line.strip() for line in line_file1]


with open("file2.txt") as file2:
    line_file2 = file2.readlines()
line_file2 = [line.strip() for line in line_file2]

common_element = [str for str in line_file1 if str in line_file2]

print(line_file1)
print(line_file2)
print(common_element)
