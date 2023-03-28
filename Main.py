from os import system
from Ratings import getRating
import os
import time
import Processor

# Idk
system("title " + 'CPU Benchmark by Ycken')
req = input('Press ENTER to start test')
os.system('cls')
procName = Processor.getProcessorName()
# Adds waiting text
print('Wait while program do test!')
print('After testing, you can see the result of your processor')
# Varible for elasped time display
start_time = time.time()
# Need values for test
countMax = 200707187.5
countToPlus = 64226.30
curCount = 0
# Need for canel test
ended = False
isStart = True

def getTimeElasped():
    return(round((time.time() - start_time)))

def calculateScore():
    return(round((countMax / (getTimeElasped() + 0.1) / 1000)))

while isStart:
    if (curCount <= countMax):
        curCount += countToPlus
        # Changes CMD's name
        system("title " + 'CPU Benchmark by Ycken: Progress: ' + str(round((curCount / countMax) * 100, 1)) + '%, Processor: ' + procName + ', Time elasped: ' + str(getTimeElasped()) + ' seconds')
    else:
        if (not ended):
            # End screen
            score = calculateScore()
            os.system('cls')
            system("title " + 'CPU Benchmark by Ycken: Progress: ' + '100%, Processor: ' + procName + ', Time elasped: ' + str(getTimeElasped()) + ' seconds')
            print('Test succesfuly completed!')
            print('Your Processor: ' + procName)
            print('Time elasped: ' + str(getTimeElasped()) + ' seconds')
            print('Your score is: ' + str(score) + '! ' + getRating(score))
            print('\nMy discord for callback: Ycken#4650')
            ended = True
            exit = input('Press ENTER to exit')
            isStart = False
            