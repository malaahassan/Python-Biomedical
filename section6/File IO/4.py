with open('example.txt', 'r') as file:
    file_content = file.read().split("\n")
    file_content = file_content[50:61]
    for line in file_content:
        print(line)