import google.generativeai as genai

# API setup
API_KEY = "AIzaSyD1Ul9w5hzeNFQSN3l3fbZTlXAtnBeqlaY"
genai.configure(api_key=API_KEY)

# Model
MODEL_NAME = "models/gemini-1.5-flash-latest"
sol = genai.GenerativeModel(model_name=MODEL_NAME)
luna = genai.GenerativeModel(model_name=MODEL_NAME)

# Start chats
chat_sol = sol.start_chat()
chat_luna = luna.start_chat()

# Debate topic
topic = "What is Github"

print(f"\n⚖️ Starting AI Debate on: {topic}\n")

# Initial prompt to Sol
opening_prompt = (
    f"Debate Topic: {topic}\n\n"
    f"You're Sol, a logical, fact-driven AI. You must sometimes agree to Luna for valid facts, but yet try to disprove Luna's statement."
    f"Start with a strong opening argument supporting your stance. Your goal is to disprove Luna's position using logic, examples, and critical analysis."
)
msg = chat_sol.send_message(opening_prompt)
print(f"🧠 Sol: {msg.text.strip()}\n")

# Debate loop
turns = 20
for i in range(turns):
    if i % 2 == 0:
        # Luna's turn
        responder = chat_luna
        name = "🌙 Luna"
        persona = (
            "You're Luna, a cautious, empathetic AI who opposes Sol’s stance. "
            "Respond by directly challenging Sol's logic, but agree to sol's valid logics"
        )
    else:
        # Sol's turn
        responder = chat_sol
        name = "🧠 Sol"
        persona = (
            "You are a smart person who is very intellectual on many topics, but opposes luna in many ways. "

        )

    prompt = f"{persona}\n\nOpponent's Argument:\n{msg.text.strip()}"
    msg = responder.send_message(prompt)
    print(f"{name}: {msg.text.strip()}\n")

# Closing statements
closing_sol = chat_sol.send_message(
    "You're Sol. Provide a concise and logical closing for the above conversation"
)
closing_luna = chat_luna.send_message(
    "You're Luna. Provide a thoughtful, and generate a closing for the above conversation, try to agree to sol but only the valid points"
)

print(f"🧠 Sol (Closing): {closing_sol.text.strip()}\n")
print(f"🌙 Luna (Closing): {closing_luna.text.strip()}\n")
