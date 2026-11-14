# Program to calculate Simple Interest
principal = float(input("Enter the Principal Amount: "))
rate = float(input("Enter the Rate of Interest (%): "))
time = float(input("Enter the Time (years): "))
simple_interest = (principal * rate * time) / 100
print("Simple Interest =", simple_interest)