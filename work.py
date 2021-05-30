# the library imported for speech recognition
import speech_recognition as sr
from chatterbot import ChatBot               # the library imported for chatbot
# the library imported for text to speech conversion
import pyttsx3
from chatterbot.trainers import ChatterBotCorpusTrainer  # to train chatbot
# Creating the profile for the chatbot
bot = ChatBot('talkbot')
bot.set_trainer(ChatterBotCorpusTrainer)  # Setting the trainer
# Training the chatBot on the corpus data
bot.train('chatterbot.corpus.english')


while(True):  # Interaction itself with the bot
    r = sr.Recognizer()
    print("please talk")
    mic = sr.Microphone()
    with mic as source:  # taking input from mic and giving it to the bot
        r.adjust_for_ambient_noise(source)
        audio = r.record(source, duration=3)
        print("recognise")
        # using google API to recognise speech
        guess = r.recognize_google(audio)
        print(guess)

    message = guess
    if((message == 'bye') or (message == 'Bye')):
        # using pyttsx3 to convert bot's response into voice
        con1 = pyttsx3.init()
        reply = 'Nice to talk to you.'
        con1.say(reply)
        con1.runAndWait()
        print('{} : {}'.format(bot.name, reply))
        break
    else:
        con = pyttsx3.init()  # using pyttsx3 to convert bot's response into voice
        print(message)  # printing the bot's response
        reply = bot.get_response(message)
        con.say(reply)
        con.runAndWait()
        print('{} : {}'.format(bot.name, reply))
