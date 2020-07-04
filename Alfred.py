import pyautogui
import speech_recognition as sr
import pyttsx3
import time
import threading
engine = pyttsx3.init()
engine.setProperty('rate', 215)
engine.setProperty('volume',1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
r = sr.Recognizer()
mic = sr.Microphone()
text = ""
name = "alfred"
engine.say("Starting Up")
engine.runAndWait()
engine.stop()
shutDown = False
spotify = True
while(not shutDown):
    while(text.lower().find(name) == -1 and text.lower().find("alfred") == -1):
        with mic as source:
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
        except:
            print(text)
    engine.say("Yes Sir?")
    engine.runAndWait()
    engine.stop()
    z = False
    while(not z):
        with mic as source:
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            z = True
        except:
            z = False
    fand = text.lower().find("and")
    t1 = text.lower().find("search for")
    if(t1 != -1):
        if(fand != -1 and fand > t1 + 11):
            engine.say("Searching for " + text[t1 + 11:fand])
        else:
            engine.say("Searching for " + text[t1+11:])
        engine.runAndWait()
        engine.stop()
        l = None
        while l == None:
            l = pyautogui.locateOnScreen('chrome2.png')
        pyautogui.click(x=l[0], y=l[1])
        l = None
        while l == None:
            l = pyautogui.locateOnScreen('star.png')
        pyautogui.click(x=l[0], y=l[1])
        if (fand != -1 and fand > t1 + 11):
            pyautogui.typewrite(text[t1+11:fand])
        else:
            pyautogui.typewrite(text[t1+11:])
        if(pyautogui.locateOnScreen('highlight.png') != None):
            pyautogui.press("backspace")
        pyautogui.typewrite("\n")
    t = text.lower().find("never")
    if (t != -1 and t1 == -1 or t != -1 and t1 != -1 and fand != -1):
        engine.say("Okay, no problem")
        engine.runAndWait()
        engine.stop()
    t = text.lower().find("order 66")
    if(t != -1 and t1 == -1 or t != -1 and t1 != -1 and fand != -1):
        engine.say("Yes sir")
        engine.runAndWait()
        engine.stop()
        shutDown = True
    t = text.lower().find("sleep")
    if (t != -1 and t1 == -1 or t != -1 and t1 != -1 and fand != -1):
        engine.say("Okay")
        engine.runAndWait()
        engine.stop()
        pyautogui.click(x=27,y=12)
        time.sleep(0.1)
        pyautogui.click(x=50, y=180)
    t = text.lower().find("change n")
    if (t != -1 and t1 == -1 or t != -1 and t1 != -1 and fand != -1):
        t2 = text[t+20:].find(" ")
        if(t2 == -1):
            t2 = len(text)-1
        name = text[t+19:t2+1].lower()
        engine.say("Changing nickname to " + name)
        engine.runAndWait()
        engine.stop()
    t = text.lower().find("restart")
    if (t != -1 and t1 == -1 or t != -1 and t1 != -1 and fand != -1):
        engine.say("Restarting")
        engine.runAndWait()
        engine.stop()
        l = None
        while l == None:
            l = pyautogui.locateOnScreen('replay.png')
        pyautogui.click(x=l[0], y=l[1])
        time.sleep(0.25)
        l = None
        while l == None:
            l = pyautogui.locateOnScreen('highlight2.png')
        pyautogui.click(x=l[0], y=l[1])
    t = text.lower().find("music")
    if (t != -1):
        tlist = text.split()
        musicType = ""
        prev = ""
        for i in tlist:
            if(i == "music"):
                musicType = prev
            prev = i
        l = None
        while l == None:
            l = pyautogui.locateOnScreen('chrome2.png')
        pyautogui.click(x=l[0], y=l[1])
        l = None
        while l == None:
            l = pyautogui.locateOnScreen('star.png')
        pyautogui.click(x=l[0], y=l[1])
        pyautogui.typewrite(musicType + " music")
        if (pyautogui.locateOnScreen('highlight.png') != None):
            pyautogui.press("backspace")
        pyautogui.typewrite("\n")
        l = None
        while l == None:
            l = pyautogui.locateOnScreen('videos.png')
        pyautogui.click(x=l[0], y=l[1])
        l = None
        while l == None:
            l = pyautogui.locateOnScreen('blue.png')
        pyautogui.click(x=l[0], y=l[1])
        print(l)
        engine.say("Playing " + musicType + " music")
        engine.runAndWait()
        engine.stop()
        time.sleep(5)
        l = None
        while l == None:
            l = pyautogui.locateOnScreen('minimize.png')
        pyautogui.click(x=l[0], y=l[1])
    t = text.lower().find("song")
    if (t != -1):
        print("hi")
        l = None
        while l == None:
            l = pyautogui.locateOnScreen('chrome2.png')
        pyautogui.click(x=l[0], y=l[1])
        print("hi2")
        l = None
        while l == None:
            l = pyautogui.locateOnScreen('star.png')
        pyautogui.click(x=l[0], y=l[1])
        if (fand != -1 and fand > t + 11):
            pyautogui.typewrite(text[t + 4:fand] + " song")
        else:
            pyautogui.typewrite(text[t + 4:] + " song")

        if (pyautogui.locateOnScreen('highlight.png') != None):
            pyautogui.press("backspace")
        pyautogui.typewrite("\n")
        l = None
        while l == None:
            l = pyautogui.locateOnScreen('videos.png')
        pyautogui.click(x=l[0], y=l[1])
        l = None
        while l == None:
            l = pyautogui.locateOnScreen('blue.png')
        pyautogui.click(x=l[0], y=l[1])
        if (fand != -1 and fand > t1 + 11):
            engine.say("Playing " + text[t1 + 4:fand])
        else:
            engine.say("Playing " + text[t1 + 4:])
        if (fand != -1 and fand > t + 11):
            engine.say("Playing " + text[t + 4:fand])
        else:
            engine.say("Playing " + text[t + 4:])
        engine.runAndWait()
        engine.stop()
        time.sleep(5)
        l = None
        while l == None:
            l = pyautogui.locateOnScreen('minimize.png')
        pyautogui.click(x=l[0], y=l[1])
    print(text)
    text = ""
