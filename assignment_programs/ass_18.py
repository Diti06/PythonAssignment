# How to check file is empty or not

import os

def is_file_empty(file_path):
    return os.path.getsize(file_path) == 0


file_path = r"C:\Users\DITI\PycharmProjects\pythonProject\assignment_programs\Example_file.txt"
if is_file_empty(file_path):
    print(f"The file is empty.")
else:
    print(f"The file is not empty.")