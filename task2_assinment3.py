import math

# Step 1: Take input from the user
num = float(input("Enter a number: "))

# Step 2: Perform calculations using math module
# Square root
sqrt_val = math.sqrt(num)

# Natural logarithm (log base e)
# log() is only defined for positive numbers
if num > 0:
    log_val = math.log(num)
else:
    log_val = "Not defined for non-positive numbers"

# Sine of the number (in radians)
sine_val = math.sin(num)

# Step 3: Display results
print(f"\nResults for the number {num}:")
print(f"Square root: {sqrt_val}")
print(f"Natural logarithm: {log_val}")
print(f"Sine (in radians): {sine_val}")

