import pyttsx3 # Transform text to voice
engine =pyttsx3.init()
import speech_recognition as sr
sr.__version__ # Transform voice into text
from datetime import datetime as dt

# Função para o assistente me ouvir :)
def commandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Estou te ouvindo querido...")
        r.pause_threeshold = 1
        audio = r.listen(source)
    try:
        print("Traduzindo...")
        query = r.recognize_google(audio, language="pt-BR")
        print(query)
    except Exception as e:
        print(e)
        speak("Não entendi, fale novamente por favor?")
        return "None"
    return query



# Função para usuario inserir o texto e a assistente falar
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Função para falar o horário
def time():
    time = dt.now().strftime("%I:%M:%S")
    speak("Agora são")
    speak(time)

# Função para falar a data
def date():
    year = dt.now().year
    month = dt.now().month
    day = dt.now().day
    speak("hoje é dia")
    speak(day)
    speak("Estamos no mês")
    speak(month)
    speak("do ano de")
    speak(year)

# Função para validar o horário e a saudação a ser falada pela assistente.
def greeting():
    hour = dt.now().hour
    if hour >= 5 and hour <=12:
        speak("Bom dia Rodrigo!")
    elif hour > 12 and hour <=18:
        speak("Boa tarde Rodrigo!")
    elif hour > 18 and hour <5:
        speak("Boa noite Rodrigo!")

# Função de boas vindas
def wish():
    speak("Olá meu amor. Seja bem vindo de volta.")
    date()
    time()
    greeting()
    speak("Como posso te ajudar?")

# Função para executar o código somente se o arquivo é executado diretamente, não importado.
if __name__ == "__main__":
    wish()

    while True:
        query = commandMic().lower()
        
        if 'hora' or 'horario' in query:
            time()        

        elif 'dia' or 'data' in query:
            date()



#while True:
#   voice = input("Olá, sou sua nova assistente virtual, pode testar minha voz digitando o texto: \n")
#   
#   speak(voice)
