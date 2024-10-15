import sqlite3
import json

con = sqlite3.connect("tutorial.db")
cur = con.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
    userName        text
                    not null, 
    userID          integer
                    not null, 
    userPass        text
                    not null
    )""")
    
#code
def newUsers(nserName, userID, userPass):
    cur.execute("""INSERT INTO users(userName, userID, userPass) VALUES(?, ?, ?)""", (nserName, userID, userPass))
    con.commit()
    return nserName, userID, userPass
              
def select_task_by_priority(userID):
    cur.execute("SELECT * FROM users WHERE priority=?", (userID == userID))
    rows = cur.fetchall()
    return rows

                

def dolist(arg):
    if arg == "newUser":
        return newUsers(newUser.get("userName"), newUser.get("userID"), newUser.get("userPass"))
    elif arg == "openAkk":
        return select_task_by_priority(newUser.get("userID"))

f = open("newUser.json")
newUser = json.load(f)
f.close
print(dolist(newUser.get("do")))
