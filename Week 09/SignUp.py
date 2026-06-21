import tkinter as tk
from tkinter import messagebox


def save_credentials():
    user = username_entry.get().strip()
    pwd = password_entry.get().strip()

    if not user or not pwd:
        messagebox.showerror("Error", "Username and Password cannot be empty")
        return

    with open("credentials.txt", "a") as file:
        file.write(f"{user},{pwd}\n")

    messagebox.showinfo("Success", "Account Created Successfully")

    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


def check_credentials():
    user = username_entry.get().strip()
    pwd = password_entry.get().strip()

    try:
        with open("credentials.txt", "r") as file:
            for line in file:
                stored_user, stored_pwd = line.strip().split(",")

                if user == stored_user and pwd == stored_pwd:
                    messagebox.showinfo("Success", "Login Successful")
                    return

        messagebox.showerror("Error", "Invalid Username or Password")

    except FileNotFoundError:
        messagebox.showerror("Error", "No accounts found. Please sign up first.")


# Main Window
root = tk.Tk()
root.title("Login System")
root.geometry("350x250")
root.resizable(False, False)

# Heading
title_label = tk.Label(root, text="Login System", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Username
tk.Label(root, text="Username").pack()
username_entry = tk.Entry(root, width=30)
username_entry.pack(pady=5)

# Password
tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack(pady=5)

# Buttons
signin_btn = tk.Button(
    root,
    text="Sign In",
    width=15,
    command=check_credentials
)
signin_btn.pack(pady=5)

signup_btn = tk.Button(
    root,
    text="Sign Up",
    width=15,
    command=save_credentials
)
signup_btn.pack(pady=5)

# Run Application
root.mainloop()