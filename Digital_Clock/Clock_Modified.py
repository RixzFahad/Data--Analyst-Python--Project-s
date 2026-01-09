import tkinter as tk
from time import strftime

# ----------------- MAIN WINDOW -----------------
root = tk.Tk()
root.title("Smart Digital Clock")
root.geometry("600x250")
root.resizable(False, False)
root.configure(bg="#0f172a")  # Dark blue background

# ----------------- FRAME -----------------
frame = tk.Frame(root, bg="#020617", bd=10, relief="ridge")
frame.place(relx=0.5, rely=0.5, anchor="center")

# ----------------- TIME FUNCTION -----------------
def update_time():
    current_time = strftime("%I:%M:%S %p")
    current_day = strftime("%A")
    current_date = strftime("%d %B %Y")

    time_label.config(text=current_time)
    day_label.config(text=current_day)
    date_label.config(text=current_date)

    time_label.after(1000, update_time)

# ----------------- LABELS -----------------
time_label = tk.Label(
    frame,
    font=("DS-Digital", 50, "bold"),
    bg="#020617",
    fg="#38bdf8"
)
time_label.pack(padx=20, pady=(10, 0))

day_label = tk.Label(
    frame,
    font=("Calibri", 18, "bold"),
    bg="#020617",
    fg="#a5f3fc"
)
day_label.pack()

date_label = tk.Label(
    frame,
    font=("Calibri", 16),
    bg="#020617",
    fg="#e0f2fe"
)
date_label.pack(pady=(0, 10))

# ----------------- START CLOCK -----------------
update_time()
root.mainloop()
