from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("AIzaSyAnYLhZMbUAutIOKdsXgJKsUl_Rr6ZxZrM")
)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="What is if else statement?"
)

print(response.text)
print("This is the end of the test file.")
print("this is only a test file to check if the API key is working and if the response is being received correctly.")
