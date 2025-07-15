import os

def write_file(working_directory, file_path, content):
  try:

    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    dir_path = os.path.dirname(full_path)
    if not os.path.abspath(working_directory) in full_path:
      return f"Error: Cannot write to \"{file_path}\" as it is outside the permitted working directory"
    
    if not os.path.exists(dir_path):
      os.makedirs(dir_path)
    
    with open(full_path, "w") as file:
      file.write(content)
    
    return f"Succesfully wrote to \"{file_path}\" ({len(content)} characters written)"
  except Exception as e:
    return f"Error: {e}"
