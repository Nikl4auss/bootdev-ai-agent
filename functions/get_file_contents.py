import os

def get_file_contents(working_directory, file_path):
  try:
    full_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not os.path.abspath(working_directory) in full_path or file_path.startswith(".."):
      return f"Error: Cannot read \"{file_path}\" as it is outside the permitted working directory"

    if not os.path.isfile(full_path):
      return f"Error: File not found or is not a regular file: \"{file_path}\""

    with open(full_path, "r") as file:
      file_contents = file.read(10000)

      if len(file_contents) == 10000:
        file_contents += f"[...File \"{ file_path}\" truncated at 10000 characters]."
      return f"{file_contents}"
  except Exception as e:
    return f"Error: {e}"
  
print(get_file_contents("calculator", "lorem.txt"))