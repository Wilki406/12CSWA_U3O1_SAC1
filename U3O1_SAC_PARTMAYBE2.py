import random
import csv
import PySimpleGUI as sg

lowerChars = "abcdefghijklmonpqrstuvwxyz"  # lower chars
upperChars = lowerChars.upper()   # upper chars using lowers.upper()
numberChars = "1234567890"  # numbers
symbolChars = "!@#$%^&*()_"  # symbols
allChars = lowerChars + upperChars + numberChars + symbolChars  # everything in one string

# random int function for generating password
def generatePassword():
    password = ("") # set blank string
    loopLength = random.randint(8,10)  # generate int for how many characters between 8 and 10
    for i in range(loopLength):  # for loop to go through for length of how many characters
        randomNumber = random.randint(0,72)  # generate a random int between 0 and 72
        password = password + allChars[randomNumber]  # select random character from random number on all chars string # and add to password

    password = password + upperChars[random.randint(0,25)] # add a upper character
    password = password + symbolChars[random.randint(0, 10)] # add a symbol
    return password  # return password and finish function

# ascii function for generating password
def asciiGenPassword():
    password2 = ("")
    loopLength2 = random.randint(10, 12)  # generate int for how many characters between 10 and 12
    for i in range(loopLength2):  # for loop to go through length of how many characters
        randomNumber2 = random.randint(33, 122)  # generate a random int between 33 and 122
        password2 = password2 + chr(randomNumber2)  # select random character from random number on all chars string and add to password

    password2 = password2 + chr(random.randint(33, 47))  # add a upper char
    password2 = password2 + chr(random.randint(65, 90))  # add a symbol
    return password2  # return password and finish function

# Set the theme
sg.theme("BrightColors")

data = 'user_accounts.csv'
records = []
lbox = []
pRanks = []
dataState = 0
foreverRecords = []
with open(data, 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        firstNames = row[0]
        lastNames = row[1]
        email = row[2]
        pword = row[3]
        playerRank = row[4]

        pRanks.append(int(playerRank))
        records.append([firstNames, lastNames, email, pword, playerRank])

for i in range(len(records)):
    lbox.append("{:<15} {:<15} {:<40} {:<15} {:<5}".format(records[i][0],records[i][1],records[i][2],records[i][3],records[i][4]))


with open(data, 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        firstNames = row[0]
        lastNames = row[1]
        email = row[2]
        pword = row[3]
        playerRank = row[4]

        foreverRecords.append([firstNames, lastNames, email, pword, playerRank])


print(pRanks)
sg.theme('DarkGrey10')
sg.set_options(font='Courier 11')

column = [[sg.Text("{:<15} {:<15} {:<40} {:<15} {:<5}".format('First name', 'Last name', 'Email', 'Password', 'Rank'), size=(150,1))],
          [sg.Listbox(lbox, key='listington', size=(130, 15)),],
          [sg.Button('Give Passwords', size=(20, 1), pad=((5,5),(20,0))), sg.Button('Sort', size=(20, 1), pad=((5,5),(20,0))), sg.Exit(size=(8,1), pad=((5,5), (20,0)))]]

layout = [[sg.Column(column)]]

window = sg.Window('Arcade Quest - System Admin, User Account Manager Pro', layout, resizable=True, location=(0,0), margins=(30,30), text_justification='left', size=(1200,600))



while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == "Give Passwords":  # if the give password button is pressed
        for i, row in enumerate(records):  # to go through every row and column
            if not row[3]:  # if statement to check if password is empty
                # THIS LINE IS VALIDATING WHAT ROWS TO ONLY UPDATE WITH A NEW PASSWORD TO CHECK THAT ONLY EMPTY PASSWORD CELLS IN THE CSV ARE ALLOWED TO BE UPDA
                records[i][3] = generatePassword()  # if it is in the same row ([i]) it using ([-1]) selects the last column of the row and sets it to the rating

        # Clear the lbox list
        lbox.clear()

        # Update the lbox list with the new formatted records
        for i in range(len(records)):
            lbox.append("{:<15} {:<15} {:<40} {:<15} {:<5}".format(records[i][0], records[i][1], records[i][2],
                                                                   records[i][3], records[i][4]))
        window['listington'].update(values=lbox)  # updates table with new data

    if event == "Sort" and dataState == 0:
        print("AHHAHA")
        lbox.clear()
        # Sort records by player rank using selection sort
        for i in range(len(pRanks)):
            smallest = i
            for k in range(i + 1, len(pRanks)):
                if pRanks[k] < pRanks[smallest]:
                    smallest = k
            pRanks[i], pRanks[smallest] = pRanks[smallest], pRanks[i]
            records[i], records[smallest] = records[smallest], records[i]

        # Clear the lbox list
        lbox.clear()

        # Update the lbox list with the new formatted records
        for i in range(len(records)):
            lbox.append(
                "{:<15} {:<15} {:<40} {:<15} {:<5}".format(records[i][0], records[i][1], records[i][2], records[i][3],
                                                           records[i][4]))

        # Update the GUI table with the sorted data
        window['listington'].update(values=lbox)
        dataState = 1
        print(dataState)

    elif event == "Sort" and dataState == 1:
        print("bingo")
        # Sort records by player rank using selection sort
        for i in range(len(pRanks)):
            smallest = i
            for k in range(i + 1, len(pRanks)):
                if pRanks[k] > pRanks[smallest]:
                    smallest = k
            pRanks[i], pRanks[smallest] = pRanks[smallest], pRanks[i]
            records[i], records[smallest] = records[smallest], records[i]

        # Clear the lbox list
        lbox.clear()

        # Update the lbox list with the new formatted records
        for i in range(len(records)):
            lbox.append(
                "{:<15} {:<15} {:<40} {:<15} {:<5}".format(records[i][0], records[i][1], records[i][2], records[i][3],
                                                           records[i][4]))

        # Update the GUI table with the sorted data
        window['listington'].update(values=lbox)
        dataState = 2

    elif event == "Sort" and dataState == 2:
        print("REEEE")

        lbox.clear()

        for i in range(len(foreverRecords)):
            lbox.append(
                "{:<15} {:<15} {:<40} {:<15} {:<5}".format(foreverRecords[i][0], foreverRecords[i][1], foreverRecords[i][2], foreverRecords[i][3],
                                                           foreverRecords[i][4]))

        # Update the GUI table with the sorted data
        window['listington'].update(values=lbox)
        dataState = 0

window.close()
