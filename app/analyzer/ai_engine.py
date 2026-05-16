import ollama

from app.analyzer.prompt_builder import build_prompt


def analyze_alert(alert):

    print("Starting AI analysis...")

    prompt = build_prompt(alert)

    try:

        response = ollama.chat(
            model='mistral',
            messages=[
                {
                    'role': 'user',
                    'content': prompt
                }
            ]
        )

        print("AI response received.")

        return response['message']['content']

    except Exception as e:

        print(f"AI ERROR: {e}")

        return "AI analysis failed."
    