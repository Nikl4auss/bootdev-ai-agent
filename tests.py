from functions.get_files_info import get_files_info
from functions.get_file_contents import get_file_contents
from functions.write_file import write_file
from functions.run_python_file import run_python_file

print("calculator/main.py")
print(run_python_file("calculator", "main.py"))
print("calculator/tests.py")
print(run_python_file("calculator", "tests.py"))
print("calculator/..main.py")
print(run_python_file("calculator", "../main.py"))
print("calculator/nonexistent.py")
print(run_python_file("calculator", "nonexistent.py"))