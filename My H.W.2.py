# Program to write, append, and read from output.txt

# Step 1: Take user input and write to file
data = input("Enter some text to write into the file: ")
file = open("output.txt", "w")   # open in write mode
file.write(data + "\n")
file.close()
print("✅ Data written to output.txt")

# Step 2: Append additional data
extra = input("Enter additional text to append: ")
file = open("output.txt", "a")   # open in append mode
file.write(extra + "\n")
file.close()
print("✅ Additional data appended to output.txt")

# Step 3: Read and display the final content
print("\n📄 Final content of output.txt:")
file = open("output.txt", "r")   # open in read mode
for line in file:
    print(line.strip())
file.close()
