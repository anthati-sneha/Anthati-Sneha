from ollama import chat
response = chat(
    model = "llama 3.2",
    messege=[
        {
            "role" : "user",
            "content" : "write me a whatsapp message to my friend geetha asking her to meet me at the bus stop .keep the answer under 2 lines."
        }
    ]
)
print(response.message.content)