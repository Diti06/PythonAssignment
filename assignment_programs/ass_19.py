# Read line number 4 from the given file.

import linecache

file_path = r"C:\Users\DITI\PycharmProjects\pythonProject\assignment_programs\Example_file.txt" #using raw strings
#the raw string tells Python not to interpret any escape sequences within the string
line_number = 4

try:
    line = linecache.getline(file_path, line_number)
    if line:
        print(f"Line {line_number}: {line}")
    else:
        print(f"Line {line_number} does not exist in the file.")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")