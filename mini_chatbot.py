from ollama import chat
question=input("Ask a question:")
response = chat(
    model="llama3.2",
    messages = {
        {
            "role" : "user",
            "content" : question
        }
    }
)

print(response.message.content)