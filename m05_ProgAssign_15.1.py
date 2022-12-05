"""
----------------------------------------------------------------------------------------------------------------------------------
Program Name: Book Thing To Do 15.1

Author: Josh Lanier 

SDEV 220

12/4/22

Program Purpose: To practice the use of the multiprocessing module. Program runs three separate processes that each execute
the print() function, which when called waits a random amount of time between 0 and 1 seconds, and then prints the current time. 

Variables: 

- waitTime      (float)             randomly generated float value created by random(), between 0 and 1, to feed to the sleep()
                                    function and to the 'Program Info' thread for testing purposes. sleep() uses it to simulate 
                                    processing time.

- currTimeST    (Structured Time)   current time held in a Structured Time object (curr[ent]TimeS[tructured]T[ime])

- fmt           (string)            format string to pass to currTimeStr as the format for the strftime() function

- currTimeStr   (string)            returned string from strftime(fmt, currTimeST) holding the current time in format
                                    24 hour time: HOUR:MIN
                                    12 hour time: HOUR:MIN AM/PM 

- n             (integer)           variable holding the current iteration value for the "for...in..." loop in main(), gets 
                                    passed to the print function that tells the user which process is starting, and then is 
                                    passed as an argument to printTime() for each process

- p             (Process)           Process object that holds attributes for each process, in this case each instance that will 
                                    run printTime()
  
----------------------------------------------------------------------------------------------------------------------------------
"""
# Thing To Do 15.1

import multiprocessing
from time import sleep

def printTime(n: int):
    """
    When called, printTime() waits a random amount of time between 0 and 1 seconds, then prints the current time.
    """

    from random import random
    from time import localtime, strftime

    waitTime = random()
    print(f"Program info: Process {n}'s wait time is {waitTime}.")
    sleep(waitTime)

    currTimeST = localtime()
    fmt = """
        24 hour time: %H:%M
        12 hour time: %I:%M %p \n------------------------------"""
    currTimeStr = strftime(fmt, currTimeST)
    print(f"Program info: Generated Structured Time object is \"{currTimeST}\".")

    print(f"""-------------------------------
    Process {n}'s current time is {currTimeStr}""")


def main():
    """
    The main execution function of the program.
    """
    print("Starting processes...")
    for n in range(3):
        print(f"Starting process {n}...")
        p = multiprocessing.Process(target=printTime, args=(n,))
        p.start()
    print("All processes are started.")
    sleep(1.5)
    print("All processes have exited.")


if __name__ == "__main__":
    main()