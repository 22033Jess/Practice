# docstring - Jess Williams airplane database
# imports
import sqlite3

# constants and variables
DATABASE = "fighters.db"


# functions
def print_all_aircraft():
    '''print all the aircraft nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from fighter;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all of the results
    print("name                          speed   max_g climb range payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    #loop finished here
    db.close()



# main code
while True:
    user_input = input("\nWhat would you like to do? \n1 Print all aircraft\n2 Exit\n")
    if user_input == "1":
        print_all_aircraft()
    elif user_input == "2":
        break
    else:
        print("That was not an option\n")
