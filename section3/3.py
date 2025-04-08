s = "Tom Jerry Harry"
s1 = list(enumerate(sorted(s.split())))
s2 = ""
for i, elem in s1:
     s2 += elem + ", " if i < len(s1) - 1 else elem
print(s2)
