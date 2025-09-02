# Program to open and read sample.txt line by line

try:
    # Open the file in read mode
    with open("sample.txt", "r") as file:
        # Loop through each line and print it
        for line in file:
            print(line.strip())  # strip() removes extra spaces/newlines

except FileNotFoundError:
    print("⚠️ The file 'sample.txt' was not found.")
