import pyttsx3
import pytube
import wikipedia
import os
import random
import datetime
import webbrowser
import speech_recognition as sr

usern=os.environ['USERNAME']
engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognition():
    s=sr.Recognizer()
    s.energy_threshold=600
    with sr.Microphone() as source:
        print("Listening...")
        audio = s.listen(source)

    try:
        print("Recognizing.....")
        print("please wait....")
        query=s.recognize_google(audio, language='en-in')
        print(query)
        return query
    except Exception as e:
        print("something went wrong while recognizing say that again please")
        print("Check your internet connection")
        speak("check your internet connection")
        return "None"

def copycatgame():
    speak("speak any thing")
    while True:
        repeat=recognition().lower()
        if "exit" in repeat:
            speak("exiting game mode")
            break
        else:
            speak(repeat)
            print(repeat)
def tossgame():
    while True:
        speak("coin is in the air so what you choose heads or tails")
        choose=recognition().lower()
        r=random.randint(1,2)
        if "heads" in choose or "head" in choose:
            if(r==1):
                print("Heads it is")
                speak("head it is, you won")
            else:
                print("Tails it is")
                speak("tail it is, you loose")
        elif "tails" in choose or "tail" in choose or "tales" in choose or "tale" in choose:
            if(r==1):
                print("Heads it is")
                speak("head it is, you loose")
            else:
                print("Tails it is")
                speak("tail it is, you won")
        elif "exit" in choose:
            speak("exiting game mode")
            break
        else:
            speak("don't cheat, choose either head or tail")
            print("you said "+choose)

def petalsgame():
    randno=int(random.randint(4,9))
    for i in range(randno):
        if i%2==0:
            print("She Loves You")
            speak("she loves you")
        else:
            print("She Loves you not")
            speak("she loves you not")
    print('\a')
    if randno%2==0:
        print("Oh ohh... I Sorry but the petals ended")
        speak("sorry to say but the petals ended")
    else:
        print("Congratulation.... She Loves you")
        speak("congratulation, she loves you")
        
def remove_char(list1, list2): 
	for i in range(len(list1)) : 
		for j in range(len(list2)) : 
			if list1[i] == list2[j] : 
				c = list1[i] 
				list1.remove(c) 
				list2.remove(c) 
				list3 = list1 + ["*"] + list2 
				return [list3, True] 
	list3 = list1 + ["*"] + list2 
	return [list3, False]

def flamesgame():
    print("Enter your name:")
    speak("Enter your name")
    p1=input()
    p1=p1.lower()
    p1_list=list(p1)
    p1.replace(" ","")
    print("Enter your Crush name:")
    speak("enter your crush name")
    p2=input()
    p2=p2.lower()
    p2.replace(" ","")
    p2_list=list(p2)
    proceed=True
    while proceed:
        ret_list=remove_char(p1_list,p2_list)
        con_list=ret_list[0]
        proceed=ret_list[1]
        star=con_list.index("*")
        p1_list=con_list[:star]
        p2_list=con_list[star+1:]
    count=len(p1_list)+len(p2_list)
    reslt=["Friends","Lovers","Affection","Marriage","Enemies","Siblings"]
    while len(reslt)>1:
        sp=(count%len(reslt)-1)
        if sp>=0:
            right=reslt[sp+1:]
            left=reslt[:sp]
            reslt=right+left
        else:
            reslt=reslt[:len(reslt)-1]
    print(p1+" and "+p2+"'s relationship status is "+reslt[0])
    speak(p1+" and "+p2+"'s relationship status is "+reslt[0])

def lovecalc():
    speak("enter your lover name")
    nme=input()
    speak("enter your name")
    nme1=input()
    r=random.randint(1,100)
    print(nme+" loves "+nme1)
    print("And love percentage is "+str(r)+"%")
    speak("your love percentage is "+str(r)+" percent")
    speak("press any key to exit")
    r=input()
def dicegame():
    r=random.randint(1,6)
    print("Dice shows"+str(r))
    speak("dice shows"+str(r))
    print("Press any key to exit")
    k=input()
def wishing():
    hour=int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning "+usern+".. i am Kaushiki... What can i do for you")
        speak("good morning "+usern+", i am kaushiki what can i do for you")
    elif hour >=12 and hour < 13:
        print("Good Noon "+usern+" i am Kaushiki.... What can i do for you")
        speak("good noon "+usern+", i am kaushiki what can i do for you")
    elif hour >=13 and hour < 16:
        print("Good Afternoon "+usern+" Sir... I am Kaushiki your Assistant.. Tell me how can i help you")
        speak("good afternoon "+usern+", sir i am kaushiki your assistant, tell me how can i help you")
    elif hour >=16 and hour < 21:
        print("Good Evening "+usern+" My Friend... I am Kaushiki your virtual helper.. Tell me how can i help you")
        speak("good eveniong "+usern+", my friend, i am kaushiki your virtual helper, tell me how can i help you")
    else:
        print("Good Night Dear "+usern+"... Kaushiki is here for you... Tell me what can i do for you")
        speak("good night dear "+usern+", kaushiki is here for you, tell me what can i do for you")

if __name__ == "__main__":
    wishing()
    while True:
        querry=None
        querry=recognition().lower()
        r=random.randint(1,4)
        if "alexa" in querry or "google assistant" in querry or "siri" in querry or "cortana" in querry:
            print("Please don't compare me with big names, i am your little friend developed by Kaustubh")
            speak("oh! come on dear")
            speak("Please don't compare me with big names, i am your little friend developed by Kaustubh")
        elif "i love you" in querry or "marry me" in querry:
            if(r==1):
                print("awwww.... I am feeling shy")
                speak("I am feeling shy")
            elif(r==2):
                print("but i am a machine... (HUMAN)")
                speak("but i am a machine, human")
            elif(r==3):
                print("but our marriage is not possile")
                speak("bitter truth is that our marriage is not possible")
            else:
                print("can we continue as a friend")
                speak("can we continue as a friend only")
        elif "your developer" in querry or "who developed you" in querry:
            print("My developer is Kaustubh vats")
            speak("my developer is kaustubh vats")
        elif "what can you do" in querry or "features" in querry or "help" in querry:
            print("Ask me to open your Favourite website, Talk to me, Play games, Play videos, Download Youtube Videos, Wikipedia")
            speak("ask me to open your favourite website, talk to me, play games, play videos, download youtube videos, wikipedia")
        elif "how are you" in querry or "how are you doing" in querry:
            print("I am good tell me what can i do for you")
            speak("i am good tell me what can i do for you")
        elif "you are beautiful" in querry or "you are good" in querry:
            print("Thank you for the compliment")
            speak("thank you for the compliment")
        elif "roll a die" in querry:
            dicegame()
        elif "did you know me" in querry or "my name" in querry:
            print("Yes your name is "+usern)
            speak("yes your name is "+usern) 
        elif "thanks" in querry or "thank you" in querry:
            print("It's nothing, you are my friend dear")
            speak("It's nothing, you are my friend dear and it is my duty to make you happy")
        elif "time" in querry:
            print(datetime.datetime.now())
            nh=str(datetime.datetime.now().hour)
            nm=str(datetime.datetime.now().minute)
            ns=str(datetime.datetime.now().second)
            speak("currently it is "+nh+" hours "+nm+" minutes and "+ns+" seconds")
        elif "youtube" in querry:
            if "download" in querry:
                print("Paste your Youtube URL here")
                speak("paste your youtube video U R L here")
                video_url = input()
                speak("downloading your video")
                print("Downloading your video")
                try:
                    youtube = pytube.YouTube(video_url)
                    video = youtube.streams.first()
                    video.download('Kaushiki/Download')
                    print("Video Downloaded succesfully")
                    speak("Video Downloaded succesfully press any key")
                    print("Press any key")
                    input()
                except:
                    print("Some error occured")
                    speak("Some error occured")
            else: 
                print("Opening youtube..")
                speak("opening youtube")
                webbrowser.open("https://www.youtube.com/")
                speak("welcome to youtube")
                break
        elif "facebook" in querry or "fb" in querry:
            print("opening Facebook...")
            speak("Opening facebook")
            webbrowser.open("https://www.facebook.com/")
            speak("here is your f b requested page")
            break
        elif "instagram" in querry or "insta" in querry:
            print("opening Instagram...")
            speak("Opening insta gram")
            webbrowser.open("https://instagram.com/")
            speak("insta gram is here")
            break
        elif "whatsapp" in querry:
            print("Opening Whatsapp...")
            speak("opening whatsapp")
            webbrowser.open("https://web.whatsapp.com/")
            speak("welcome to whatsapp")
            break
        elif "cricket" in querry or "live score" in querry:
            print("Live cricket score is here")
            speak("live cricket score is here")
            webbrowser.open("https://www.google.com/search?q=cricket live score")
            speak("these thrilling cricket match is going on check them out")
            break
        elif "videos" in querry or "video" in querry:
            speak("which type of video you want to play")
            vid=recognition()
            speak("sure")
            webbrowser.open("https://www.youtube.com/results?search_query="+vid+"videos")
            break
        elif "google" in querry:
            if "open google" in querry:
                speak("opening google")
                webbrowser.open("https://www.google.co.in/")
                speak("search anything here")
            else:
                querry=querry.replace("google","")
                webbrowser.open("https://www.google.com/search?q="+querry)
                speak("search results from google are here")
            break
        elif "wikipedia" in querry:
            querry=querry.replace("wikipedia","")
            results=wikipedia.summary(querry, sentences=2)
            print("According to wikipedia")
            speak("according to wikipedia")
            print(results)
            speak(results)
            print("Press any key to continue")
            inp=input()
        elif "games" in querry or "game" in querry:
            print("which game you want to play")
            print("1. Toss a coin")
            print("2. Count the petals")
            print("3. roll a dice")
            print("4. copy cat")
            print("5. Love calculator")
            print("6. Flames")
            print("input the number using keyboard")
            speak("input the number using keyboard")
            h=input()
            print("say exit to exit game mode during playing a game")
            speak("say exit to exit game mode during playing a game")
            if(h=="1"):
                speak("opening toss a coin game")
                tossgame()
            elif(h=="2"):
                speak("opening count the petals")
                petalsgame()
            elif(h=="3"):
                speak("roll a dice")
                dicegame()
            elif(h=="4"):
                speak("opening copy cat")
                copycatgame()
            elif(h=="5"):
                speak("opening love calculator")
                lovecalc()
            elif(h=="6"):
                speak("opening Flames")
                flamesgame()
            else:
                print("Exiting game mode")
                speak("exiting game mode")

        elif "hello" in querry or "hey" in querry or "hay" in querry:
            if(r==1):
                print("Hello my friend")
                speak("hello my friend")
            elif(r==2):
                print("Hola....            (Hola is Hello in Spanish)")
                speak("hola, hola is Hello in Spanish")
            elif(r==3):
                print("Namaskaar...          (Namaskaar is hello in hindi)")
                speak("namaskaar, namaskaar is hello in hindi")
            else:
                print("Hello dear how can i help you")
                speak("hello dear how can i help you")
        elif "open" in querry:
            querry=querry.replace("open ","")
            querry=querry.replace(" ","")
            print("opening "+querry)
            speak("opening "+querry)
            webbrowser.open("https://www."+querry)
            speak("here is what i found")
            break
        elif "exit" in querry or "bye" in querry:
            print("Bye Bye see you later")
            speak("bye bye see you later") 
            break
        elif "none" in querry:
            continue
        else:
            print("Sorry i did not understand")
            speak("sorry i did not understand")
            webbrowser.open("www.google.com/search?q="+querry)
            speak("but here is what i found")
            break