# Import tkinter module for GUI creation
import tkinter as tk

# Import filedialog for open/save dialogs and messagebox for popups
from tkinter import filedialog, messagebox


# -------------------- FILE FUNCTIONS --------------------

def new_file():
    """Clear the text area to create a new file"""
    text.delete(1.0, tk.END)


def open_file():
    """Open an existing text file and display its content"""
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",                     # Default file extension
        filetypes=[("Text Files", "*.txt")]           # Allow only .txt files
    )

    # If user selects a file
    if file_path:
        with open(file_path, "r") as f:               # Open file in read mode
            text.delete(1.0, tk.END)                  # Clear text area
            text.insert(tk.END, f.read())             # Insert file content


def save_file():
    """Save the written content into a text file"""
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",                     # Default extension
        filetypes=[("Text Files", "*.txt")]           # File type filter
    )

    # If user chooses a location
    if file_path:
        with open(file_path, "w") as files:           # Open file in write mode
            files.write(text.get(1.0, tk.END))        # Write text content
        messagebox.showinfo("Saved ✨", "File saved successfully!")


# -------------------- MAIN WINDOW --------------------

# Create main application window
root = tk.Tk()

# Set window title
root.title("🌸 Rixz Anime Text Editor 🌸")

# Set window size
root.geometry("900x600")

# Prevent resizing for clean look
root.resizable(False, False)

# Set anime-style background color
root.configure(bg="#1e1e2e")  # Dark violet anime theme


# -------------------- MENU BAR --------------------

# Create menu bar
menu = tk.Menu(root, bg="#2a2a40", fg="white")

# Attach menu to window
root.config(menu=menu)

# Create File menu
file_menu = tk.Menu(menu, tearoff=0, bg="#2a2a40", fg="white")

# Add File menu to menu bar
menu.add_cascade(label="File", menu=file_menu)

# Add options inside File menu
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)


# -------------------- TEXT AREA --------------------

# Create scrollbar for smooth scrolling
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create text editor widget
text = tk.Text(
    root,
    wrap=tk.WORD,                    # Word wrapping
    font=("Comic Sans MS", 14),       # Anime-friendly font
    bg="#282a36",                     # Dark anime background
    fg="#f8f8f2",                     # Soft white text
    insertbackground="white",         # Cursor color
    yscrollcommand=scrollbar.set      # Attach scrollbar
)

# Expand text editor to full window
text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

# Connect scrollbar with text widget
scrollbar.config(command=text.yview)


# -------------------- KEYBOARD SHORTCUTS --------------------

# Ctrl + N → New file
root.bind("<Control-n>", lambda e: new_file())

# Ctrl + O → Open file
root.bind("<Control-o>", lambda e: open_file())

# Ctrl + S → Save file
root.bind("<Control-s>", lambda e: save_file())


# -------------------- RUN APPLICATION --------------------

# Start the GUI event loop
root.mainloop()
