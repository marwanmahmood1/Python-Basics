# ==========================
#       READING FILES
# ==========================
# Reading files essentially is what the name suggests, however it consists of various modes:

# "r" → READ (default): Opens the file for reading. (Returns error if the file does not exist)
# "w" → WRITE: Creates a new file or overwrites an existing file.
# "a" → APPEND: Opens the file for writing, but adds new content at the end instead of overwriting.
# "x" → CREATE: Creates a new file. Error if the file already exists.

# (Always make sure the file exists when using "r")

# Example: Open a file in read mode
file = open("example.txt", "r")

# Read entire file
content = file.read()
print("File content:\n", content)

file.close()

# Alternative: read line by line (preferred with 'with' because it auto-closes the file)
with open("example.txt", "r") as f:
    for line in f:
        print("Line:", line.strip())
