import tkinter.messagebox
from tkinter import *

root = Tk()
root.title('Printing Dollars')
root.geometry('400x300')


def Money():
    if slider.get() > 0:
        tkinter.messagebox.showinfo(title='Money Credited!', message=f'Congratulations!! ${slider.get()} has been '
                                                                 f'successfully credited to your Bank Account.')

    else:
        tkinter.messagebox.showerror(title='Error occurred!!', message="Sorry! You didn't get anything!! coose to get "
                                                                       "some money")


Label(text="How many dollars do you want in your Account?").grid(row=0, column=1)
slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=50, fg='blue', bg='lightgrey')
slider.grid(row=1, column=1)

Button(text='Get your money', bg='lightskyblue', command=Money).grid(row=3, column=1)

root.mainloop()
