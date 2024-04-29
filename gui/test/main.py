import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

def toggle_frames(current_frame):
    if current_frame == frame1:
        frame1.pack_forget()
        frame2.pack(fill=tk.BOTH, expand=True)
    else:
        frame2.pack_forget()
        frame1.pack(fill=tk.BOTH, expand=True)

# create tab for one piece checking ttttttttt
def seule_tabs_window():
    # Create a new window for tabs
    tabs_window = tk.Toplevel(root)
    tabs_window.title("Seule piece")
    tabs_window.config(bg="#82CEC4")
    window_width = 650
    window_height = 450
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    tabs_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    tabs_window.resizable(False, False)


    # Create the frames
    tabe1 = tk.Frame(tabs_window, bg="#82CEC4")
    tabe1.pack(fill=tk.BOTH, expand=True)

    # Load the image
    seule_descr_img = Image.open("C:\\Users\\synel\\Desktop\\My Desktop\\works\\MedAllal\\test\\img\\imgs\\desc1.png")

    # Resize the image
    resized_seule_descr = seule_descr_img.resize((500, 200))  # Specify the desired width and height

    # Convert the resized image to PhotoImage format
    seule_descr = ImageTk.PhotoImage(resized_seule_descr)

    # Create the label with the resized image
    seule_descr_label = tk.Label(tabe1, image=seule_descr, bg="#82CEC4")
    seule_descr_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)


    image_btn_regle1 = Image.open("C:\\Users\\synel\\Desktop\\My Desktop\\works\\MedAllal\\test\\img\\imgs\\re3.png")
    # Resize the image
    resized_image_btn_regle1 = image_btn_regle1.resize((160, 80))  # Specify the desired width and height
    # Convert the resized image to PhotoImage format
    btn_regle1 = ImageTk.PhotoImage(resized_image_btn_regle1)
    # Create button and image 
    btn_regle1_button = tk.Button(tabe1, font=("sans-serif", 20), bg="#82CEC4", image = btn_regle1, borderwidth = 0)
    btn_regle1_button.place(relx=0.2, rely=0.65, anchor=CENTER)
    btn_regle1_button.config(cursor="hand2")

    image_btn_regle2 = Image.open("C:\\Users\\synel\\Desktop\\My Desktop\\works\\MedAllal\\test\\img\\imgs\\re2.png")
    # Resize the image
    resized_image_btn_regle2 = image_btn_regle2.resize((160, 80))  # Specify the desired width and height
    # Convert the resized image to PhotoImage format
    btn_regle2 = ImageTk.PhotoImage(resized_image_btn_regle2)
    # Create button and image 
    btn_regle2_button = tk.Button(tabe1, font=("sans-serif", 20), bg="#82CEC4", image = btn_regle2, borderwidth = 0)
    btn_regle2_button.place(relx=0.5, rely=0.65, anchor=CENTER)
    btn_regle2_button.config(cursor="hand2")

    image_btn_regle3 = Image.open("C:\\Users\\synel\\Desktop\\My Desktop\\works\\MedAllal\\test\\img\\imgs\\re1.png")
    # Resize the image
    resized_image_btn_regle3 = image_btn_regle3.resize((160, 80))  # Specify the desired width and height
    # Convert the resized image to PhotoImage format
    btn_regle3 = ImageTk.PhotoImage(resized_image_btn_regle3)
    # Create button and image 
    btn_regle3_button = tk.Button(tabe1, font=("sans-serif", 20), bg="#82CEC4", image = btn_regle3, borderwidth = 0)
    btn_regle3_button.place(relx=0.8, rely=0.65, anchor=CENTER)
    btn_regle3_button.config(cursor="hand2")

    

    tabs_window.mainloop()


def ass_tabs_window():
    # Create a new window for tabs
    tabs_window = tk.Toplevel(root)
    tabs_window.title("Seule piece")
    tabs_window.config(bg="#82CEC4")
    window_width = 650
    window_height = 450
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    tabs_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    tabs_window.resizable(False, False)


    # Create the frames
    tabe1 = tk.Frame(tabs_window, bg="#82CEC4")
    tabe1.pack(fill=tk.BOTH, expand=True)

    # Load the image
    seule_descr_img = Image.open("C:\\Users\\synel\\Desktop\\My Desktop\\works\\MedAllal\\test\\img\\imgs\\desc1.png")

    # Resize the image
    resized_seule_descr = seule_descr_img.resize((500, 200))  # Specify the desired width and height

    # Convert the resized image to PhotoImage format
    seule_descr = ImageTk.PhotoImage(resized_seule_descr)

    # Create the label with the resized image
    seule_descr_label = tk.Label(tabe1, image=seule_descr, bg="#82CEC4")
    seule_descr_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)


    image_btn_regle1 = Image.open("C:\\Users\\synel\\Desktop\\My Desktop\\works\\MedAllal\\test\\img\\imgs\\re3.png")
    # Resize the image
    resized_image_btn_regle1 = image_btn_regle1.resize((160, 80))  # Specify the desired width and height
    # Convert the resized image to PhotoImage format
    btn_regle1 = ImageTk.PhotoImage(resized_image_btn_regle1)
    # Create button and image 
    btn_regle1_button = tk.Button(tabe1, font=("sans-serif", 20), bg="#82CEC4", image = btn_regle1, borderwidth = 0)
    btn_regle1_button.place(relx=0.2, rely=0.65, anchor=CENTER)
    btn_regle1_button.config(cursor="hand2")

    image_btn_regle2 = Image.open("C:\\Users\\synel\\Desktop\\My Desktop\\works\\MedAllal\\test\\img\\imgs\\re2.png")
    # Resize the image
    resized_image_btn_regle2 = image_btn_regle2.resize((160, 80))  # Specify the desired width and height
    # Convert the resized image to PhotoImage format
    btn_regle2 = ImageTk.PhotoImage(resized_image_btn_regle2)
    # Create button and image 
    btn_regle2_button = tk.Button(tabe1, font=("sans-serif", 20), bg="#82CEC4", image = btn_regle2, borderwidth = 0)
    btn_regle2_button.place(relx=0.5, rely=0.65, anchor=CENTER)
    btn_regle2_button.config(cursor="hand2")

    image_btn_regle3 = Image.open("C:\\Users\\synel\\Desktop\\My Desktop\\works\\MedAllal\\test\\img\\imgs\\re1.png")
    # Resize the image
    resized_image_btn_regle3 = image_btn_regle3.resize((160, 80))  # Specify the desired width and height
    # Convert the resized image to PhotoImage format
    btn_regle3 = ImageTk.PhotoImage(resized_image_btn_regle3)
    # Create button and image 
    btn_regle3_button = tk.Button(tabe1, font=("sans-serif", 20), bg="#82CEC4", image = btn_regle3, borderwidth = 0)
    btn_regle3_button.place(relx=0.8, rely=0.65, anchor=CENTER)
    btn_regle3_button.config(cursor="hand2")

    

    tabs_window.mainloop()

def assenv_tabs_window():
    # Create a new window for tabs
    tabs_window = tk.Toplevel(root)
    tabs_window.title("Seule piece")
    tabs_window.config(bg="#82CEC4")
    window_width = 650
    window_height = 450
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    tabs_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    tabs_window.resizable(False, False)


    # Create the frames
    tabe1 = tk.Frame(tabs_window, bg="#82CEC4")
    tabe1.pack(fill=tk.BOTH, expand=True)

    # Load the image
    seule_descr_img = Image.open("C:\\Users\\synel\\Desktop\\My Desktop\\works\\MedAllal\\test\\img\\imgs\\desc1.png")

    # Resize the image
    resized_seule_descr = seule_descr_img.resize((500, 200))  # Specify the desired width and height

    # Convert the resized image to PhotoImage format
    seule_descr = ImageTk.PhotoImage(resized_seule_descr)

    # Create the label with the resized image
    seule_descr_label = tk.Label(tabe1, image=seule_descr, bg="#82CEC4")
    seule_descr_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)


    image_btn_regle1 = Image.open("C:\\Users\\synel\\Desktop\\My Desktop\\works\\MedAllal\\test\\img\\imgs\\re3.png")
    # Resize the image
    resized_image_btn_regle1 = image_btn_regle1.resize((160, 80))  # Specify the desired width and height
    # Convert the resized image to PhotoImage format
    btn_regle1 = ImageTk.PhotoImage(resized_image_btn_regle1)
    # Create button and image 
    btn_regle1_button = tk.Button(tabe1, font=("sans-serif", 20), bg="#82CEC4", image = btn_regle1, borderwidth = 0)
    btn_regle1_button.place(relx=0.2, rely=0.65, anchor=CENTER)
    btn_regle1_button.config(cursor="hand2")

    image_btn_regle2 = Image.open("C:\\Users\\synel\\Desktop\\My Desktop\\works\\MedAllal\\test\\img\\imgs\\re2.png")
    # Resize the image
    resized_image_btn_regle2 = image_btn_regle2.resize((160, 80))  # Specify the desired width and height
    # Convert the resized image to PhotoImage format
    btn_regle2 = ImageTk.PhotoImage(resized_image_btn_regle2)
    # Create button and image 
    btn_regle2_button = tk.Button(tabe1, font=("sans-serif", 20), bg="#82CEC4", image = btn_regle2, borderwidth = 0)
    btn_regle2_button.place(relx=0.5, rely=0.65, anchor=CENTER)
    btn_regle2_button.config(cursor="hand2")

    image_btn_regle3 = Image.open("C:\\Users\\synel\\Desktop\\My Desktop\\works\\MedAllal\\test\\img\\imgs\\re1.png")
    # Resize the image
    resized_image_btn_regle3 = image_btn_regle3.resize((160, 80))  # Specify the desired width and height
    # Convert the resized image to PhotoImage format
    btn_regle3 = ImageTk.PhotoImage(resized_image_btn_regle3)
    # Create button and image 
    btn_regle3_button = tk.Button(tabe1, font=("sans-serif", 20), bg="#82CEC4", image = btn_regle3, borderwidth = 0)
    btn_regle3_button.place(relx=0.8, rely=0.65, anchor=CENTER)
    btn_regle3_button.config(cursor="hand2")

    

    tabs_window.mainloop()
    

# Create the main window
root = tk.Tk()
root.title("Verfication")

window_width = 750
window_height = 550
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
root.resizable(False, False)
root.configure(bg="#8E9295")
root.attributes('-alpha', 0.95)


# Frame 1  taking full width and height
frame1 = tk.Frame(root, bg="#D8E0E0")
frame1.pack(fill=tk.BOTH, expand=True)


# Create the title label
# Load the image
title_img = Image.open("C:\\Users\\synel\\Desktop\\My Desktop\\works\\MedAllal\\test\\img\\imgs\\home_title.png")

# Resize the image
resized_title = title_img.resize((500, 200))  # Specify the desired width and height

# Convert the resized image to PhotoImage format
title = ImageTk.PhotoImage(resized_title)

# Create the label with the resized image
title_label = tk.Label(frame1, image=title, bg="#D8E0E0")
title_label.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

# create center start bottun
# Add Image 
# Load the image
image_b = Image.open("C:\\Users\\synel\\Desktop\\My Desktop\\works\\MedAllal\\test\\img\\buttons\\btn_click.png")

# Resize the image
resized_image_b = image_b.resize((300, 150))  # Specify the desired width and height

# Convert the resized image to PhotoImage format
login_btn = ImageTk.PhotoImage(resized_image_b)

# Create button and image 
start_button = tk.Button(frame1, font=("sans-serif", 20), bg="#D8E0E0", command=lambda: toggle_frames(frame1), image = login_btn, borderwidth = 0)
start_button.place(relx=0.5, rely=0.5, anchor=CENTER)
start_button.config(cursor="hand2")

#  add 2 logos to bottom of the window one in left and one in the right
# Load the image
image1 = Image.open("C:\\Users\\synel\\Desktop\\My Desktop\\works\\MedAllal\\test\\img\\logo\\logo1.png")

# Resize the image
resized_image1 = image1.resize((100, 100))  # Specify the desired width and height

# Convert the resized image to PhotoImage format
logo1 = ImageTk.PhotoImage(resized_image1)

# Create the label with the resized image
logo1_label = tk.Label(frame1, image=logo1, bg="#D8E0E0")
logo1_label.place(relx=0.9, rely=0.9, anchor=tk.CENTER)
# Load the image
image2 = Image.open("C:\\Users\\synel\\Desktop\\My Desktop\\works\\MedAllal\\test\\img\\logo\\logo2.png")

# Resize the image
resized_image2 = image2.resize((100, 100))  # Specify the desired width and height

# Convert the resized image to PhotoImage format
logo2 = ImageTk.PhotoImage(resized_image2)

# Create the label with the resized image
logo2_label = tk.Label(frame1, image=logo2, bg="#D8E0E0")
logo2_label.place(relx=0.1, rely=0.9, anchor=tk.CENTER)



# Frame 2 taking full width and height
frame2 = tk.Frame(root, bg="#82CEC4")
frame2.pack(fill=tk.BOTH, expand=True)


image_home = Image.open("C:\\Users\\synel\\Desktop\\My Desktop\\works\\MedAllal\\test\\img\\buttons\\home1.png")

# Resize the image
resized_image_home = image_home.resize((50, 50))  # Specify the desired width and height

home_btn = ImageTk.PhotoImage(resized_image_home)

# Create button and image 
home_button = tk.Button(frame2, font=("sans-serif", 20), bg="#82CEC4", command=lambda: toggle_frames(frame2), image = home_btn, borderwidth = 0)
home_button.place(relx=0.04, rely=0.08, anchor=CENTER)
home_button.config(cursor="hand2")

# for one piece

image_seuleP = Image.open("C:\\Users\\synel\\Desktop\\My Desktop\\works\\MedAllal\\test\\img\\buttons\\seulepiece.png")

# Resize the image
resized_image_seuleP = image_seuleP.resize((220, 80))  # Specify the desired width and height

seuleP_btn = ImageTk.PhotoImage(resized_image_seuleP)

# Create button and image 
seuleP_button = tk.Button(frame2, font=("sans-serif", 20), bg="#82CEC4", command=seule_tabs_window, image = seuleP_btn, borderwidth = 0)
seuleP_button.place(relx=0.2, rely=0.4, anchor=CENTER)
seuleP_button.config(cursor="hand2")

# add descrip   hanya die image li baghi for one piece :D
# Load the image
seule_img = Image.open("C:\\Users\\synel\\Desktop\\My Desktop\\works\\MedAllal\\test\\img\\imgs\\img1.png")

# Resize the image
resized_seule = seule_img.resize((200, 200))  # Specify the desired width and height

# Convert the resized image to PhotoImage format
seuleImage = ImageTk.PhotoImage(resized_seule)

# Create the label with the resized image
seule_Image = tk.Label(frame2, image=seuleImage, bg="#D8E0E0")
seule_Image.place(relx=0.2, rely=0.7, anchor=tk.CENTER)

# for assambalage

image_ass = Image.open("C:\\Users\\synel\\Desktop\\My Desktop\\works\\MedAllal\\test\\img\\buttons\\assamblage.png")

# Resize the image
resized_image_ass = image_ass.resize((220, 80))  # Specify the desired width and height

ass_btn = ImageTk.PhotoImage(resized_image_ass)

# Create button and image 
ass_button = tk.Button(frame2, font=("sans-serif", 20), bg="#82CEC4", command=ass_tabs_window, image = ass_btn, borderwidth = 0)
ass_button.place(relx=0.5, rely=0.4, anchor=CENTER)
ass_button.config(cursor="hand2")

# add descrip   hanya die image li baghi for assamblage :D
# Load the image
ass_img = Image.open("C:\\Users\\synel\\Desktop\\My Desktop\\works\\MedAllal\\test\\img\\imgs\\img2.png")

# Resize the image
resized_ass = ass_img.resize((200, 200))  # Specify the desired width and height

# Convert the resized image to PhotoImage format
assImage = ImageTk.PhotoImage(resized_ass)

# Create the label with the resized image
ass_Image = tk.Label(frame2, image=assImage, bg="#D8E0E0")
ass_Image.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# for ass & env

image_assEnv = Image.open("C:\\Users\\synel\\Desktop\\My Desktop\\works\\MedAllal\\test\\img\\buttons\\ass_env.png")

# Resize the image
resized_image_assEnv = image_assEnv.resize((220, 80))  # Specify the desired width and height

assEnv_btn = ImageTk.PhotoImage(resized_image_assEnv)

# Create button and image 
assEnv_button = tk.Button(frame2, font=("sans-serif", 20), bg="#82CEC4", command=assenv_tabs_window, image = assEnv_btn, borderwidth = 0)
assEnv_button.place(relx=0.8, rely=0.4, anchor=CENTER)
assEnv_button.config(cursor="hand2")

# add descrip   hanya die image li baghi for ass & env :D
# Load the image
assEnv_img = Image.open("C:\\Users\\synel\\Desktop\\My Desktop\\works\\MedAllal\\test\\img\\imgs\\img3.png")

# Resize the image
resized_assEnv = assEnv_img.resize((200, 200))  # Specify the desired width and height

# Convert the resized image to PhotoImage format
assEnvImage = ImageTk.PhotoImage(resized_assEnv)

# Create the label with the resized image
assEnv_Image = tk.Label(frame2, image=assEnvImage, bg="#D8E0E0")
assEnv_Image.place(relx=0.8, rely=0.7, anchor=tk.CENTER)

# Initially, show Frame 1 and hide Frame 2
frame1.pack()
frame2.pack_forget()

# Start the main loop
root.mainloop()