from anthropic import Anthropic
from config import ANTHROPIC_API_KEY

client = Anthropic(api_key=ANTHROPIC_API_KEY)

PROMPT = """Likho ek fresh Hinglish motivation message, 4 se 6 chhoti lines mein.
Tone: brutally honest aur emotionally thoda painful, lekin abusive ya harmful bilkul nahi.
Har baar naya content likho, repeat mat karo.
End mein ek clear action likho jo main abhi turant karu.
Sirf message likho, koi intro ya explanation nahi."""


def generate_motivation() -> str:
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=300,
        messages=[{"role": "user", "content": PROMPT}],
    )
    return response.content[0].text.strip()


def run():
    from telegram_utils import send_message
    msg = generate_motivation()
    send_message(msg)


if __name__ == "__main__":
    run()
