import os
import subprocess
def run_python_file(working_directory, file_path):
    try:
      full_path = os.path.abspath(os.path.join(working_directory, file_path))

      if not os.path.abspath(working_directory) in full_path or file_path.startswith(".."):
        return f"Error: Cannot execute \"{file_path}\" as it is outside the permitted working directory"

      if not os.path.isfile(full_path):
        return f"Error:File \"{file_path}\" not found"
      
      if not full_path.endswith(".py"):
         return f"Error: \"{file_path}\" is not a Python file."
      
    except Exception as e:
       return f"Error: {e}"
    
    try:
       
      result = subprocess.run(args=["python3", full_path], timeout=30, capture_output=True, text=True)
      
      output = ""
      
      if len(result.stdout) == 0 and len(result.stderr):
         return "No output produced"
      output += f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}"
      
      if result.returncode != 0:
         output += f"\nProcess exited with code: {result.returncode}"
      
      return output
    except Exception as e:
       return f"Error: executing Pyton file: {e}"
    
print(run_python_file(".", "main.py"))