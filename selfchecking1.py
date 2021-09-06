from tkinter import *
import numpy as np
import random
#generates a random 16 digits
digtexts = np.random.randint(2, size=16)
q1check = 0
q2check = 0
q3check = 0
q4check = 0
q5check = 0

#The function to swap 1s to 0s, it is used as the button command
def flipper0():
    #Probably an awful way of swapping a 1 to a 0 but oh well
    dig0["text"] = (str(int((not bool(int(dig0["text"]))))))

def flipper1():
    dig1["text"] = (str(int((not bool(int(dig1["text"]))))))

def flipper2():
    dig2["text"] = (str(int((not bool(int(dig2["text"]))))))

def flipper4():
    dig4["text"] = (str(int((not bool(int(dig4["text"]))))))

def flipper8():
    dig8["text"] = (str(int((not bool(int(dig8["text"]))))))

def checkAnswer():
    global q1check, q2check, q3check, q4check, q5check
    #sets the checks to a new variable so I can put them back afterwards
    oldq1 = q1check
    oldq2 = q2check
    oldq3 = q3check
    oldq4 = q4check
    oldq5 = q5check
    #Sets each label or button to the default background
    dig0["background"] = "SystemButtonFace"
    dig1["background"] = "SystemButtonFace"
    dig2["background"] = "SystemButtonFace"
    dig3["background"] = "SystemButtonFace"
    dig4["background"] = "SystemButtonFace"
    dig5["background"] = "SystemButtonFace"
    dig6["background"] = "SystemButtonFace"
    dig7["background"] = "SystemButtonFace"
    dig8["background"] = "SystemButtonFace"
    dig9["background"] = "SystemButtonFace"
    dig10["background"] = "SystemButtonFace"
    dig11["background"] = "SystemButtonFace"
    dig12["background"] = "SystemButtonFace"
    dig13["background"] = "SystemButtonFace"
    dig14["background"] = "SystemButtonFace"
    dig15["background"] = "SystemButtonFace"

    #Gets the text of each of the buttons
    selzero = dig0["text"]
    selone = dig1["text"]
    seltwo = dig2["text"]
    selfour = dig4["text"]
    seleight = dig8["text"]
    #adds the 1s to the total if the selection is a 1
    q1check += int(selone)
    q2check += int(seltwo)
    q3check += int(selfour)
    q4check += int(seleight)
    q5check += int(selzero) + int(selone) + int(seltwo) + int(selfour) + int(seleight)
    if q1check%2 != 0:
        print("Check the first selection box")
        #Highlights the boxes for this selection
        dig1["background"] = "light blue"
        dig5["background"] = "light blue"
        dig9["background"] = "light blue"
        dig13["background"] = "light blue"
        dig3["background"] = "light blue"
        dig7["background"] = "light blue"
        dig11["background"] = "light blue"
        dig15["background"] = "light blue"
    elif q2check%2 != 0:
        print("Check the second selection box")
        dig2["background"] = "light blue"
        dig6["background"] = "light blue"
        dig10["background"] = "light blue"
        dig14["background"] = "light blue"
        dig3["background"] = "light blue"
        dig7["background"] = "light blue"
        dig11["background"] = "light blue"
        dig15["background"] = "light blue"
    elif q3check%2 != 0:
        print("Check the third selection box")
        dig4["background"] = "light blue"
        dig5["background"] = "light blue"
        dig6["background"] = "light blue"
        dig7["background"] = "light blue"
        dig12["background"] = "light blue"
        dig13["background"] = "light blue"
        dig14["background"] = "light blue"
        dig15["background"] = "light blue"
    elif q4check%2 != 0:
        print("Check the final selection box")
        dig8["background"] = "light blue"
        dig9["background"] = "light blue"
        dig10["background"] = "light blue"
        dig11["background"] = "light blue"
        dig12["background"] = "light blue"
        dig13["background"] = "light blue"
        dig14["background"] = "light blue"
        dig15["background"] = "light blue"
    elif q5check %2 != 0:
        print("You have an odd number of 1s")
    else:
        print("Well done! You got it right!")
    #Puts the checks back to their previous state
    q1check = oldq1
    q2check = oldq2
    q3check = oldq3
    q4check = oldq4
    q5check = oldq5
if __name__ == "__main__":
    #The name of the main thing
    gui = Tk()

    #Adds the "check answer" button
    checkmyanswer = Button(gui, text="Check Answer", command=checkAnswer)

    #Add all the buttons and put them in their place "pady" adds vertical space
    dig0 = Button(gui, text=digtexts[0], command=flipper0)
    dig1 = Button(gui, text=digtexts[1], command=flipper1)
    dig2 = Button(gui, text=digtexts[2], command=flipper2)
    dig4 = Button(gui, text=digtexts[4], command=flipper4)
    dig8 = Button(gui, text=digtexts[8], command=flipper8)
    dig0.grid(row=0,column=0,pady=5)
    dig1.grid(row=0,column=1)
    dig2.grid(row=0,column=2)
    dig4.grid(row=1,column=0)
    dig8.grid(row=2,column=0,pady=5)
    #Make all the rest random, also probably horribly inefficient but it's not a big code so it's fine for now

    dig3 = Label(gui, text=digtexts[3])
    dig5 = Label(gui, text=digtexts[5])
    dig6 = Label(gui, text=digtexts[6])
    dig7 = Label(gui, text=digtexts[7])
    dig9 = Label(gui, text=digtexts[9])
    dig10 = Label(gui, text=digtexts[10])
    dig11 = Label(gui, text=digtexts[11])
    dig12 = Label(gui, text=digtexts[12])
    dig13 = Label(gui, text=digtexts[13])
    dig14 = Label(gui, text=digtexts[14])
    dig15 = Label(gui, text=digtexts[15])

    #Sets all of the positions of each label
    dig3.grid(row=0,column=3)
    dig5.grid(row=1,column=1)
    dig6.grid(row=1,column=2)
    dig7.grid(row=1,column=3)
    dig9.grid(row=2,column=1)
    dig10.grid(row=2,column=2)
    dig11.grid(row=2,column=3)
    dig12.grid(row=3,column=0)
    dig13.grid(row=3,column=1)
    dig14.grid(row=3,column=2)
    dig15.grid(row=3,column=3)

    #Makes sure that "checkanswer" spans across all 4 columns and also has a bit of space from the text
    checkmyanswer.grid(row=4, columnspan=4, pady=5)

    #Numbers 0 through to 15
    for i in range(16):
        #Checks that i is not a power of 2
        if (not (i & (i-1) == 0)):
            #Checks if the last digit is a 1
            if (str(format(i,"04b"))[3]) == "1":
                if digtexts[i] == 1:
                    q1check += 1
            #Checks if the second to last digit is a 1
            if (str(format(i,"04b"))[2]) == "1":
                if digtexts[i] == 1:
                    q2check += 1
            #Checks if the third to last digit is a 1
            if (str(format(i,"04b"))[1]) == "1":
                if digtexts[i] == 1:
                    q3check += 1
            #Checks if the fourth to last digit is a 1
            if (str(format(i,"04b"))[0]) == "1":
                if digtexts[i] == 1:
                    q4check += 1
            #Just checks all of the 1s that aren't the "selector" ones
            if digtexts[i] == 1:
                q5check += 1
    #Runs the system
    gui.mainloop()


