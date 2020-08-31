# TODO
from cs50 import SQL
from sys import argv, exit
import csv

def name_split(full_name): #define a function to split up names. call it name_split.
    names = full_name.split() #"Harry James Potter" = ["Harry", "James", "Potter"] names = the split
    return names if len(names) >= 3 else [names [0], None, names[1]] #return the names array if lenth is 3 or more. ELSE if no middle name send 'none' value.

if len(argv) != 2: # (1)
    print("Incorrect number of Arguments")
    exit(1)

db = SQL("sqlite:///students.db") # (2)

csv_path = argv[1] # (3) [argv 1 being name]
with open(csv_path) as csv_file: # (4) store path as file
    reader = csv.DictReader(csv_file) # (5) read file
    for row in reader:
        names = name_split(row["name"]) #insert name_split function
        db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)", #SQL syntax
            names[0], names[1], names[2], row["house"], row["birth"]) # (6) assign rows

 #import and ask correct no of arguments (1)
 #connecting database (2)
 #storing connection in csv path (3)
 #opening path in file (4)
 #dic reader construct (5)
 #partition construct to assign rows but also to sanitize to avoid names with O' or jr. (6)