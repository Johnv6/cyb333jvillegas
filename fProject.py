
#John Glenn Villegas

#stores the events
total = []
tWarn = []
tError = []
tInfo = []
tCrit = []

with open('logs.txt') as f: #opens the text file.
    line2 = f.readlines() #reads the lines.

    for line in line2: #reads every line in the text file.
        if "Warning" in line:
            total.append(line)
            tWarn.append(line)
        if "Error" in line:
            total.append(line)
            tError.append(line)
        if "Information" in line:
            total.append(line)
            tInfo.append(line)
        if "Critical" in line:
            total.append(line)
            tCrit.append(line)

total = '\n'.join(total) #separates each result in the list.

#-------------------------------------------------------------------------

check = False
while check != True: #keeps asking questions until user is done.
    #information below of the choices and number of events.
    print("-------------------------------------------------------")
    print("\nSorts files according to the choices below: \n")
    print("[1] Warning     (" + str(len(tWarn)) + " events)")
    print("[2] Error       (" + str(len(tError)) + " events)")
    print("[3] Information (" + str(len(tInfo)) + " events)")
    print("[4] Critical    (" + str(len(tCrit)) + " events)")
    print("\nTotal Events: " + str(len(total)) + "\n")
    print("[0] To end program.")
    print("Hit [Enter] to view all events.") #hitting enter displays the entire file.
    print("-------------------------------------------------------")

    word = input("Choose a number: ") #user are asked to type something.
    print("\n")
    #The choices below determine the results.
    if word == "1":
        word = "Warning"
    elif word == "2":
        word = "Error"
    elif word == "3":
        word = "Information"
    elif word == "4":
        word = "Critical"
    elif word == "0": #Entering 0 will end the program.
        print('Program Done!')
        break
    else:
        print("\n[----Enter valid numbers only----]\n")


    list = [] #used to store the content of the file.

    with open('logs.txt') as f: #opens the text file.
        lines = f.readlines() #reads the lines.

        for line in lines: #reads every line in the text file.
            if word in line: #if the entered word is in file..
                list.append(line) #add that entire line to list.

    list = '\n'.join(list) #separates each result in the list.

    print(list) #displays all the results.
