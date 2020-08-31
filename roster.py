# TODO
from sys import argv
from cs50 import SQL

if len(argv) != 2:
    print("Incorrect Arguments")
    exit(1)

db = SQL("sqlite:///students.db") #from students DB query student entered
hogwarts_house = argv[1]
rows = db.execute("SELECT * FROM students WHERE house = ? ORDER BY last, first", hogwarts_house) #SQL syntax to navigate tables
for row in rows:
    first, middle, last, birth = row["first"], row["middle"], row["last"], row["birth"]
    print(f"{first} {middle + ' ' if middle else ''}{last}, born{birth}")


#check arguements
#open db
#take house
#query database
#? meaning house
#for rows {} construct we are making sure to avoid middle name problem.