# ==========================
#       WRITING FILES
# ==========================

# Similar to Reading Files, there are writing modes:
# "w" → Write (overwrites the file if it exists, creates if not)
# "a" → Append (adds new content at the end of file, creates if not)
# "x" → Create (creates a new file, gives error if file already exists)

# Example: Writing (overwriting the file)
with open("example.txt", "w") as f:
    f.write("This will overwrite any existing content.\n")
    f.write("Hello, world!\n")

# Example: Appending (adding content to the end of the file)
with open("example.txt", "a") as f:
    f.write("This line will be added at the end.\n")

# Example: Creating a new file (will raise an error if it already exists)
# Uncomment to test
# with open("new_file.txt", "x") as f:
#     f.write("This file is created fresh and will error if run again.\n")

print("File writing completed!")
