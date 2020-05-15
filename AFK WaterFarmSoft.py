import os
import MotoZero
from datetime import datetime

def repage():
    print("\nAFK WaterFarmSoft V5.0 \nCopyright Vassilis Papavassilopoulos & Samuel Schoonhoven \nAll Rights Reserved\nType help For Help\n\n")
    
def clear(): 
    os.system("cls")

def time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time - " + current_time)

def quickstart():
    length = int(input("Time (seconds): "))
    print("Pump on for {} second(s)".format(str(length))) 
    MotoZero.quickstart(MotoZero.relay, length)
    clear()
    repage()
    
def scheduled_start():
    time = input("Start at what time? (format - HH:MM (24-hour)): ")
    print("SCHEDULED MODE ACTIVATED")
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        if time == current_time:
            MotoZero.procedure(MotoZero.relay)
            print("SCHEDULED MODE ACTIVATED")
    

def main():
	while True:
		command = input("\n>").lower()
		command.replace(" ", "")
		if command == "help":
			print("HELP: \nquickstart - Starts pump for set time\nschedule - Starts pump at scheduled time\nhelp - Displays this page\ntime - Displays Time\nexit - Exits")
		elif command == "time":
			time()
		elif command == "quickstart":
			quickstart()
			now = datetime.now()
			current_time = now.strftime("%H:%M:%S")
			print("Current Time - " + current_time)
		elif command == "schedule":
			scheduled_start()
		elif command == "exit":
		    exit()
		else:
			print("'{}' is not recognised as a command".format(command))


repage()
time()

main()
