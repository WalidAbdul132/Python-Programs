x = int(input("Please enter the first int number "))
x2 = int(input("Please enter the second int number "))

if x2 < x:
    print("wrong number...")
else:
    print("The numbers from", x, "to", x2, "are". format(x, x2))

for i in range(x + 1, x2, 1):
    print(i, end=' ')
