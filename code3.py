#robo speaker
import pyttsx3
print ("welcome to robo speaker created by zoya")
robo = pyttsx3.init()
# x = input("what you want me to say: ")
while True:
    x = input("what you want me to say: ")
    if (x == "q"):    
        break
    robo.say(x)


    robo.runAndWait()
