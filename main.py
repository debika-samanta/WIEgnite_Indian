import pyttsx3
import speech_recognition as s
import datetime
import cv2
import winsound

cam = cv2.VideoCapture(0)

voice = pyttsx3.init()
time = datetime.datetime.now()
def ask() :
    voice.say("Mam Are you feeling safe ??")
    voice.runAndWait()

#def listen():
#    with s.Microphone() as source:
#        r.pause_threshold = 1
#        audio = r.listen(source)
#    try :
#        print("Recognize")
#        query = r.recognize_google(audio, language='en-in')
#        print(query)
#    except Exception :
#        print("error")
#        return "None"
#    return query
#speech = listen();

if((int(time.strftime("%H"))>19) and (int(time.strftime("%H"))<5)):
    # it would execute only in the night time

    if(int(time.strftime("%M")==30) and (int(time.strftime("%M")==0))):
         # this time would be set as per the timing of stopages

        speech= str(input("The microphone input "))
        if(speech=="no"):
            while cam.isOpened():
                    # ret stands for retrive
                ret, frame1 = cam.read()
                ret, frame2 = cam.read()
                diff = cv2.absdiff(frame1, frame2)
                gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
                blur = cv2.GaussianBlur(gray, (5, 5), 0)
                _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
                dilated = cv2.dilate(thresh, None, iterations=3)
                contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                    # cv2.drawContours(frame1,contours,-1,(0,255,0),2)
                for c in contours:
                    if cv2.contourArea(c) < 5000:
                        continue
                    x, y, w, h, = cv2.boundingRect(c)
                    cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    winsound.Beep(700, 200)
                        # winsound.PlaySound("sound.file",in case for giving instruction of not doing nusence)


                if cv2.waitKey(10) == ord('q'):
                        # if user gives input "q" then program stops..
                        break
                cv2.imshow('camera', frame1)


