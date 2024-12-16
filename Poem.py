# 10. Write a speaking chatbot program in Python to provide: (20 points)
# First name initial A-F: Read a short Mother's Day poem
# First name initial G-M: Read a short Father's Day poem
# First name initial N-Z: Read a short Valentine's Day poem

# First name initial: J => Read a short Father's Day poem

import pyttsx3
import random
import time

b = "Spartan: "
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Predefined list for Father's Day poem
father_poem = [
    "A father is someone you can depend, A role model and a friend. He guides you through thick and thin, A love so deep, it’s held within.",
    "To the world, you’re a father, but to me, you’re the world. Happy Father’s Day to the one who makes everything better.",
    "Father, you are the strength that never fades, The comfort I find in the darkest of days. Happy Father's Day, with love that stays.",
    "Dad, you’ve been my guiding light, Showing me the way, day and night. Your love is endless, and your heart is true, I’m so grateful to have you.",
    "To the dad who always knows just what to say, who helps me find my way, Happy Father’s Day, in every possible way!",
    "Fathers are the ones who teach us how to fly, with wings of love that never die. Happy Father’s Day to the one who made me strong and high.",
    "A father's love is a treasure so deep, a promise that’s forever to keep. Happy Father’s Day, Dad, with love and cheer, I’m so lucky to have you near.",
    "To the one who taught me how to be brave, To the one who’s always there, keeping me safe. Happy Father’s Day, you’re my hero, Dad, and I’ll love you always."
]

# Text-to-Speech Function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Greeting Function Based on Time of Day
def greetings():
    print(b, 'Good day. My name is Spartan. Version 1.00')
    speak('Good day. My name is Spartan. Version 1.00')
    print(b, 'Would you like to hear a short Father\'s Day poem?')
    speak('Would you like to hear a short Father\'s Day poem?')

# Main Command Function to read Father's Day poem
def takeCommand():
    while True:
        print(" ")
        query = input("User: ")

        if 'yes' in query.lower() or 'one more' in query.lower():
            poem = random.choice(father_poem)
            print(b, poem)
            speak(poem)
        
        elif 'exit' in query.lower() or 'bye' in query.lower():
            print(b, "Goodbye, my friend. I will miss you")
            speak("Goodbye, my friend. I will miss you")
            break

# Startup and Greeting
time.sleep(2)
print('Initializing...')
time.sleep(2)
print('Spartan is preparing...')
time.sleep(2)
print('Environment is building...')
time.sleep(2)
greetings()
takeCommand()
