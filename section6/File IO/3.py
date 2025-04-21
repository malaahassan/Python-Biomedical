with open('example.txt', 'a') as file:
    file.write("\n")
    for i in range(1, 101):
        file.write(f"{i}\n")
