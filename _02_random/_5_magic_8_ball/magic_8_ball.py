import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    question = simpledialog.askstring(title='8 Ball', prompt= "What is a question you want the 8 ball to answer?")
    # Make a variable and initialize it to a random number between 0 and 3
    rand = random.randint(0, 3)
    # If the random number is 0
    if rand == 0:
        # tell the user "Yes"
        messagebox.showinfo(message="Yes")
    # If the random number is 1
    if rand == 1:
        # tell the user "No"
        messagebox.showinfo(message="No")
    # If the random number is 2
    if rand == 2:
        # tell the user "Maybe you should ask Google?"
        messagebox.showinfo(message="Maybe you should ask Google?")
    # If the random number is 3
    if rand == 3:
        # write your own answer
        messagebox.showinfo(message="Hmmmm. I'm not so sure.")
