import tkinter as tk
#For Making Gui In Python We Use Tkinter
from time import strftime
root = tk.Tk()
root.title("Digital Clock")
def time():
    string = strftime("%H:%M:%S %p \n %d/%m/%Y")
    label.config(text=string)
    label.after(1000, time)
label = tk.Label(root, font=("calibri", 35,"bold"),bg="Black",fg="yellow")
label.pack()
time()
root.mainloop()
root.destroy()
label.pack(anchor="center")
time()
root.mainloop()


"""
🔍 DETAILED EXPLANATION OF EVERYTHING
1️⃣ import tkinter as tk
What it does: Imports Tkinter, Python’s built-in GUI (Graphical User Interface) library.

as tk means: You can write tk.Label, tk.Tk() instead of tkinter.Label.

📌 Used for creating:

Windows
Buttons
Labels
Frames
GUI apps

2️⃣ from time import strftime
What it does: Imports the strftime() function from the time module.

Why needed: Converts system time into a formatted string.

3️⃣ root = tk.Tk()
What it does: Creates the main application window.

This is the root window where all widgets live.

📌 Without this → GUI will NOT appear.

4️⃣ root.title("Digital Clock")
What it does:

Sets the title of the window (top bar text).

5️⃣ def time():
What it does:

Defines a function named time.

This function updates the clock every second.

📌 Functions allow reusability and auto-updates.

6️⃣ strftime("%H:%M:%S %p \n %d/%m/%Y")
What it does:

Gets current system time and date.

Format meaning:
Code	Meaning
%H	Hour (24-hour)
%M	Minutes
%S	Seconds
%p	AM / PM
\n	New line
%d	Day
%m	Month
%Y	Year

📌 Example Output:

21:45:12 PM
06/01/2026

7️⃣ label.config(text=string)
What it does:

Updates the text of the label.

Changes displayed time dynamically.

📌 config() is used to modify widget properties.

8️⃣ label.after(1000, time)
What it does: Calls the time() function again after 1000 milliseconds (1 second).

📌 This is the heart of the digital clock.

⚠️ Without after() → clock updates only once.

9️⃣ label = tk.Label(...)
What it does:

Creates a Label widget (text display).

Parameters explained:
Parameter	Meaning
root	Parent window
font	Text style & size
bg	Background color
fg	Text color
🔟 label.pack()
What it does:

Places the label inside the window.

Uses Pack geometry manager.

📌 Without this → label won’t appear.

1️⃣1️⃣ time()
What it does:

Calls the time() function first time.

Starts the clock.

1️⃣2️⃣ root.mainloop()
What it does:

Starts the Tkinter event loop.

Keeps the window open.
"""