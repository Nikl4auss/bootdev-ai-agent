import os
from google.genai import types

def get_files_info(working_directory, directory=None):
  try:

    full_path = os.path.abspath(os.path.join(working_directory, directory))

    if not os.path.abspath(working_directory) in full_path or directory.startswith(".."):
      return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"

    if not os.path.isdir(full_path):
      return f"Error: \"{directory}\" is not a directory"
    
    formated_output = ""
    for item in os.listdir(full_path):
      item_path = f"{full_path}/{item}"
      is_dir = os.path.isdir(item_path)
      file_size = os.path.getsize(item_path)
      formated_output += f"{item}: file_size={file_size} bytes, is_dir={is_dir}\n"

    return formated_output
  except Exception as e:
    return f"Error: {e}"
  
schema_get_files_info = types.FunctionDeclaration(
  name="get_files_info",
  description="List files in the directory along with their sizes, constrainted to the working directory",
  parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
      "directory": types.Schema(
        type=types.Type.STRING,
        description="The directory to list the files from, relative to the working directory"
      )
    }
  )
)