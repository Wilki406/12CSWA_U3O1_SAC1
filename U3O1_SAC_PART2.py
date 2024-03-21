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

data = 'testuser_accounts.csv'
records = []
lbox = []

headers = ["first_name","last_name","email","password","player_rank"] #list of headers


with open(data, 'r') as file: #read data
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        firstNames = row[0]
        lastNames = row[1]
        email = row[2]
        pword = row[3]
        playerRank = row[4]

        records.append([firstNames, lastNames, email, pword, playerRank])

for i in range(len(records)):
    lbox.append("{:<15} {:<15} {:<40} {:<15} {:<5}".format(records[i][0],records[i][1],records[i][2],records[i][3],records[i][4]))


sg.theme('DarkGrey10')
sg.set_options(font='Courier 11')

column = [[sg.Text("{:<15} {:<15} {:<40} {:<15} {:<5}".format('First name', 'Last name', 'Email', 'Password', 'Rank'), size=(96,1))],
          [sg.Listbox(lbox, key='listington', size=(93, 15)),],
          [sg.Button('Give Passwords', size=(20, 1)), sg.Exit(size=(8,1))]]

column2 = [[sg.Text("User Details:"), sg.Push()],
           [sg.Text("First name:"), sg.Input(key="fnameinput", size=(20, 1),)],
           [sg.Text("Last name:"), sg.Input(key="lnameinput", size=(20, 1),)],
           [sg.Text("Email:"), sg.Input(key="emailinput", size=(20, 1),)],
           [sg.Text("Password:"), sg.Input(key="passwordinput", size=(20, 1),)],
           [sg.Button("Add New")]]


layout = [[sg.Column(column),sg.VSeperator(), sg.Column(column2)]] # layout for the gui

# set the window information as per scope
window = sg.Window('Arcade Quest - System Admin, User Account Manager Pro', layout, resizable=True, location=(0,0), margins=(30,30), text_justification='middle', size=(1400,600))

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit': #exit if button if pressed
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


    if event == "Add New": # if add new button is clocked
        inputedfname = str(values["fnameinput"]) # get the new first name
        inputedlname = str(values["lnameinput"]) # get the new last name
        inputedemail = str(values["emailinput"]) # get the new email
        inputedpassword = str(values["passwordinput"]) # get the new password
        pRanks = [] # make new list for people ranks
        pRanks.append(int(playerRank)) # fill new list with player rank column as integers not strings


        if not inputedfname:  # check to see if data is present
            sg.popup_error("Please enter data into the firstname field!")  # give the user an error saying to enter required data
            continue  # restart the loop to belay the rating
        if not inputedlname:
            sg.popup_error("Please enter data into the lastname field!")  # give the user an error saying to enter required data
            continue  # restart the loop to belay the rating
        if not inputedemail:
            sg.popup_error("Please enter data into the email field!")  # give the user an error saying to enter required data
            continue  # restart the loop to belay the rating
        if not inputedpassword:
            sg.popup_error("Please enter data into the password field!")  # give the user an error saying to enter required data
            continue  # restart the loop to belay the rating






        userDesRank = pRanks[-1] + 1 # user designated rank = last the value in the column of pranks +1
        newlist = [inputedfname, inputedlname, inputedemail, inputedpassword, userDesRank] # make new list from entered data

        with open('testuser_accounts.csv', 'w', newline='') as file:  # open / make the new csv file in write mode
            # newline='' ensures that the file object does not perform any newline translation
            writer = csv.writer(file)  # set the csv writer
            writer.writerow(headers)  # write the headings as the CORRECT headings
            writer.writerows(records)  # write the data to the new csv file
            writer.writerow(newlist) # write a new row of new list data

        lbox.clear() # clear current data inside list box
        records.clear() # clear current data inside records
        with open(data, 'r') as file: # open file
            reader = csv.reader(file) # select the csv reader to read data
            next(reader) # read but skip the header

            # get the data from each row
            for row in reader:
                firstNames = row[0]
                lastNames = row[1]
                email = row[2]
                pword = row[3]
                playerRank = row[4]

                # fill records with new data
                records.append([firstNames, lastNames, email, pword, playerRank])

        for i in range(len(records)): # append new record data to listbox
            lbox.append(
                "{:<15} {:<15} {:<40} {:<15} {:<5}".format(records[i][0], records[i][1], records[i][2], records[i][3],
                                                           records[i][4]))
        window['listington'].update(values=lbox)  # updates table with new data

window.close() #close window
