# import pyttsx3
# engine= pyttsx3.init()
# engine.say(" I will speak this text")
# engine.runAndWait()
import pyttsx3
engine = pyttsx3.init()
engine.say("Testing 1 2 3")
engine.runAndWait()
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Select default voice
engine.say("Hello, this is a test.")
engine.runAndWait()
