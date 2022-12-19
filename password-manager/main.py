from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    web = web_type.get()
    try:
        with open("data.json", "r") as file:
            all_data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if web in all_data:
            post_password = all_data[web]["password"]
            email = all_data[web]["email"]
            messagebox.showinfo(title=web, message=f" Email: {email}\n password: {post_password}")
        else:
            messagebox.showinfo(title="Not find", message=f"{web} have not add")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gerenate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
               'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(1, 3))]

    password_symbol = [choice(symbols) for _ in range(randint(1, 3))]

    password_number = [choice(numbers) for _ in range(randint(1, 3))]

    password_list = password_letter + password_symbol + password_number
    shuffle(password_list)

    password = "".join(password_list)
    pass_ent.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = web_type.get()
    email_name = name_ent.get()
    password = pass_ent.get()
    new_data = {
        website: {
            "email": email_name,
            "password": password,
        }
    }

    if len(website) < 1 or len(password) < 1:
        messagebox.showinfo(title="Oop", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            web_type.delete(0, END)
            pass_ent.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(heigh=200, width=200, bg="white", highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Label
web_lab = Label(text="Website:", bg="white")
web_lab.grid(column=0, row=1)
name_lab = Label(text="Email/Username:", bg="white")
name_lab.grid(column=0, row=2)
pass_lab = Label(text="Password:", bg="white")
pass_lab.grid(column=0, row=3)

#Entries
web_type = Entry(width=20)
web_type.grid(column=1, row=1)
# enter first in the website entry
web_type.focus()
name_ent = Entry(width=45)
name_ent.grid(column=1, row=2, columnspan=2)
name_ent.insert(0, "wayne@gmail.com")
pass_ent = Entry(width=20)
pass_ent.grid(column=1, row=3)

# Add Button
add_but = Button(text="Add", width=36, command=save)
add_but.grid(column=1, row=4, columnspan=2)

# Germinate Buttons
generate_password_button = Button(text="Generate Password", width=20, command=gerenate_password)
generate_password_button.grid(row=3, column=2)
# Search
search_button = Button(text="Search", width=20, command=find_password)
search_button.grid(row=1, column=2)
window.mainloop()
