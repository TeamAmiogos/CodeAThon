import tkinter as tk

def button_action():
    print("Button was pressed")

# Create the main window
root = tk.Tk()

# Create a button widget
button = tk.Button(root, text="Press me", command=button_action)

# Add the button to the main window
button.pack()
menu_bar = tk.Menu(root)
# Create a file menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create an edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")

# Add the menus to the menu bar
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Add the menu bar to the main window
root.config(menu=menu_bar)

# Start the main loop
root.mainloop()