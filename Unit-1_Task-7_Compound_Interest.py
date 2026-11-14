# Program to calculate Compound Interest

principal = float(input("Enter the Principal Amount: "))
rate = float(input("Enter the Rate of Interest (%): "))
time = float(input("Enter the Time (years): "))

amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal

print("Compound Interest =", compound_interest)
print("Total Amount =", amount)