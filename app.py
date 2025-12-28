import gradio as gr
import random

def chat(message, history):
    responses = [
        "🎤 **Voice AI Assistant** running locally!",
        "💻 **GitHub**: github.com/swaveelfayaz/voice-ai-assistant",
        "🔊 **Local Demo**: Mic → Speech-to-Text → Llama 3.2 → Voice",
        "📱 **Setup**: `pip install -r requirements.txt` + `ollama pull llama3.2:1b`",
        "🚀 **Portfolio**: Real-time voice AI pipeline built in VS Code"
    ]
    return random.choice(responses)

demo = gr.ChatInterface(
    chat,
    title="🤖 Voice AI Assistant",
    description="**Real-time voice demo on GitHub** 👇\nMic → Speech-to-Text → Llama 3.2 → Text-to-Speech"
)

if __name__ == "__main__":
    demo.launch()
