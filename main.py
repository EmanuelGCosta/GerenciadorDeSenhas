from tkinter import *
from tkinter import messagebox
import json
from random import choice, randint, shuffle


def password_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for num in range(randint(8, 10))]
    password_list += [choice(numbers) for num in range(randint(2, 4))]
    password_list += [choice(symbols) for num in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)


def save_data():
    website = website_entry.get().capitalize()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Erro", message="Não deixe nenhum campo vazio")
    else:
        try:
            with open("data.json", "r") as data_json:
                data = json.load(data_json)

        except FileNotFoundError:
            with open("data.json", "w") as data_json:
                json.dump(new_data, data_json, indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w") as data_json:
                json.dump(data, data_json, indent=4)
        finally:
            website_entry.delete(0, END)
            # email_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    website = website_entry.get().capitalize()
    try:
        with open("data.json") as data_json:
            data = json.load(data_json)
    except FileNotFoundError:
        messagebox.showinfo(title="Erro", message="Dados não encontrados")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\n"
                                                       f"Password: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Erro", message=f'Dados de "{website}" não foram encontrados')


window = Tk()
window.title("Gerenciador de senhas")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Webseite:", bg="white")
website_label.grid(column=0, row=1)
website_entry = Entry(width=32)
website_entry.focus()
website_entry.grid(column=1, row=1)

# Email
email_label = Label(text="Email/Username:", bg="white")
email_label.grid(column=0, row=2)
email_entry = Entry()
email_entry.insert(0, "")
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

# Senhas: caixa de entrada e escrita
password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

# Botões
search_button = Button(text="Search", bg="white", command=find_password, width=14)
search_button.grid(column=2, row=1)
generate_button = Button(text="Generate Password", bg="white", command=password_generate, width=14)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", bg="white", width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
