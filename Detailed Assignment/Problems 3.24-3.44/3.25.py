print("Muhammad Osama - 18B-003-CS - Sec'A'")
print("Detailed Assignment")
print("Problem No: 3.25 ")

name = eval(input("Enter studnts names: "))
name.casefold()
sel_name = []
for student in name:
    if student.startswith(tuple('ABCDEFGHIJKLM')):
        sel_name.append(student)
sel_name.sort()
print(*sel_name,sep = '\n')
