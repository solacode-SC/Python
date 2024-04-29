import tkinter as tk
from tkinter import Image, ImageTk

def toggle_tabe(current_tabe):
    if current_tabe == tabe1:
        tabe1.pack_forget()
        tabe2.pack(fill=tk.BOTH, expand=True)
    else:
        tabe2.pack_forget()
        tabe1.pack(fill=tk.BOTH, expand=True)

# Create a new window for tabs
tabs_window = tk.Toplevel()
tabs_window.title("Seule piece")
tabs_window.config(bg="#82CEC4")
window_width = 650
window_height = 450
screen_width = tabs_window.winfo_screenwidth()
screen_height = tabs_window.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
tabs_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
tabs_window.resizable(False, False)

# Create the frames
tabe1 = tk.Frame(tabs_window, bg="#82CEC4")
tabe1.pack(fill=tk.BOTH, expand=True)

# Load the image
seule_descr_img = Image.open("C:\\Users\\synel\\Desktop\\My Desktop\\works\\MedAllal\\test\\img\\buttons\\btn_click.png")

# Resize the image
resized_seule_descr = seule_descr_img.resize((500, 200))  # Specify the desired width and height

# Convert the resized image to PhotoImage format
seule_descr = ImageTk.PhotoImage(resized_seule_descr)

# Create the label with the resized image
seule_descr_label = tk.Label(tabe1, image=seule_descr, bg="#D8E0E0")
seule_descr_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

# Load and resize image buttons
image_btn_regle1 = Image.open("C:\\Users\\synel\\Desktop\\My Desktop\\works\\MedAllal\\test\\img\\buttons\\btn_click.png")
resized_image_btn_regle1 = image_btn_regle1.resize((160, 50))  # Specify the desired width and height
btn_regle1 = ImageTk.PhotoImage(resized_image_btn_regle1)

image_btn_regle2 = Image.open("C:\\Users\\synel\\Desktop\\My Desktop\\works\\MedAllal\\test\\img\\buttons\\btn_click.png")
resized_image_btn_regle2 = image_btn_regle2.resize((160, 50))  # Specify the desired width and height
btn_regle2 = ImageTk.PhotoImage(resized_image_btn_regle2)

image_btn_regle3 = Image.open("C:\\Users\\synel\\Desktop\\My Desktop\\works\\MedAllal\\test\\img\\buttons\\btn_click.png")
resized_image_btn_regle3 = image_btn_regle3.resize((160, 50))  # Specify the desired width and height
btn_regle3 = ImageTk.PhotoImage(resized_image_btn_regle3)

# Create buttons with images
btn_regle1_button = tk.Button(tabe1, font=("sans-serif", 20), bg="#D8E0E0", command=lambda: toggle_tabe(tabe1), image=btn_regle1, borderwidth=0)
btn_regle1_button.place(relx=0.2, rely=0.65, anchor=tk.CENTER)
btn_regle1_button.config(cursor="hand2")

btn_regle2_button = tk.Button(tabe1, font=("sans-serif", 20), bg="#D8E0E0", command=lambda: toggle_tabe(tabe1), image=btn_regle2, borderwidth=0)
btn_regle2_button.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
btn_regle2_button.config(cursor="hand2")

btn_regle3_button = tk.Button(tabe1, font=("sans-serif", 20), bg="#D8E0E0", command=lambda: toggle_tabe(tabe1), image=btn_regle3, borderwidth=0)
btn_regle3_button.place(relx=0.8, rely=0.65, anchor=tk.CENTER)
btn_regle3_button.config(cursor="hand2")

tabs_window.mainloop()
