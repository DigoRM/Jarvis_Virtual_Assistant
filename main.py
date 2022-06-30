import pyttsx3 # Transform text to voice
from datetime import datetime as dt
engine =pyttsx3.init()

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

wish()
#
#while True:
#   voice = input("Olá, sou sua nova assistente virtual, pode testar minha voz digitando o texto: \n")
#   
#   speak(voice)
