import random
import csv
import PySimpleGUI as sg

lowerChars = "abcdefghijklmonpqrstuvwxyz" #lower chars
upperChars = lowerChars.upper() #upper chars using lowers.upper()
numberChars = "1234567890" #numbers
symbolChars = "!@#$%^&*()_" #symbols
allChars = lowerChars + upperChars + numberChars + symbolChars #everything in one string

def generatePassword(): #random int function for generating password
    password = ("") # set blank string
    loopLength = random.randint(8,10) #generate int for how many characters between 8 and 10
    for i in range(loopLength): # for loop to go through for length of how many characters
        randomNumber = random.randint(0,72) # generate a random int between 0 and 72
        password = password + allChars[randomNumber] # select random character from random number on all chars string and add to password

    password = password + upperChars[random.randint(0,25)] # add a upper character
    password = password + symbolChars[random.randint(0, 10)] # add a symbol
    return password # return password and finish function

def asciiGenPassword(): #ascii function for generating password
    password2 = ("")
    loopLength2 = random.randint(10, 12) #generate int for how many characters between 10 and 12
    for i in range(loopLength2): # for loop to go through length of how many characters
        randomNumber2 = random.randint(33, 122) # generate a random int between 33 and 122
        password2 = password2 + chr(randomNumber2) # select random character from random number on all chars string and add to password

    password2 = password2 + chr(random.randint(33, 47)) #add a upper char
    password2 = password2 + chr(random.randint(65, 90)) #add a symbol
    return password2 # return password and finish function

# Set the theme
sg.theme("BrightColors")


# Creating empty lists ready to be appended to
firstNames = []
lastNames = []
emails = []
userpasswords = []
playerRank = []



# Read data from CSV file
with open('DataFiles/user_accounts.csv', 'r') as file:
    # setting the reader to be a csv dictionary reader
    reader = csv.DictReader(file)

    # going through each column
    for col in reader:
        # Taking all the data in each column with the corresponding name and appending it to the list
        firstNames.append(col["first_name"])
        lastNames.append(col["last_name"])
        emails.append(col["email"])
        userpasswords.append(col["password"])
        playerRank.append(col["player_rank"])

# the list that will house all the data columns has other lists inside of it
tabledata = [['First name', 'Last name', 'Email', 'Password', 'Rank']] ### DOUBLE SQUARE BRACKETS BECAUSE LIST INSIDE OF LIST
# for loop to merge each iteration in the 4 lists together and then append them to the list that will be put into the table
for fname, lname, emal, userpas, plrank in zip(firstNames, lastNames, emails, userpasswords, playerRank):
    tabledata.append([fname, lname, emal, userpas, plrank])

# Create the table seperate from the layout
tbl1 = sg.Table(values=tabledata[1:], headings=tabledata[0], ### [1:] to skip first row.
                                                             ### [0] to set the headers as the first list/row in the list
                auto_size_columns=True,
                display_row_numbers=False,
                justification='left', key='table',
                enable_click_events=True,expand_y=False,expand_x=True,size = (5,     15),)

# Create the layout
layout = [[tbl1],
          [[sg.Button("Give Passwords"), sg.Push(),sg.Button("Exit")]]]  # layout of gui

# Create window
window = sg.Window("Prac Sac", layout, icon='', size=(1200, 600), resizable=True)

# while loop to enable button functionality.
while True:
    event, values = window.read()
    if event in (None, "Exit"):
        break # break loop to close then close window
    if event == "Give Passwords": # if the give password button is pressed
        for i, row in enumerate(tabledata):  # to go through every row and column
            if not row[3]:  # if statement to check if password is empty
                # THIS LINE IS VALIDATING WHAT ROWS TO ONLY UPDATE WITH A NEW PASSWORD TO CHECK THAT ONLY EMPTY PASSWORD CELLS IN THE CSV ARE ALLOWED TO BE UPDA
                tabledata[i][3] = generatePassword()  # if it is in the same row ([i]) it using ([-1]) selects the last column of the row and sets it to the rating
        window["table"].update(values=tabledata[1:])  # updates table with searched data

# Close the window
window.close()
