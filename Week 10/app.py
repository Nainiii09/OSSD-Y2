import tkinter as tk
from tkinter import messagebox

# -----------------------
# Sign In Function
# -----------------------
def sign_in():
    username = username_entry.get()
    password = password_entry.get()

    try:
        with open("credentials.txt", "r") as file:
            for line in file:
                stored_user, stored_pass = line.strip().split(",")

                if username == stored_user and password == stored_pass:
                    messagebox.showinfo("Success", "Login Successful")
                    return

        messagebox.showerror("Error", "Invalid Credentials")

    except FileNotFoundError:
        messagebox.showerror("Error", "No users found. Please sign up first.")


# -----------------------
# Sign Up Function
# -----------------------
def sign_up():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "Fields cannot be empty")
        return

    with open("credentials.txt", "a") as file:
        file.write(f"{username},{password}\n")

    messagebox.showinfo("Success", "Account Created")


# -----------------------
# Sign In Window
# -----------------------
def sign_in_window():
    clear_window()

    tk.Label(root, text="Sign In", font=("Arial", 16)).pack(pady=10)

    global username_entry, password_entry

    tk.Label(root, text="Username").pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    tk.Button(root, text="Login", command=sign_in).pack(pady=5)

    tk.Button(root,
              text="Go To Sign Up",
              command=sign_up_window).pack()


# -----------------------
# Sign Up Window
# -----------------------
def sign_up_window():
    clear_window()

    tk.Label(root, text="Sign Up", font=("Arial", 16)).pack(pady=10)

    global username_entry, password_entry

    tk.Label(root, text="Username").pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    tk.Button(root, text="Create Account",
              command=sign_up).pack(pady=5)

    tk.Button(root,
              text="Go To Sign In",
              command=sign_in_window).pack()


# -----------------------
# Clear Window
# -----------------------
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()


# -----------------------
# Main Menu
# -----------------------
def main_menu():
    clear_window()

    tk.Label(root,
             text="Welcome",
             font=("Arial", 16)).pack(pady=20)

    tk.Button(root,
              text="Sign In",
              width=15,
              command=sign_in_window).pack(pady=5)

    tk.Button(root,
              text="Sign Up",
              width=15,
              command=sign_up_window).pack(pady=5)


# -----------------------
# Root Window
# -----------------------
root = tk.Tk()
root.title("Application")
root.geometry("300x250")

main_menu()

root.mainloop()