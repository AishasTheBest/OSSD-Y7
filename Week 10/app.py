import tkinter as tk
from tkinter import messagebox

# login reading from file
def read_file():

    users = {}

    try:
        with open("users.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                users[username] = password

    except FileNotFoundError:
        pass

    return users


def write_file(username, password):

    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")


def login():

    username = username_entry.get()
    password = password_entry.get()

    users = read_file()

    if username in users and users[username] == password:
        messagebox.showinfo("Success", "Login Successful")

    else:
        messagebox.showerror("Error", "Invalid Username or Password")


def signup():

    username = username_entry.get()
    password = password_entry.get()

    users = read_file()

    if username in users:
        messagebox.showerror("Error", "Username already exists")

    else:
        write_file(username, password)
        messagebox.showinfo("Success", "Signup Successful")


def main():

    global username_entry, password_entry

    # Username Label
    username_label = tk.Label(root, text="Username")
    username_label.pack(pady=5)

    # Username Entry
    username_entry = tk.Entry(root)
    username_entry.pack(pady=5)

    # Password Label
    password_label = tk.Label(root, text="Password")
    password_label.pack(pady=5)

    # Password Entry
    password_entry = tk.Entry(root, show="*")
    password_entry.pack(pady=5)

    # Login Button
    login_button = tk.Button(root, text="Login", command=login)
    login_button.pack(pady=5)

    # Signup Button
    signup_button = tk.Button(root, text="Signup", command=signup)
    signup_button.pack(pady=5)


root = tk.Tk()
root.title("Login System")
root.geometry("300x250")

main()

root.mainloop()