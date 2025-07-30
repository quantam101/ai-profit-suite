import os
import openai
from fpdf import FPDF
from datetime import datetime

# Read API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Prompt for the AI
prompt = (
    "Generate a self-improvement learning prompt for the day. "
    "Include 1 paragraph of motivation, 1 actionable tip, and 1 reflective question."
)

# Call OpenAI
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a motivational life coach."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=500,
    temperature=0.7
)

# Extract the response text
message = response['choices'][0]['message']['content']

# Prepare the output directory
os.makedirs("output", exist_ok=True)
filename = f"output/daily_prompt.pdf"

# Generate PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt=f"📅 AI Daily Prompt - {datetime.now().strftime('%Y-%m-%d')}

{message}")

# Save PDF
pdf.output(filename)

print(f"✅ Prompt generated and saved to {filename}")
