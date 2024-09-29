from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol =[choice(symbols) for _ in range(randint(2, 4))]
    password_number =[choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_number+password_letter+password_letter
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username= username_entry.get()
    password =password_entry.get()
    new_data = {
        website:{
            "email":username,
            "password": password
        }
    }
    # To check is the entry is left blank
    if len(website) == 0 or len(password)==0:
        messagebox.showerror(title= "Incomplete form", message = "Please complete all required field")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
                print(data)

        except FileExistsError:
            with open("data.json", "w") as data_file:
            # saving updated data
                json.dump(new_data, data_file, indent= 4)

        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent= 4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- Search ------------------------------- #

def search():
    print("Active button")
    item = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
        # Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No data named {item} file found")
    else:
        if item in data:
            username = data[item]["email"]
            password = data[item]["password"]
            messagebox.showinfo(title =  "Search result", message=f"Email: {username} \n Password:  {password}")
            print(username + password)
        else:
            messagebox.showinfo(title="Error", message=f"No detail for {item} exist")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.minsize(width=500, height=500)
window.config(padx = 50, pady = 50)


canvas = Canvas(width=200, height=200)
Lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=Lock_img)
canvas.grid(row= 0, column = 1, sticky="W")

#Website
website_label = Label(text ="Website: ")
website_label.grid(row= 1, column = 0)

website_entry = Entry(width=33)
website_entry.grid(row= 1, column = 1, columnspan= 2, sticky="W")
website_entry.focus()
# Username
username_label = Label(text ="Email/Username: ")
username_label.grid(row= 2, column = 0)
username_entry = Entry(width=50)
username_entry.insert(0,"mails.tim@yahoo.com")
username_entry.grid(row= 2, column = 1, columnspan= 2, sticky="W")

# Password
password_label = Label(text ="Password: ")
password_label.grid(row= 3, column = 0)
password_entry = Entry(width=33)
password_entry.grid(row= 3, column = 1, sticky="W")


# Buttons
generate_button = Button(text="Generate Button", command=generate_password, width=13)
generate_button.grid(row= 3,column=2, sticky="W")

add_button = Button(text="Add", command=save)
add_button.config(width=42)
add_button.grid(row= 4,column=1, columnspan= 2, sticky="W")

search_button = Button(text="Search Button", command=search, width=13)
search_button.grid(row= 1,column=2, sticky="W")


window.mainloop()