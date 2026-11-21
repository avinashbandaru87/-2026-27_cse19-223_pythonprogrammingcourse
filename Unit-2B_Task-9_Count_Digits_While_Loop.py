# Unit-2B_Task-9_Count_Digits_While_Loop.py

num = int(input("Enter a number: "))

count = 0

if num == 0:
    count = 1
else:
    while num != 0:
        count += 1
        num //= 10

print("Number of digits =", count)