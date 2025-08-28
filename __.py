def read_file(filename):
    try:
        with open(filename, 'r') as file:
            # Read and print line by line
            for line in file:
                print(line.strip())  # strip() removes extra spaces/newlines
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main Program
if __name__ == "__main__":
    read_file("sample.txt")
