"""
----------------------------------------------------------------------------------------------------------------------------------
Program Name: Book Thing To Do 13.1-3

Author: Josh Lanier 

SDEV 220

12/4/22

Program Purpose: This program creates a text file called "today.txt", writes today's date to it, then closes it, opens it, reads it
to a variable, then parses the read string to a Structured Time object.

Variables: 

- fileName      (string)            the file name for the "today.txt" file

- todayFile     (TextIOWrapper)     the file object for "today.txt"

- today         (datetime)          the datetime object that holds today's date

- fmt           (string)            the format string for the time string format function "strftime()" and later on the parse function "strptime()"

- todayString1  (string)            the returned string from the time string format function "strftime()" formatting the datetime object 'today'

- file          (TextIOWrapper)     a second file object for "today.txt"

- today_string  (string)            the string read from "today.txt"

- ts_parsed     (Structured Time)   today_string parsed back into a Structured Time object using "strptime()"
   
  

----------------------------------------------------------------------------------------------------------------------------------
"""
# Thing To Do 13.1

from datetime import date

import time

fileName = "today.txt"

print(f"Creating {fileName} and opening it.")

todayFile = open(fileName, 'wt')

today = date.today()

fmt = "%B %d %Y"

todayString1 = today.strftime(fmt)

print(f"Writing to {fileName}: \"{todayString1}\"")

todayFile.write(todayString1)

print(f"Closing {fileName}")

todayFile.close()

# Thing To Do 13.2

fileName = "today.txt"

print(f"Opening {fileName}")

file = open(fileName, 'rt')

print(f"Reading {fileName}...")

today_string = file.read()

print(f"Read \"{today_string}\" from {fileName}.")

print(f"Closing {fileName}")

file.close()

# Thing To Do 13.3

print(f"Parsing contents of {fileName}.")

ts_parsed = time.strptime(today_string, fmt)

print(f"Parsed version of today_string is: \"{ts_parsed}\".")


