import openai
import os

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_change(old, new):
    prompt = f"""
Compare the two versions of the API documentation below. Highlight key changes relevant for developers (e.g., limit changes, deprecations, new endpoints).

Old:
{old}

New:
{new}

Respond in bullet points. Bold critical info.
"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return response.choices[0].message.content
    except openai.RateLimitError as e:
        print("Rate limit exceeded. Please check your quota and try again later.")
        return "Rate limit exceeded."
    except openai.OpenAIError as e:
        print(f"OpenAI API error: {e}")
        return "API error occurred."
    except Exception as e:
        print(f"Unexpected error: {e}")
        return "Unexpected error occurred."