# File Creation
try:
    # Open a new file in write mode
    with open('my_file.txt', 'w') as file:
        # Write three lines of text to the file
        file.write('Hello, World!\n')
        file.write('This is a mix of strings and numbers: 12345\n')
        file.write('Python is fun!\n')

    # File Reading and Display
    # Open the file in read mode
    with open('my_file.txt', 'r') as file:
        # Read the contents of the file
        content = file.read()
        # Display the contents on the console
        print(content)

    # File Appending
    # Open the file in append mode
    with open('my_file.txt', 'a') as file:
        # Append three additional lines of text to the existing content
        file.write('Let\'s append some more text.\n')
        file.write('Here\'s another line.\n')
        file.write('And one more for good measure.\n')

    # Re-display the file content after appending
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print('The file was not found.')
except PermissionError:
    print('You do not have permission to access this file.')
except Exception as e:
    print(f'An error occurred: {e}')
finally:
    print('File handling operations are complete.')
