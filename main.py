import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types 
from functions.get_files_info import schema_get_files_info

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def main():
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info
        ]
    )
    
    if len(sys.argv) < 2:
        print("Error: An user prompt was expected")
        exit(code=1)
    
    system_prompt = """
    You are a helpful AI coding agent.
    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:
    - List files and directories
    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """
    user_prompt = sys.argv[1]
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt, tools=[available_functions])
        )
    if isinstance(response.function_calls, list):
        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
    print(response.text)
    if len(sys.argv) > 2:
        if sys.argv[2] == "--verbose":
            print(f"User prompt: {user_prompt}\nPrompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")

    
if __name__ == "__main__":
    main()
