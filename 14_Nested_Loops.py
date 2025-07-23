# =========================
#       NESTED LOOPS
# =========================
# A nested loop is simply one loop running inside another.
# The inner loop will complete ALL of its iterations for each single iteration of the outer loop.

# Example: Multiplication Table (1 to 3)
for x in range(1, 4):         # Outer loop
    for y in range(1, 4):     # Inner loop
        print(f"{x} x {y} = {x * y}")
    print("---------")  # Separator for readability

# What happens here:
# - Outer loop runs 3 times (x = 1, 2, 3)
# - For each value of x, the inner loop runs fully (y = 1, 2, 3)
