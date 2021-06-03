print("1: Add\n2: Subtract\n3: Multiply\n4: Divide")

n = int(input("Enter your choice : "))
a = int(input("Enter first operand : "))
b = int(input("Enter second operand : "))


if n == 1:
    print(f"A + B = {a+b}")

elif n == 2:
    print(f"A - B = {a-b}")

elif n == 3:
    print(f"A * B = {a*b}")

elif n == 4:
    print(f"A / B = {a/b}")
    
else:
    print("Wrong choice")
