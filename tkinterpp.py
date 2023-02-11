# gui password generator 

from tkinter import*
from random import randint 

root = Tk()
root.title('Password.com - Strong Password Generator')

root.geometry("500x300")

# Generate random password
def new_rand():
    # clear entry box 
    pw_entry.delete(0, END)

    # Get PW Length, convert to integer 
    pw_length = int(my_entry.get())

    # create a variable to hold a password 
    my_password = ''

    # Loop through password length 
    for x in range(pw_length):
        my_password += chr(randint(33,126))
        
# Output pass to the screen 
    pw_entry.insert(0,my_password)
# copy to clipboard 
def clipper():
    # clear the clipboard
    root.clipboard_clear()
    # copy to clipboard 
    root.clipboard_append(pw_entry.get())

#label frame
lf = LabelFrame(root, text="How many Characters?")
lf.pack(pady=20)

# Create entry box for characters 

my_entry = Entry(lf, font=("Helvetica",24))
my_entry.pack(pady=20, padx=20)

# Create Entry box for returned pass

pw_entry = Entry(root, text='', font=("Helvetica", 24), bd=0, bg="systembuttonface")
pw_entry.pack(pady=20)

# Create a frame for buttons

my_frame = Frame(root)
my_frame.pack(pady=20)

# Create our buttons 

my_button = Button(my_frame, text="Generate Strong Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text= "Copy to Clipboard", command=clipper)
clip_button.grid(row=0, column=1, padx=10)


root.mainloop()