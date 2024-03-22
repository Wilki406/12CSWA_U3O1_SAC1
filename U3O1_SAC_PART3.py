import random  # random module
import csv  # csv module
import PySimpleGUI as sg  # psg module

lowerChars = "abcdefghijklmonpqrstuvwxyz"  # lower chars
upperChars = lowerChars.upper()   # upper chars using lowers.upper()
numberChars = "1234567890"  # numbers
symbolChars = "!@#$%^&*()_"  # symbols
allChars = lowerChars + upperChars + numberChars + symbolChars  # everything in one string

# I HAVE USED SELECTION SORT AS IT WAS THE ONLY SORTING FUNCTION I KNEW HOW TO CODE :)
# plus selection sort is easy to change to be highest to lowest and then to lowest to highest
def sortRecords(records, pRanks, order): # function to sort the order of records
    for i in range(len(pRanks)):  # iterate through the length of elements
        smallest = i  # assume current value is the lowest
        for k in range(i + 1, len(pRanks)):  # iterate through the unsorted portion of the list to find the minimum
            if order == "asc" and pRanks[k] < pRanks[smallest]: # if the current element is < than the element update min index and order is asc
                smallest = k  # swap current element with lowest element
            elif order == "desc" and pRanks[k] > pRanks[smallest]: # if the current element is < than the element update min index and order is desc
                smallest = k  # swap current element with lowest element
        pRanks[i], pRanks[smallest] = pRanks[smallest], pRanks[i] # Swap the current element with the minimum element found
        records[i], records[smallest] = records[smallest], records[i] # Swap the current iteration of records with the smallest record iteration

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

data = 'testuser_accounts.csv'  # csv file
records = []  # records string
lbox = []  # lbox string
pRanks = []  # playerRanks string or pranks string
dataState = 0  # data state
foreverRecords = []  # forever records string
headers = ["first_name","last_name","email","password","player_rank"]  # list of headers
searchResults = 0  # search results integer


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

#print(pRanks)  # testing purposes
sg.theme('DarkGrey10')  # set the theme to the mr fits theme
sg.set_options(font='Courier 11')  # font to courier 11

# columns for layout
# enable events needs to be true for the listbox and the input box
column = [[sg.Button('Sort', size=(20, 1))],[sg.Text("Search: "),sg.Input(key="filteredsearch",enable_events=True,size=(30, 1)), sg.Text("", key="results")],
          [sg.Text("{:<15} {:<15} {:<40} {:<15} {:<5}".format('First name', 'Last name', 'Email', 'Password', 'Rank'), size=(96,1))],
          [sg.Listbox(lbox, key='listington', size=(93, 15),enable_events=True),],
          [sg.Button('Give Passwords', size=(20, 1)), sg.Exit(size=(8,1))]]

column2 = [[sg.Text("User Details:"), sg.Push()],
           [sg.Text("First name:"), sg.Input(key="fnameinput", size=(20, 1),)],
           [sg.Text("Last name:"), sg.Input(key="lnameinput", size=(20, 1),)],
           [sg.Text("Email:"), sg.Input(key="emailinput", size=(20, 1),)],
           [sg.Text("Password:"), sg.Input(key="passwordinput", size=(20, 1),)],
           [sg.Button("Add New")]]

# layout to have column 1 then a Vseperator and then column 2
layout = [[sg.Column(column),sg.VSeperator(), sg.Column(column2)]] # layout for the gui


# set the window
window = sg.Window('Arcade Quest - System Admin, User Account Manager Pro', layout, resizable=True, location=(0,0), margins=(30,30), text_justification='left', size=(1300,600))


#while loop to do stuff and that
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit': #if exit button pressed end the while loop
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
        window['results'].update(f"") # update the results text to 'none'

    if event == "Sort":  # if sort button is pressed
        if dataState == 0:  # if datastate is set to 0
            sortRecords(records, pRanks, "asc")  # use the sort function with inputs of records, pranks, and in ascending order
            dataState = 1  # then make datastate set to 1
        elif dataState == 1:  # if datastate is set to 1
            sortRecords(records, pRanks, "desc")  # use the sort function with inputs of records, pranks, and in descending order
            dataState = 2  # then make datastate set to 2
        else:  # if datastate is 2
            records = foreverRecords.copy()  # make records equal to a copy of foreverRecords which is records that never changes
            pRanks = [int(row[4]) for row in records]  # make p ranks set to a list of ints for each row in records
            dataState = 0  # make data state set to 0

        lbox.clear()
        for i in range(len(records)):
            lbox.append("{:<15} {:<15} {:<40} {:<15} {:<5}".format(records[i][0], records[i][1], records[i][2],
                                                                   records[i][3], records[i][4]))
        window['listington'].update(values=lbox)
        window['results'].update(f"")  # update the results text to 'none'

    if event == "Add New":  # if add new button is pressed

        inputedfname = str(values["fnameinput"])  # get the new first name
        inputedlname = str(values["lnameinput"])  # get the new last name
        inputedemail = str(values["emailinput"])  # get the new email
        inputedpassword = str(values["passwordinput"])  # get the new password
        pRanks = []  # make new list for people ranks
        pRanks.append(int(playerRank))  # fill new list with player rank column as integers not strings

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

        userDesRank = pRanks[-1] + 1 # user designated rank = last the value in the column of pRanks +1
        newlist = [inputedfname, inputedlname, inputedemail, inputedpassword, userDesRank] # make new list from entered data

        with open(data, 'w', newline='') as file:  # open / make the new csv file in write mode
            # newline='' ensures that the file object does not perform any newline translation
            writer = csv.writer(file)  # set the csv writer
            writer.writerow(headers)  # write the headings as the CORRECT headings
            writer.writerows(foreverRecords)  # write the data to the new csv file
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
        window['results'].update(f"")  # update the results text to 'none'


    if values['filteredsearch'] != '':  # if a key is entered in search field
        search = values['filteredsearch'].lower()  # convert search string to lowercase

        newValues = [] # make new list called newValues
        #print("EVENT") # see if searching works
        lbox.clear() # clear the data inside lbox
        newNewValues = []  # make a new list
        with open(data, 'r') as file:  # Open dataset in read mode to go through each row to find both text
            reader = csv.reader(file) # set the reader for the file
            next(reader)  # Skip the header row
            for row in reader:
                if search in row[0].lower():  # check if search string is present in the first column
                    newValues.append(','.join(row))  # join the columns back into a comma separated string
                elif search in row[1].lower():  # check if search string is present in the first column
                    newValues.append(','.join(row))  # join the columns back into a comma seperated string

        for value in newValues: # for each value in the new values
            newNewValues.append(value.split(','))  # put the comma separated string into a list
        #print(newValues)
        #print(newNewValues)

        for i in range(len(newNewValues)):  # append new record data to listbox
            lbox.append(
                "{:<15} {:<15} {:<40} {:<15} {:<5}".format(newNewValues[i][0], newNewValues[i][1], newNewValues[i][2], newNewValues[i][3],
                                                           newNewValues[i][4]))

        window['listington'].update(values=lbox)  # updates table with new data


        searchResults = len(newNewValues)  # search results is equal to how many rows when searched
        window['results'].update(f"{(str(searchResults))} results")  # update it with f string to say how many results
        if values['filteredsearch'] == '':  # idk if this works but it's meant to and causes no errors so its here
            window['results'].update(f"")  # update with nothing
        if searchResults == 0:  # if there are no search results
            window['results'].update(f"No entries found with that keyword")  # print the thing i needed to say

        if values['filteredsearch'] == 'Benjamin Wilkinson':
            window['results'].update(f"YOU FOUND AN EASTER EGG")

window.close()  # close the window if while loop ends
