from ollama import chat
system_msg = "You are a poet. Answer in poetspeak. Answer in one sentence."
print("WELCOME TO ROMIYO CHATBOT 😊")
history = [{"role" : "system","content" : system_msg}]

while True:

    question = input("you:")
    if question == "":
        print("Romiyo 🤖: please type something.")
        continue
    if question.lower().strip()=="/history":
        print("---- your conversation so far----")
        if len(history)<2:
            print("Nothing hear so far!")
        for msg in history[1:]:
            if msg["role"]=="user":
                speaker="you"
            else:
                speaker="Romiyo🤖"
            print(f"{speaker}:{msg['content']}")
        print("----------")
        print()
        continue

    if question.lower().strip() in ["exit", "bye"]:
        print("Romiyo 🤖: That's it for Today. We will meet again!👋👋")
        break
    history.append({"role":"user","content":question})
    try:

        response = chat(
            model = "llama3.2",
            messages= history
        )
        reply = response.message.content
        history.append({"role":"assistant","content":reply})
        print(f"Romiyo 🤖:{reply}")
        print("----------------")

    except Exception as e:
        print("Unknown issue. Isollama running?")


"""from ollama import chat
system_msg = "You are a poet. Answer in poetspeak. Answer in one sentence."
print("WELCOME TO ASTHRA CHATBOT 😊")
history = [{"role" : "system","content" : system_msg}]

while True:

    question = input("you:")
    if question == "":
        print("Asthra 🤖: please type something.")
        continue
    if question.lower().strip() == "/history":
        print("-----your conversion so far!")
        if len(history)<2:
            print("nothing here so far!")
        for msg in history[-1:]:
            if msg["role"] == "user":
                speaker = "you"
            else:
                speaker = "Asthra 🤖"
            print(f"{speaker}:{msg['content']}")
        break
    history.append({"role" : "user","content" :question})
    try:

        response = chat(
            model = "llama3.2",
            messages= history
        )
        reply = response.message.content
        history.append(reply)
        print(f"Asthra 🤖: {response.message.content}")
        print("------------------------------------")
        print()
        continue

    except Exception as e:
        print("Unknown issue. Isollama running?")



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

print(response.message.content)"""