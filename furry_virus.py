import tkinter as tk
import os
import sys
import random

file_dir = os.path.dirname("cat.jpg")
sys.path.append(file_dir)

import subprocess
subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])

from PIL import Image, ImageTk

file_name = None

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

def file_path(file_name):
    return os.path.join(script_dir, str(file_name))

def center_root(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - width) // 2
    y_position = (screen_height - height) // 2
    root.geometry(f"{width}x{height}+{x_position}+{y_position}")

def on_focus_in(event):
    event.widget.config(highlightbackground="#c0e4f3", highlightcolor="#c0e4f3", highlightthickness=2)

def on_focus_out(event):
    event.widget.config(highlightbackground="#d9dbdb", highlightcolor="#d9dbdb", highlightthickness=2)

def main():
    global root
    global card_entry
    global expiry_entry
    global security_entry

    # Initialize the main root
    root = tk.Tk()
    center_root(root, 850, 400)
    root.resizable(0, 0)
    root.title("Totally Not Malware")
    root.configure(background="#ffffff")

    # Load the image and display it
    try:
        # Load the image from the correct path
        image = Image.open(file_path("goober.jpg"))
        image = image.resize((330, 390), Image.LANCZOS)
        img = ImageTk.PhotoImage(image)
        
        # Create a label with a red outline and no default border
        image_label = tk.Label(root, image=img, borderwidth=0, highlightbackground="red", highlightthickness=1)
        image_label.image = img
        image_label.grid(row=0, column=0, rowspan=5, padx=5, pady=5, sticky="w")
    except Exception as e:
        print(f"Error loading image: {e}")

    # Main text label
    main_label = tk.Label(root, text="H-hi there...\nDo you th-think I could have your\ncredit card information, p-please?", justify="center", bg="#ffffff", font=('Arial 20'))
    main_label.grid(row=0, column=1, columnspan=3, sticky="news")

    # Entry fields and labels
    tk.Label(root, text="Card number:", bg="#ffffff", font=('Arial 20'), borderwidth=2).grid(row=1, column=1, sticky="e", padx=5)
    tk.Label(root, text="Expiry date:", bg="#ffffff", font=('Arial 20'), borderwidth=2).grid(row=2, column=1, sticky="e", padx=5)
    tk.Label(root, text="Security code:", bg="#ffffff", font=('Arial 20'), borderwidth=2).grid(row=3, column=1, sticky="e", padx=5)

    card_entry = tk.Entry(root, width=20, font=('Arial 20'), borderwidth=0, relief="solid", highlightbackground="#d9dbdb", highlightcolor="#d9dbdb", highlightthickness=2)
    card_entry.grid(row=1, column=2, columnspan=2, padx=5, pady=2)
    card_entry.bind("<FocusIn>", on_focus_in)
    card_entry.bind("<FocusOut>", on_focus_out)

    expiry_entry = tk.Entry(root, width=20, font=('Arial 20'), borderwidth=0, relief="solid", highlightbackground="#d9dbdb", highlightcolor="#d9dbdb", highlightthickness=2)
    expiry_entry.grid(row=2, column=2, columnspan=2, padx=5, pady=2)
    expiry_entry.bind("<FocusIn>", on_focus_in)
    expiry_entry.bind("<FocusOut>", on_focus_out)

    security_entry = tk.Entry(root, width=20, font=('Arial 20'), borderwidth=0, relief="solid", show="*", highlightbackground="#d9dbdb", highlightcolor="#d9dbdb", highlightthickness=2)
    security_entry.grid(row=3, column=2, columnspan=2, padx=5, pady=2)
    security_entry.bind("<FocusIn>", on_focus_in)
    security_entry.bind("<FocusOut>", on_focus_out)

    # Button
    button_frame = tk.Frame(root, highlightbackground="#d9dbdb", highlightthickness=2, bd=0)
    button_frame.grid(row=4, column=1, columnspan=3, pady=10)

    submit_button = tk.Button(button_frame, text="Th-thanks", width=10, font=('Arial 20'), borderwidth=0, relief="solid", bg='#ffffff', activebackground="#c0e4f3", command=pass_details)
    submit_button.pack(padx=2, pady=2)

    root.mainloop()

def pass_details():
    card_num = card_entry.get()
    expiry = expiry_entry.get()
    code = security_entry.get()

    if card_num and expiry and code:
        print(f"Card-Number: {card_num}\nExpiry-Date: {expiry}\nSecurity-Code: {code}\n")
        thanku_window()
    else:
        print("Empty Input")

def thanku_window():
    global thanku  # Make thanku global to manage its scope
    thanku = tk.Toplevel(root)  # Using Toplevel to keep it as a child of root
    center_root(thanku, 550, 400)
    thanku.resizable(0,0)
    thanku.title("Thankuuu!!!")

    thanku_label = tk.Label(thanku, text="Th-Thankuu~ uwu", font=('Arial 50'), justify="center", fg="#ff33ff")
    thanku_label.grid(row=0, column=0)

    try:
        # Load the image specific to this window
        image_path = file_path("goober2.jpg")
        image2 = Image.open(image_path)
        image2 = image2.resize((540, 300), Image.LANCZOS)
        img2 = ImageTk.PhotoImage(image2)

        # Create a label with the new image reference
        image_label = tk.Label(thanku, image=img2, borderwidth=0, justify="center")
        image_label.image = img2  # Reference kept specific to this window
        image_label.grid(row=1, column=0, sticky="news")
    except Exception as e:
        print(f"Error loading image: {e}")

    root.withdraw()
    thanku.after(2000, btw_window)

def btw_window():

    global btw_window  # Make thanku global to manage its scope
    btw = tk.Toplevel(thanku)  # Using Toplevel to keep it as a child of root
    center_root(btw, 550, 600)
    btw.resizable(0,0)
    btw.title("Thankuuu!!!")

    btw_label = tk.Label(btw, text=f"Oh, b-btw...\nYour computer\nhas virus owo", font=('Arial 50'), justify="center", fg="#ff33ff")
    btw_label.grid(row=0, column=0)

    try:
        # Load the image specific to this window
        image_path = file_path("goober3.jpg")
        image2 = Image.open(image_path)
        image2 = image2.resize((540, 300), Image.LANCZOS)
        img2 = ImageTk.PhotoImage(image2)

        # Create a label with the new image reference
        image_label = tk.Label(btw, image=img2, borderwidth=0, justify="center")
        image_label.image = img2  # Reference kept specific to this window
        image_label.grid(row=1, column=0, sticky="news")
    except Exception as e:
        print(f"Error loading image: {e}")

    thanku.withdraw()
    btw.after(1000, funny_windows)

def create_funny_window(count):
    phrases = ["uwu", "owo", "nya~", "meow", "TwT"]  # List of phrases to display
    random_phrase = random.choice(phrases)  # Randomly select a phrase

    # Create a new Toplevel window
    funny_window = tk.Toplevel(thanku)  # Using Toplevel to keep it as a child of the thanku window
    funny_window.title("Funny Window")

    # Set random position for the window
    screen_width = funny_window.winfo_screenwidth()
    screen_height = funny_window.winfo_screenheight()
    random_x = random.randint(0, screen_width - 200)  # Adjust width accordingly
    random_y = random.randint(0, screen_height - 100)  # Adjust height accordingly
    funny_window.geometry(f"+{random_x}+{random_y}")  # Set the position of the window

    # Create a label using the same style as in the btw_window function
    funny_label = tk.Label(funny_window, text=random_phrase, font=('Arial 50'), justify="center", fg="#ff33ff")
    funny_label.grid(row=0, column=0)

    # Loop to create more windows
    if count < 499:  # Stop after creating 10 windows (0 to 9)
        funny_window.after(1, lambda: create_funny_window(count + 1))  # Call the function again after 1 second

def funny_windows():
    create_funny_window(0)  # Start the creation with the first window

main()