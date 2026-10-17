num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("ID of num1:", id(num1))
print("Hex of num1:", hex(num1))

print("ID of num2:", id(num2))
print("Hex of num2:", hex(num2))

num3 = num1 + num2
print("Addition:", num3)

num4 = num1 - num2
print("Subtraction:", num4)

num5 = num1 * num2
print("Multiplication:", num5)

if num2 != 0:
    num6 = num1 // num2
    print("Division:", num6)
else:
    print("Cannot divide by zero")

print("ID of addition:", id(num3))
print("Hex of addition:", hex(num3))

print("ID of subtraction:", id(num4))
print("Hex of subtraction:", hex(num4))

print("ID of multiplication:", id(num5))
print("Hex of multiplication:", hex(num5))



