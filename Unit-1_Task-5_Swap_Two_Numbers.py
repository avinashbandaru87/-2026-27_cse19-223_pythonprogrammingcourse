# Program to swap two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Before Swapping:")
print("First Number =", num1)
print("Second Number =", num2)
num1, num2 = num2, num1
print("After Swapping:")
print("First Number =", num1)
print("Second Number =", num2)