def read_file_with_error_handling():
    """Asks user for filename and handles potential errors."""
    while True:
        filename = input("Enter the filename to read (or 'quit' to exit): ")
        
        if filename.lower() == 'quit':
            break
            
        try:
            with open(filename, 'r') as file:
                content = file.read()
            print("\nFile content:")
            print(content)
            break
            
        except FileNotFoundError:
            print(f"Error: The file '{filename}' doesn't exist. Please try again.")
        except PermissionError:
            print(f"Error: You don't have permission to read '{filename}'. Please try another file.")
        except UnicodeDecodeError:
            print(f"Error: Couldn't decode '{filename}'. It might be a binary file.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

read_file_with_error_handling()