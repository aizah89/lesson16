import os 

shutdown = input("Shutdown computer? (yes or no):")

if shutdown == 'no':
    exit()
else:
    os.system("shutdown /s /t 1")