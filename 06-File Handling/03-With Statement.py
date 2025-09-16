# ==========================
#      "WITH" STATEMENT
# ==========================

# The "with" statement automatically opens and closes files.
# Benefits:
#  - Cleaner syntax
#  - No need to call file.close()
#  - Safer (prevents resource leaks even if an error occurs)

# Example: Reading with "with"
with open("example.txt", "r") as f:
    content = f.read()
    print("File content:\n", content)

# Example: Writing with "with"
with open("example.txt", "w") as f:
    f.write("This file was written using the 'with' statement.\n")

# Example: Appending with "with"
with open("example.txt", "a") as f:
    f.write("This line was appended safely with 'with'.\n")

print("All operations done safely with 'with'!")

#-----------------------------

#   WITHOUT "with"

# Must manually close the file, risk of forgetting.
file = open("example.txt", "w")
file.write("Hello without with!\n")
file.close()  # If you forget this, file stays open (bad practice)

# ----------------------------

#   WITH "with"

# File automatically closes after the block ends — safer and cleaner.
with open("example.txt", "w") as f:
    f.write("Hello with 'with'!\n")

# No need to call f.close()
