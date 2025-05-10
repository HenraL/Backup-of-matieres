import os

# Define the directory where the files are located, this ensures we are not accessing files from unintended locations
file_directory = "path_to_your_directory"  # Change this to your desired directory

# Ensure the directory is safe by checking if the path is inside the intended directory
def is_safe_file(file_name):
    return os.path.commonpath([file_directory, os.path.abspath(file_name)]) == file_directory

a = os.listdir(file_directory)
column = 0

# Progress input
progress = input("Do you wish to activate the info on the progress of the program? [(y)es/(n)o]").lower()

for i in range(len(a)):
    print("{} {}\t".format(i, a[i]), end="")
    if column == 2:
        column = 0
        print()
    column += 1

# File selection input
b = int(input("\nEnter the index of the file to convert into a database:"))
c = os.path.join(file_directory, a[b])

# Check if file is safe to open
if not is_safe_file(c):
    print(f"Warning: The file '{c}' is not inside the allowed directory!")
    exit(1)

if progress == "y":
    print("Extracting the raw data from the file {}".format(c))

# Open and read file
with open(c, "r") as f:
    d = f.read()

if progress == "y":
    print("Data Extracted")

# Character input
e = input("Enter the character between the term and definition:")
f = input("Enter the character between each term/definition (enter ret to insert a python return '\\n'):")

# Convert 'ret' to newline
if f == "ret":
    f = "\n"

word = ""
word2 = ""
temp = ""
liste = []
A = 0
index = 0

# Processing data
if progress == "y":
    print("Processing the data of the file", end="")

for i in d:
    if i == f and A == 1:
        word2 = temp
        liste.append({"index": index, "term": word, "definition": word2})
        word = word2 = temp = ""
        A = 0
        index += 1
        if progress == "y":
            print(".", end="")
    elif i == e and A == 0:
        word = temp
        temp = ""
        A = 1
    else:
        temp += str(i)

if progress == "y":
    print("[Done]")

liste.append({"index": index, "term": "Created by", "definition": "Henry Letellier"})

# File output options
j = input("Enter 0 to just write the list to a file.\nEnter 1 to specify a specific character to put between the term and definitions:")
g = input("Enter the name of the file to write the results to:")
h = input("Enter the file extension (no . required):")

# Writing the data to a file
if j == "0":
    i = input("Enter the name of the list containing the processed data:")
    if progress == "y":
        print("List length={}\nWriting the processed data to the given file".format(len(liste)), end="")

    output_path = os.path.join(file_directory, f"{g}.{h}")
    with open(output_path, "w") as f:
        f.write("{}=[".format(i))
        for item in liste:
            f.write("{}".format(item))
            if progress == "y":
                print(".", end="")
        f.write("]")

    print("[Done]")
    if progress == "y":
        print("Data written")
else:
    k = input("Enter ret to insert a python return '\\n'\nEnter the character to insert between the term and the definition:")
    l = input("Enter ret to insert a python return '\\n'\nEnter the character to insert between each term/definition:")
    m = input("Do you wish to write the index for each line? [(y)es/(n)o]:").lower()

    if k.lower() == "ret":
        k = "\n"
    if l.lower() == "ret":
        l = "\n"

    if progress == "y":
        print("List length={}\nWriting the processed data to the given file".format(len(liste)), end="")

    output_path = os.path.join(file_directory, f"{g}.{h}")
    with open(output_path, "w") as f:
        if m == "n":
            for item in liste:
                f.write(f"{item['term']}{k}{item['definition']}{l}")
                if progress == "y":
                    print(".", end="")
        else:
            for item in liste:
                f.write(f"{item['index']}{k}{item['term']}{k}{item['definition']}{l}")
                if progress == "y":
                    print(".", end="")

    if progress == "y":
        print("[Done]")

print("Finished")
print("Created by Henry Letellier")
