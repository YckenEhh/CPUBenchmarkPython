from winreg import *

# Processor name from regedit (ONLY WINDOWS)
def getProcessorName():
    aReg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
    aKey = OpenKey(aReg, r"HARDWARE\DESCRIPTION\System\CentralProcessor\0")
    processorName = QueryValueEx(aKey, 'ProcessorNameString')[0]
    return(processorName)