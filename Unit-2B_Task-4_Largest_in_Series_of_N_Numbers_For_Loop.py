# Unit-2B_Task-4_Largest_in_Series_of_N_Numbers_For_Loop.py

n = int(input("Enter the number of values: "))

largest = float('-inf')

for i in range(1, n + 1):
    num = float(input(f"Enter number {i}: "))
    
    if num > largest:
        largest = num

print("Largest number =", largest)