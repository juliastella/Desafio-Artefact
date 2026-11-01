from google import genai
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
for modelo in client.models.list():
    print(modelo.name)
