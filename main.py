from ollama import chat
from ollama import ChatResponse

response: ChatRespone = chat(model="llama3:latest",messages=[{
    'role':'user',
    'content':'wwhy is the sky blue?',
},])

print(response['message']['content'])
