######################################################
#    This file is an example of how to use the LRHD 
#    The motors are fired sequentially 
#    and displayed on the screen visually
######################################################

from lrhd import lrhd
from pygame import mixer
import os.path
#from pathlib import path
import numpy as np
import time
import csv
import random
import testcsv as tcsv

#base_path = Path(__file__).parent
#file_path = base_path / "../crema_45_new/audio/1042_IEO_HAP_HI.mp3").resolve()
# Create an instance of the LRHD
hap_disp = lrhd()

# Get the dimension of the display
dims = (hap_disp.y_dim, hap_disp.x_dim)

# Clear the display
hap_disp.clear_display()

# Warms up the display
hap_disp.warmup()


class combination:  
    def __init__(self, emotion, audiofile):  
        self.emotion = emotion 
        self.audiofile = audiofile 


class combinationResponse:  
    def __init__(self, emotion, audiofile, response):  
        self.emotion = emotion 
        self.audiofile = audiofile 
        self.response = response
combinationlist = []  
combinationresponselist = []
answerinputtedyet = True
prevCombination = None

# Scans the display by firing each motor sequentially
'''for i in range(dims[0]*dims[1]):
    # Create a blank haptic image 
    image = np.zeros(dims, np.uint8)
    # Lights up one motor
    image.flat[i] = 255
    # Sends the haptic image to the LRHD
    hap_disp.draw(image)
    # Delay so it can be felt
    time.sleep(0.4)'''
def AU4(pulsewidth,gap):
    for x in range(0,1):
        image = np.zeros(dims, np.uint8)
        image[0,0] = 255
        image[0,1] = 255
        image[0,2] = 255
        image[0,3] = 255
        hap_disp.draw(image)
        time.sleep(pulsewidth)
        hap_disp.clear_display()
        time.sleep(gap)
        image = np.zeros(dims, np.uint8)
        image[1,0] = 255
        image[1,1] = 255
        image[1,2] = 255
        image[1,3] = 255
        hap_disp.draw(image)
        time.sleep(pulsewidth)
        hap_disp.clear_display()
        time.sleep(gap)
        
        image = np.zeros(dims, np.uint8)
        image[2,0] = 255
        image[2,1] = 255
        image[2,2] = 255
        image[2,3] = 255
        hap_disp.draw(image)
        time.sleep(pulsewidth)
        hap_disp.clear_display()
        time.sleep(gap)
    #time.sleep(5)
    
def AU1(pulsewidth,gap):
    for x in range(0,1):
        image = np.zeros(dims, np.uint8)
        image[1,0] = 255
        image[1,3] = 255
        hap_disp.draw(image)
        time.sleep(pulsewidth)
        hap_disp.clear_display()
        time.sleep(gap)
        image = np.zeros(dims, np.uint8)
        image[0,1] = 255
        image[0,2] = 255
        hap_disp.draw(image)
        time.sleep(pulsewidth)
        hap_disp.clear_display()
        time.sleep(gap)
        
        image = np.zeros(dims, np.uint8)
        image[1,1] = 255
        image[1,2] = 255
        hap_disp.draw(image)
        time.sleep(pulsewidth)
        hap_disp.clear_display()
        time.sleep(gap)
    #time.sleep(5)
    
    
def AU9(pulsewidth,gap):
    image = np.zeros(dims, np.uint8)
    image[2,1] = 255
    image[2,2] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display()
    time.sleep(gap) 
    image = np.zeros(dims, np.uint8)
    image[1,1] = 255
    image[1,2] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display()
    time.sleep(gap)
    image = np.zeros(dims, np.uint8)
    image[1,1] = 255
    image[1,2] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth) 
    hap_disp.clear_display()
    time.sleep(gap)
    #time.sleep(5)

def AU6(pulsewidth,gap):
    image = np.zeros(dims, np.uint8)
    image[1,0] = 255
    image[2,0] = 255
    
    image[1,3] = 255
    image[2,3] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display() 
    time.sleep(gap)
    image = np.zeros(dims, np.uint8)
    image[1,0] = 255
    image[2,0] = 255
    
    image[1,3] = 255
    image[2,3] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display()
    time.sleep(gap)
    image = np.zeros(dims, np.uint8)
    image[1,0] = 255
    image[2,0] = 255
    
    image[1,3] = 255
    image[2,3] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display()
    time.sleep(gap)
    #time.sleep(5)
    
def AU26(pulsewidth,gap):
    
    image = np.zeros(dims, np.uint8)
    image[1,1] = 255
    image[1,2] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display() 
    time.sleep(gap)
    image = np.zeros(dims, np.uint8)
    image[2,1] = 255
    image[2,2] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display()
    time.sleep(gap)
    image = np.zeros(dims, np.uint8)
    image[3,1] = 255
    image[3,2] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display()
    time.sleep(gap)
    #time.sleep(5)
    
def AU20(pulsewidth,gap):
    
    image = np.zeros(dims, np.uint8)
    image[3,1] = 255
    image[3,2] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display() 
    time.sleep(gap)
    image = np.zeros(dims, np.uint8)
    image[3,0] = 255
    image[3,1] = 255
    image[3,2] = 255
    image[3,3] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display()
    time.sleep(gap)
    image = np.zeros(dims, np.uint8)
    image[3,0] = 255
    image[3,3] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display()
    time.sleep(gap)
    #time.sleep(5)

def AU27(pulsewidth,gap):
    image = np.zeros(dims, np.uint8)
    image[2,1] = 255
    image[2,2] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display() 
    time.sleep(gap)
    image = np.zeros(dims, np.uint8)
    image[1,1] = 255
    image[1,2] = 255
    image[2,1] = 255
    image[2,2] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display()
    time.sleep(gap)
    image = np.zeros(dims, np.uint8)
    image[0,0] = 255
    image[0,3] = 255
    image[3,0] = 255
    image[3,3] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display()
    time.sleep(gap)
    #time.sleep(5)

def AU5(pulsewidth,gap):
    image = np.zeros(dims, np.uint8)
    image[2,0] = 255
    image[2,3] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display() 
    time.sleep(gap)
    image = np.zeros(dims, np.uint8)
    image[0,0] = 255
    image[0,3] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display()
    time.sleep(gap)
    #time.sleep(5)

def AU7(pulsewidth,gap):
    image = np.zeros(dims, np.uint8)
    image[0,0] = 255
    image[0,3] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display() 
    time.sleep(gap)
    image = np.zeros(dims, np.uint8)
    image[1,0] = 255
    image[1,1] = 255
    image[1,2] = 255
    image[1,3] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display()
    time.sleep(gap)
    #time.sleep(5)
    
def AU10(pulsewidth,gap):
    image = np.zeros(dims, np.uint8)
    image[3,1] = 255
    image[3,2] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display() 
    time.sleep(gap)
    image = np.zeros(dims, np.uint8)
    image[2,1] = 255
    image[2,2] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display()
    time.sleep(gap)
    
    image = np.zeros(dims, np.uint8)
    image[0,1] = 255
    image[0,2] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display()
    time.sleep(gap)
    #time.sleep(5)

def AU15(pulsewidth,gap):
    image = np.zeros(dims, np.uint8)
    image[1,1] = 255
    image[1,2] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display() 
    time.sleep(gap)
    image = np.zeros(dims, np.uint8)
    image[2,0] = 255
    image[2,3] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display()
    time.sleep(gap)
    
    image = np.zeros(dims, np.uint8)
    image[3,0] = 255
    image[3,3] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display()
    time.sleep(gap)
    #time.sleep(5)
    
def AU12(pulsewidth,gap):
    image = np.zeros(dims, np.uint8)
    image[3,1] = 255
    image[3,2] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display() 
    time.sleep(gap)
    image = np.zeros(dims, np.uint8)
    image[2,0] = 255
    image[2,3] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display()
    time.sleep(gap)
    
    image = np.zeros(dims, np.uint8)
    image[1,0] = 255
    image[1,3] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display()
    time.sleep(gap)
    #time.sleep(5)

def getListItem():
    my_path_file_location = os.path.abspath(os.path.dirname(__file__))
    path_file_location = os.path.join(my_path_file_location, "..\\file_list.csv")
    #print(path_file_location)
    path_file_location = "C:/Users/kuteb/source/repos/Haptic-Temperature-Project-new/file_list.csv"
    #print(path_file_location)
    with open(path_file_location) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        i =0;
        for row in csv_reader:
            if(i>0):
                combinationlist.append(combination(row[0],row[2]))
            else:
                i=i+1
''' #note: this only plays out the first occurence file, not all
mixer.init()
my_path = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(my_path, "../crema_45_new/audio/"+row[2])
file_path = ("C:/Users/kuteb/source/repos/Haptic-Temperature-Project-new/crema_45_new/audio/"+row[2])
print("playing " + row[2])
mixer.music.load(file_path)
mixer.music.play()
break'''

patternpause = 1

def happy(pulsewidth,gap):
    AU12(pulsewidth,gap)
    time.sleep(patternpause)
    AU6(pulsewidth,gap)

def sad(pulsewidth,gap):
    AU1(pulsewidth,gap)
    time.sleep(patternpause)
    AU6(pulsewidth,gap)

def anger(pulsewidth,gap):
    AU4(pulsewidth,gap)
    time.sleep(patternpause)
    AU7(pulsewidth,gap)

def fear(pulsewidth,gap):
    #getListItem("fear",intensity)
    AU5(pulsewidth,gap)

def disgust(pulsewidth,gap):
    #getListItem("disgust",intensity)
    AU10(pulsewidth,gap)


def playEmotion(strEmotion):
    if(strEmotion=="happy"):
        happy(0.25,0.05)
    if(strEmotion=="sad"):
        sad(0.25,0.05)
    if(strEmotion=="anger"):
        anger(0.25,0.05)
    if(strEmotion=="fear"):
        fear(0.25,0.05)
    if(strEmotion=="disgust"):
        disgust(0.25,0.05)

def playNextPattern():
    global prevCombination
    global answerinputtedyet 
    if(answerinputtedyet==False):
        print("seems like you did not record answer for the previous pattern played. please go back and input the participant's answer\n")
        return;
    answerinputtedyet=False;
    rand = random.randint(0,len(combinationlist)-1)
    filePlaying = combinationlist[rand].audiofile
    my_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(my_path, "../crema_45_new/audio/"+filePlaying)
    file_path = ("C:/Users/kuteb/source/repos/Haptic-Temperature-Project-new/crema_45_new/audio/"+filePlaying)
                
    emotionPlaying = combinationlist[rand].emotion
    prevCombination = combination(emotionPlaying,filePlaying)
    mixer.init()
    print("playing file " +filePlaying+ "\n")
    mixer.music.load(file_path)
    mixer.music.play()
    #playEmotion(emotionPlaying)
    combinationlist.remove(combinationlist[rand])
    print("number of combinations left: "+ (str)(len(combinationlist))+ "\n")

def repeatPrevPattern():
    if(prevCombination is None):
        print("no patterns have been played yet, so repeating is impossible!\n")
        return
    filePlaying = prevCombination.audiofile
    emotionPlaying = prevCombination.emotion
    
    my_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(my_path, "../crema_45_new/audio/"+filePlaying)
    file_path = ("C:/Users/kuteb/source/repos/Haptic-Temperature-Project-new/crema_45_new/audio/"+filePlaying)
                
    mixer.init()
    print("repeating emotion " + emotionPlaying+" with file " +filePlaying+ "\n")
    mixer.music.load(file_path)
    mixer.music.play()
    #playEmotion(emotionPlaying)

def askForAnswer():
    global answerinputtedyet
    if(prevCombination is None):
        print("no patterns have been played yet, so inputting answers is impossible!\n")
        return
    stringAnswer = str(input("type in subject's response to emotion "+prevCombination.emotion+ " and file "+ prevCombination.audiofile+"\n\t\taccepted responses:\n\t\ts for sad"+"\n\t\th for happy\n\t\tf for fear\n\t\ta for anger\n\t\td for disgust\n"))
    strAn = ""
    while(stringAnswer!="s" and stringAnswer!="h" and stringAnswer!="a" and stringAnswer!="d" and stringAnswer!="f"):
        print("input not recognized. try again.\n")
        stringAnswer = str(input("type in subject's response to emotion "+prevCombination.emotion+ " and file "+ prevCombination.audiofile+"\n\t\taccepted responses:\n\t\ts for sad"+"\n\t\th for happy\n\t\tf for fear\n\t\ta for anger\n\t\td for disgust\n"))
    if(stringAnswer=="s"):
        strAn = "sad"
    if(stringAnswer=="h"):
        strAn = "happy"
    if(stringAnswer=="a"):
        strAn = "anger"
    if(stringAnswer=="f"):
        strAn = "fear"
    if(stringAnswer=="d"):
        strAn = "disgust"
    combinationResponseGiven = combinationResponse(prevCombination.emotion,prevCombination.audiofile,strAn)
    combinationresponselist.append(combinationResponseGiven)
    answerinputtedyet = True


#start

pattern = -1
interval = -1
gapped = 0.05
intensityinput = "hi"
stringInput = ""

stringInput = str(input("type in next command:\n\tn for playing next pattern\n\tr for repeat\n\ti for inputting subject answers\n\tq for quit\n"))
getListItem()
#for i in combinationlist:
#    print(i.emotion+" "+i.audiofile+"\n")
while(stringInput!="q"):
    if(len(combinationlist)==0):
        print("all patterns have been played. press q to exit\n")
    if(stringInput=="n"):
        playNextPattern()
    elif(stringInput=="r"):
        repeatPrevPattern()
    elif(stringInput=="i"):
        askForAnswer()
    else:
        print("command not recognized. try again\n")
    stringInput = str(input("type in next command:\n\tn for playing next pattern\n\tr for repeat\n\ti for inputting subject answers\n\tq for quit\n"))

#finally print out all of the answers with the files
print("Emotion\t\t\t\t\tFilePlayed\t\t\t\t\tUser Response\n")
listpass = []
for x in combinationresponselist:
    print(x.emotion+"\t\t\t\t\t"+x.audiofile+"\t\t\t\t\t"+x.response)
    ps =[]
    ps.append(x.emotion)
    ps.append(x.audiofile)
    ps.append(x.response)
    listpass.append(ps)
tcsv.savefile(listpass)
'''pattern = -1
interval = -1
gapped = 0.05
while (pattern != 0):
    print(pattern)
    print(interval)
    print(gapped)
    time.sleep(2)
    if pattern==1:
        alternateleftright(interval,gapped)
        print("here")
    elif pattern==2:
        alternatetopbottom(interval,gapped)
    elif pattern==3:
        explode(interval,gapped)
    elif pattern==4:
        rain(interval,gapped)
    elif pattern==5:
        shouldertap(interval,gapped)
    elif pattern==6:
        snakevertical(interval,gapped)
    elif pattern==7:
        snakehorizontal(interval,gapped)
    elif pattern==8:
        sixmotorburst(interval,gapped)
    elif pattern==9:
        spinedown(interval,gapped)
    elif pattern==10:
        spineup(interval,gapped)
    elif pattern==11:
        wavedown(interval,gapped)
    elif pattern==12:
        waveleft(interval,gapped)
    elif pattern==13:
        waveright(interval,gapped)
    elif pattern==14:
        waveup(interval,gapped)
    elif pattern==15:
        spiralin(interval,gapped)
    elif pattern==16:
        spiralout(interval,gapped)
    pattern = int(input("type on pattern number (0 to stop)"))
    interval =float(input("type in interval - 1 or 0.25"))'''
