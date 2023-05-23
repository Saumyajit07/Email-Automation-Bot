import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()

    except:
        pass


def send_email(receiver, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('saumyajit.mondal07@gmail.com', 'Bachhanari')
    email = EmailMessage()
    email ['From'] = 'saumyajit.mondal07@gmail.com'
    email ['To'] = receiver
    email.set_content(message)
    server.send_message(email)



email_list = {
    'saumya' : 'saumyajitmondal6@gmail.com',
    'rashi' : '4643458ac@gmail.com',
    'puchki' : 'sinfeci@gmail.com',
    'jason' : 'yeviseni@gmail.com'
}
def get_email_info():
    talk('To whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, message)
    talk('Hey Saumyajit. Your Email is sent')


get_email_info()
