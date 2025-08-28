def write_and_append_file(filename):
    try:
        # Step 1: Write user input to the file
        text = input("Enter text to write to the file: ")
        with open(filename, 'w') as file:
            file.write(text + "\n")
        print(f"Data successfully written to {filename}.")

        # Step 2: Append additional data
        additional_text = input("Enter additional text to append: ")
        with open(filename, 'a') as file:
            file.write(additional_text + "\n")
        print("Data successfully appended.")

        # Step 3: Read and display the final content
        print("\nFinal content of output.txt:")
        with open(filename, 'r') as file:
            print(file.read())

    except Exception as e:
        print(f"An error occurred: {e}")


# Main Program
if __name__ == "__main__":
    write_and_append_file("output.txt")
