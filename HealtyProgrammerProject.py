#Excercise 7
#Healty Programmer

#9am - 5pm
#Water - water.mp3 (3.5 litres) - input - Drank - log time in text - Every 40 Minute
#Eyes - eyes.mp3 - Done - Every 30min - EyDone - log file - Every 30 Minute
#Physical activity - physcical.mp3 -every 45 min - Done - Exdone - log file

#Rules
#Import pygame module to play audio

from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open('mylogs.txt','a') as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    #musicloop('water.mp3','stop')
    init_water = time()
    init_eyes = time()
    init_excercise = time() 
    watersecs = 5
    eyessecs = 20
    exsecs = 10
   

    while True:
         if time() - init_water>watersecs:
             print('Water Drinking time. Enter "drank" to stop the alaram')
             musiconloop('water.mp3','drank')
             init_water = time()                      
             log_now('Drank water at')

         if time() - init_eyes>eyessecs:
             print('Eye Excercise time. Enter "doneeyes" to stop the alaram')
             musiconloop('eye.mp3','doneeyes')
             init_eyes = time()
             log_now('Eye Relaxed at at')    

         if time() - init_excercise>exsecs:
             print('Physical Activity Time. Enter "donephy" to stop the alaram')
             musiconloop('Exc.mp3','donephy')
             init_excercise = time()
             log_now('Physcial Activity done at')         

       
          

       
             
                
