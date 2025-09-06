# =========================
#     BUILT-IN MODULES
# =========================
# Python has many built-in modules to handle common tasks.

import random
import datetime
import os

# --- random module ---
print("Random integer (1–100):", random.randint(1, 100))
print("Random choice from list:", random.choice(["apple", "banana", "cherry"]))

# --- datetime module ---
today = datetime.date.today()
print("Today's date:", today)

now = datetime.datetime.now()
print("Current time:", now.strftime("%H:%M:%S"))

# --- os module ---
print("Current working directory:", os.getcwd())
print("List of files in current dir:", os.listdir("."))
