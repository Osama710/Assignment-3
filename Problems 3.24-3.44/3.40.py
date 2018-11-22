print("Muhammad Osama - 18B-003-CS - Sec'A'")
print("Detailed Assignment")
print("Problem No: 3.40 ")

def partition(lst):
    for x in lst:
        x.casefold()
        if x[1] in "abcdefghijklm":
            print(x)
