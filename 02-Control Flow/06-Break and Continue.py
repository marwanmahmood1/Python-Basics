# ==========================
#      BREAK & CONTINUE
# ==========================
# Loops usually run until their condition is no longer true.
# But sometimes, we need to control the loop ourselves:
# - break → stops the loop completely.
# - continue → skips the rest of the current loop iteration and moves to the next one.

# --- break example ---
for number in range(1, 10):
    if number == 5:
        print("Breaking at number 5")
        break  # Loop stops here
    print("Number:", number)

print("Loop ended with break\n")

# --- continue example ---
for number in range(1, 6):
    if number == 3:
        print("Skipping number 3")
        continue  # Skip this iteration and move to the next
    print("Number:", number)

print("Loop ended with continue")
