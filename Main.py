from os import system
from winreg import *
import time

aReg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
aKey = OpenKey(aReg, r"HARDWARE\DESCRIPTION\System\CentralProcessor\0")
processorName = QueryValueEx(aKey, 'ProcessorNameString')[0]
start_time = time.time()
countMax = 200707187.5
countToPlus = 64226.30
curCount = 0
ended = False

while True:
    if (curCount <= countMax):
        curCount += countToPlus
        system("title " + 'CPU Benchmark by Ycken: Progress: ' + str(round((curCount / countMax) * 100, 1)) + '%, Processor: ' + processorName + ', Time elasped: ' + str(round((time.time() - start_time))) + ' seconds')
    else:
        if (not ended):
            system("title " + 'CPU Benchmark by Ycken: Progress: ' + '100%, Processor: ' + processorName + ', Time elasped: ' + str(round((time.time() - start_time))) + ' seconds')
            print('Test succesfuly completed!')
            print('Your Processor: ' + processorName)
            print('Time elasped: ' + str(round(time.time() - start_time)))
            print('Your score is: ' + str(round((countMax / (time.time() - start_time) / 1000))) + '!')
            print('\nMy discord for callback: Ycken#4650')
            ended = True