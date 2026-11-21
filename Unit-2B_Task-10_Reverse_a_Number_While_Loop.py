# Unit-2B_Task-10_Reverse_a_Number_While_Loop.py

num = int(input("Enter a number: "))

reverse = 0
temp = num

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

print("Reversed number =", reverse)