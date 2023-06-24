import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket
    lottery_num = ""
    for i in range (6):
        rand = random.randint(0, 100)
        lottery_num += str(rand) + "  "
    # TODO 2) Display the selected numbers to the user in a pop-up
    messagebox.showinfo(title = "Lottery Ticket", message = lottery_num)
    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
