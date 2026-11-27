# Unit-1_Task-15_Type_Conversion.py

num_int = 10
num_float = 5.5
num_str = "25"

# Type Conversion
float_value = float(num_int)
int_value = int(num_float)
string_to_int = int(num_str)

print("Original Integer:", num_int, "Type:", type(num_int))
print("Converted to Float:", float_value, "Type:", type(float_value))

print("Original Float:", num_float, "Type:", type(num_float))
print("Converted to Integer:", int_value, "Type:", type(int_value))

print("Original String:", num_str, "Type:", type(num_str))
print("Converted to Integer:", string_to_int, "Type:", type(string_to_int))
