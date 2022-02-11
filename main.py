from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

#---- Password generator ----#
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for i in range(randint(8,10))]
    password_symbols = [choice(symbols) for i in range(randint(2,4))]
    password_numbers = [choice(numbers) for i in range(randint(2,4))]
    password_list = password_letter + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    input3.insert(0, password)
    pyperclip.copy(password)



#---- Save Password ----#
def save():
    website = input1.get()
    email = input2.get()
    password = input3.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='oops', message='You have to fill this out.')
    else:
        is_good = messagebox.askokcancel(title=f'{website}', message=f'These are the details you entered: \n Email:{email} '
                                                           f'\n Password:{password} \n Is it okay to save this?')

        if is_good:
            with open('data.txt', 'a') as data:
                data.write(f'{website} | {email} | {password}\n')
                input1.delete(0,END)
                input3.delete(0,END)

#---- UI Setup ---#

window = Tk()
window.title('Password Generator')
window.config(padx=20, pady=20)
window.minsize(200, 200)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)


website = Label(text='Website:')
website.grid(column=0, row =1,columnspan=1)

input1 = Entry(width=35)
input1.grid(column=1, row=1, columnspan=2)

Username= Label(text='Username/Email:')
Username.grid(column=0, row=2,columnspan=1)

input2 = Entry(width=35)
input2.insert(0,'example@email.com')
input2.grid(column=1, row=2, columnspan=2)

password = Label(text='Password:')
password.grid(column=0, row=3, columnspan=1)

input3 = Entry(width=20)
input3.grid(column=1, row=3)

generate_password = Button(text='Generate password', width = 15, command=generate)
generate_password.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()