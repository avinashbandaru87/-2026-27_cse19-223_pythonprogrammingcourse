# Unit-2B_Task-3_Sum_and_Average_of_N_Numbers_For_Loop.py

n = int(input("Enter the number of values: "))

total = 0

for i in range(1, n + 1):
    num = float(input(f"Enter number {i}: "))
    total += num

average = total / n

print("Sum =", total)
print("Average =", average)