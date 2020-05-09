import speech_recognition as sr
import datetime
def recog():
    reco = sr.Recognizer()
    with sr.Microphone() as source:
        print("speak...")
        reco.pause_threshold = 1
        audio = reco.listen(source)
        try:
            output = reco.recognize_google(audio , language='en-in')
            output = str(output)
        except sr.UnKnownValueError:
            print("did not understand")
            return recog()
        return output
def file(speech):
    day = datetime.datetime.now().day
    time_hour = datetime.datetime.now().hour
    time_min = datetime.datetime.now().minute
    file_name = "day " + str(day) + "_" + "time "+ str(time_hour) + "_" + str(time_min)
    file_name = ("notepad/" + file_name + ".txt")
    f = open(file_name , "a")
    f.write(speech)
    f.close()
    print("saved in " + file_name)
##MAIN START##

#call the function which convert speech to text...And return string
speech = recog()
print("You said :\n" + speech)
flag = input("Do you want to save this into a file\n")
flag.lower()
if flag == "yes":
    file(speech)
else:
    recog()
