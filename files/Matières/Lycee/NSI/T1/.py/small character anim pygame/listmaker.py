def pause():
    input("Press enter to continue")


def append(namee, string):
    # Use context manager for safer file handling
    with open(f"result_{namee}.txt", "a") as f:
        f.write(f"{string}")


def clean(namee):
    # Clean the file by opening in write mode, this will overwrite the file
    with open(f"result_{namee}.txt", "w"):
        pass  # Just open and close to clear the content


def read(file, variable):
    try:
        # Use context manager to safely read the file
        with open(file, "r") as f:
            variable = f.read()
            print(variable)
        return variable
    except FileNotFoundError:
        print(f"Sorry, couldn't find the file {file}")
        print("Ending program")
        pause()
        exit(1)  # Exit the program if file is not found
    except Exception as e:
        print(f"An error occurred: {e}")
        pause()
        exit(1)


w = """ """
namee = ""
variable = ""
list = []
namegiven = False
liiste = []
# path="img/right_character/img"
path = "img/The unknown thing/exported"
image = ""

# Get the file name to read
fileOriginName = input("Please specify the name of the file to read: ")
variable = read(fileOriginName, variable)

imageName = input("Name the variable that will contain the image: ")
for file in variable:
    if file != '\n':
        image += file
    else:
        list.append(f"{path}/{image}")
        if not namegiven:
            namee = image
            namegiven = True
        image = ""

clean(namee)
append(namee, w)
finalList = []
finalListPure = []
for index, item in enumerate(list):
    finalList.append(f"{imageName}{index+1}=\"{item}\"")
    finalList.append(f"\"{item}\"")
    # finalListPure.append(f"{imageName}{index+1}")
    append(namee, f"{imageName}{index+1}=\"{item}\"\n")

append(namee, f"{imageName}={finalList}")
print(w)
print(f"{imageName}={finalList}")
print(f"Work finished, find the result in the file : result_{namee}.txt")
print("(c) Program created by Henry Letellier")
pause()
