# =========================
#       READING FILES
# =========================
# Reading files essentially is what the name suggests, however it consists of various modes
# 
# Modes: "r" → read, "w" → write, "a" → append, "x" → create

# Make sure the file "example.txt" exists in the same folder
file = open("example.txt", "r")

# Read entire file
content = file.read()
print("File content:\n", content)

file.close()

# Alternative: read line by line
with open("example.txt", "r") as f:
    for line in f:
        print("Line:", line.strip())
