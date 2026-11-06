import os

from openai import OpenAI

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    print("Error: OPENROUTER_API_KEY IS NOT SET.")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

messages = [
    {
        "role": "system",
        "content": "You are a helpful and friendly AI assistant."
    }
]


print("=" * 35)
print(" Simple AI Chatbot")
print("=" * 35)
print("Type 'exit' or 'quit' to stop.\n")

while True:

    try:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("\nBot: Goodbye!")
            break

        if not user_input:
            continue

        messages.append({
            "role": "user",
            "content": user_input
        })

        response = client.chat.completions.create(
            model = "openrouter/free",
            messages = messages
        )

        reply = response.choices[0].message.content

        messages.append({
            "role": "assistant",
            "content": reply
        })

        print(f"\nBot: {reply}\n")

    except KeyboardInterrupt:
        print("\n\nBot: Goodbye!")
        break

    except Exception as e:
        print(f"\nError: {e}\n")
