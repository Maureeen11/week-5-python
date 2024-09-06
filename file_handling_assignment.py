def create_file():
    try:
        with open('my_file.txt', 'w') as file:
            # Write a string to the file
            file.write("This is a sample text.\n")
            
            # Write a tuple (formatted as text) to the file
            file.write("Tuple: (1, 'apple', 3.14)\n")
            
            # Write some numbers to the file
            file.write("Numbers: 42, 56, 78\n")
            
        print("File created and written successfully.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}")
    finally:
        print("File creation block executed.")

def read_file():
    try:
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}")
    finally:
        print("File reading block executed.")

def append_to_file():
    try:
        with open('my_file.txt', 'a') as file:
            # Append additional lines
            file.write("Appending a new string.\n")
            file.write("Appending a new tuple: (2, 'banana', 6.28)\n")
            file.write("Appending more numbers: 99, 101, 202\n")
            
        print("File appended successfully.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}")
    finally:
        print("File appending block executed.")

if __name__ == "__main__":
    create_file()    # Create and write to the file
    read_file()      # Read and display the file content
    append_to_file() # Append more lines to the file
    read_file()      # Read and display the file content again to show the appended lines
