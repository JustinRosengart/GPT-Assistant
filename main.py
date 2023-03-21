import speech_recognition as sr
import pyttsx3
import openai

# Ersetzen Sie YOUR_API_KEY durch Ihren tatsächlichen OpenAI API-Schlüssel
openai.api_key = open("openai_token", "r").read()


class LachsAssistent:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

    def sprechen(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with sr.Microphone() as quelle:
            print("Zuhören...")
            audio = self.recognizer.listen(quelle)
        try:
            text = self.recognizer.recognize_google(audio, language="de-DE")
            print(f"Benutzer sagte: {text}")
            return text
        except:
            print("Entschuldigung, ich konnte Sie nicht verstehen.")
            return ""

    def openai_anfrage(self, frage):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"{frage} in deutsch\n",
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.5,
        )
        antwort = response.choices[0].text.strip()
        return antwort

    def starten(self):
        print("Lachs-Assistent gestartet.")
        while True:
            gesprochener_text = self.listen()
            if "hey gpt" in gesprochener_text.lower():
                self.sprechen("Ja, wie kann ich Ihnen helfen?")
                frage = self.listen()
                antwort = self.openai_anfrage(frage)
                self.sprechen(antwort)


if __name__ == "__main__":
    assistent = LachsAssistent()
    assistent.starten()
