#import tkinter
from tkinter import *
#initialize tkinter as root
root = Tk()

#the following function gives your button it's response to clicks
def my_Click():
    my_Label = Label(root, text="Yup, I'm the result of clicking on that there button.")
    my_Label.pack()


#create the button (what the button is inside[root], and the text="to be inside the button", 
# you can also put in a state=ACTIVE), you can also alter the size of the button with padx=50, and pady=25,
# the 'command=' tag is attached to the function created)
myButton = Button(root, text="Click all up on me!", state=ACTIVE, padx=50, pady=25, command = my_Click)

#place button on the screen
myButton.pack()

#give the main loop for window
root.mainloop()