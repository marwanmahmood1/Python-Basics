# ======================
#      WHILE LOOPS
# ======================

# As long as a condition specified by the user remains true, while loops would keep going until the condition is no longer satisfied.

count = 5

while count > 0:
    print("Countdown:", count)
    count -= 1  # Decrement the count by 1 after each loop iteration

print("Liftoff!")  # Printed when the loop ends


# As such, if a condition has no way of becoming false, it would result in an INFINITE LOOP:

# while True:
# print("This loop never ends!")
