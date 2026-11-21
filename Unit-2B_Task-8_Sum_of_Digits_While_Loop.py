# Unit-2B_Task-8_Sum_of_Digits_While_Loop.py

num = int(input("Enter a number: "))

sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num //= 10

print("Sum of digits =", sum_digits)