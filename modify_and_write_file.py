def modify_and_write_file(input_filename, output_filename):
    """Reads a file, modifies its content, and writes to a new file."""
    try:
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Modify content (example: convert to uppercase)
        modified_content = content.upper()
        
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"Successfully wrote modified content to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file {input_filename} was not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing {input_filename}.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Example 
modify_and_write_file('original.txt', 'modified.txt')