import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    if len(password_entry.get()) != 0:
        password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = ''.join(password_list)
    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    error = False
    new_data = {
        website_entry.get(): {
            "email": email_entry.get(),
            "password": password_entry.get(),
        }
    }
    if email_entry.get() == "":
        messagebox.showinfo(title="OOPS!", message="no email")
        error = True
    elif website_entry.get() == "":
        messagebox.showinfo(title="OOPS!", message="no website")
        error = True
    elif password_entry.get() == "":
        messagebox.showinfo(title="OOPS!", message="no password")
        error = True

    if not error:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def search():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            website = website_entry.get()
            login = data[website]["email"]
            password = data[website]["password"]
        messagebox.showinfo(title=f"{website}", message=f"Login: {login}\nPassword: {password} ")

    except (KeyError, FileNotFoundError):
        messagebox.showinfo(title="OOPS!", message="There is no data for this website")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky=E)

website_entry = Entry(width=24)
website_entry.focus()
website_entry.grid(column=1, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky=E)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "bgdanterty@gmail.com")
password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky=E)

password_entry = Entry(width=24)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate", width=6, command=generate)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=33, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=6, command=search)
search_button.grid(column=2, row=1)

window.mainloop()
