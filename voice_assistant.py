import speech_recognition as sr
import ollama
import pyttsx3


def listen():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening... (Speak now)")
            # Adjust for background noise
            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            # Capture audio from mic
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("Processing...")

        # Convert speech to text using Google STT
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text

    except sr.WaitTimeoutError:
        print("No speech detected (timeout).")
        return None
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return None
    except sr.RequestError:
        print("Speech recognition service unavailable.")
        return None
    except Exception as e:
        print(f"Listen error: {e}")
        return None


def think(text: str):
    if not text:
        return None

    print("Thinking...")
    try:
        # Use smaller model that fits your RAM
        response = ollama.chat(
            model="llama3.2:1b",
            messages=[
                {
                    "role": "user",
                    "content": text,
                }
            ],
        )

        response_text = response["message"]["content"]
        print(f"AI: {response_text}")
        return response_text

    except Exception as e:
        print(f"Think error: {e}")
        return "Sorry, something went wrong while thinking."


def speak(text: str):
    if not text:
        return

    try:
        engine = pyttsx3.init()

        # Optional: choose voice
        voices = engine.getProperty("voices")
        if voices:
            engine.setProperty("voice", voices[0].id)

        # Speed of speech
        engine.setProperty("rate", 175)

        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        print(f"Speak error: {e}")


def main():
    print("--- Voice Assistant Started ---")
    speak("Hello, I am ready. You can start speaking.")

    while True:
        # 1. Listen
        user_input = listen()

        # If nothing heard, keep listening
        if not user_input:
            continue

        # Exit keywords
        if user_input.lower().strip() in ["exit", "stop", "quit", "bye"]:
            speak("Goodbye!")
            print("Exiting...")
            break

        # 2. Think
        ai_response = think(user_input)

        # 3. Speak
        speak(ai_response)


if __name__ == "__main__":
    main()
