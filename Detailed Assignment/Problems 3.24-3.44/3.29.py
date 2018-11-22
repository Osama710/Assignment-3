print("Muhammad Osama - 18B-003-CS - Sec'A'")
print("Detailed Assignment")
print("Problem No: 3.29 ")

n = eval(input("Enter a positive integer: "))
print("The positive divisors of the number are: ")
for i in range(1,n+1):
    if (n%i == 0):
        print(i)
