import random
import RPi.GPIO as GPIO
from pygame import mixer
from time import sleep
'''
+++++++++
use pins 11,13,15 for GPIO activation buttons
+++++++++
USED BY I2c Bonnet uses pins 1,2,4,6,35,40 these are unavailible.
+++++++++
'''
foo=0
press = 0
Ls = ["L1.wav","L2.wav","L3.wav","L4.wav","L5.wav","L6.wav","L7.wav","L8.wav","L9.wav","L10.wav","L11.wav","L12.wav","L13.wav"]
Ms = ["M1.wav","M2.wav","M3.wav","M4.wav","M5.wav","M6.wav","M7.wav","M8.wav","M9.wav","M10.wav","M11.wav","M12.wav","M13.wav"]
Ss = ["S1.wav","S2.wav","S3.wav","S4.wav","S5.wav","S6.wav","S7.wav","S8.wav","S9.wav","S10.wav","S11.wav","S12.wav","S13.wav"]

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN)
GPIO.setup(22, GPIO.IN)

def button():
    while True:
        
        if GPIO.input(17) == False:
            print("short sound")
            Shortsound()
        
        if (GPIO.input(27) == False):
            print('longsound')
            Longsound()

        if (GPIO.input(22) == False):
            print('medsound')
            Medsound()
        
        sleep(0.3);
   
        #press=input("enter\n")
        #print('pressed ', press)
        #return int(press)
   
def RNG():#defnine random number generator
    x=0
    rnv = random.randint(1,13)
    print('Rnv is:',rnv)
    return rnv
'''
ideal sound function
def Sound(x):
    mixer.init()
    mixer.music.load(Ls[1])
    mixer.music.play()
    #while mixer.music.get_busy()==True:
    print("playing...")
    mixer.quit()
'''

def Longsound(): #plays a long sound
    x=RNG()
    def Lsound(x):
        mixer.init()
        mixer.music.load(Ls[x-1])
        mixer.music.play()
        while mixer.music.get_busy()==True:
            print(x-1)#temp
        mixer.quit()
        
    if x==1:
       Lsound(x)
    elif x==2:
        Lsound(x)        

    elif x==3:
        Lsound(x)

    elif x==4:
        Lsound(x)

    elif x==5:
        Lsound(x)

    elif x==6:
        Lsound(x)

    elif x==7:
        Lsound(x)

    elif x==8:
        Lsound(x)

    elif x==9:
        Lsound(x)

    elif x==10:
        Lsound(x)

    elif x==11:
        Lsound(x)

    elif x==12:
        Lsound(x)

    elif x==13:
        Lsound(x)

def Shortsound():#plays short sound
    x=RNG()
    def Ssound(x):
        mixer.init()
        mixer.music.load(Ss[x-1])
        mixer.music.play()
        while mixer.music.get_busy()==True:
            print(x-1)#temp
        mixer.quit()
    if x==1:
        Ssound(x)

    elif x==2:
        Ssound(x)
        
    elif x==3:
        Ssound(x)

    elif x==4:
        Ssound(x)

    elif x==5:
        Ssound(x)

    elif x==6:
        Ssound(x)

    elif x==7:
        Ssound(x)

    elif x==8:
        Ssound(x)

    elif x==9:
        Ssound(x)

    elif x==10:
        Ssound(x)

    elif x==11:
        Ssound(x)

    elif x==12:
        Ssound(x)

    elif x==13:
        Ssound(x)

def Medsound():
    x=RNG()
    def Msound(x):
        mixer.init()
        mixer.music.load(Ms[x-1])
        mixer.music.play()
        while mixer.music.get_busy()==True:
            print(x-1)#temp
        mixer.quit()
    if x==1:
        Msound(x)

    elif x==2:
        Msound(x)
        
    elif x==3:
        Msound(x)

    elif x==4:
        Msound(x)

    elif x==5:
        Msound(x)

    elif x==6:
        Msound(x)

    elif x==7:
        Msound(x)

    elif x==8:
        Msound(x)

    elif x==9:
        Msound(x)

    elif x==10:
        Msound(x)

    elif x==11:
        Msound(x)

    elif x==12:
        Msound(x)

    elif x==13:
        Msound(x)

    
def main():
    print("\n\nhello world\n")
    press = button()
    #print("main post button",press)
    '''
    if press == 1:#calling Longsound
        Longsound()
    if press ==2:#calling Medsound
        Medsound()
    if press==3:#calling shortsound
        Shortsound()
        '''
'''
main program run
'''
while True:   #loops program ill figure out how to exit and shutdown later
    main() #calls main program        
