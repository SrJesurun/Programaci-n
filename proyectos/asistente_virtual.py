import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
engine.say("Hola, ¿en que puedo ayudarte?")
engine.runAndWait()

r = sr.Recognizer()
with sr.Microphone() as source:
    print("di algo:")
    audio = r.listen(source)
    texto = r.recognize_google(audio, language="es-ES")
    print("dijiste:", texto)
    
if "hora" in texto:
    from datetime import datatime
    hora = datatime.now().strftime("%H:%M")
    engine.say(f"la hora es {hora}")
elif "como estas" in texto:
    engine.say("estoy aprendiendo contigo")
else:
    engine.say("no entendi eso")
engine.runAndWait()