# Import required modules
from itertools import cycle               # Used to loop images infinitely
from PIL import Image, ImageTk, ImageEnhance  # For image handling & effects
import tkinter as tk                      # GUI library

# ------------------ ROOT WINDOW ------------------
root = tk.Tk()                            # Create main window
root.title("Rixz Premium SlideShow")      # Window title
root.geometry("1100x1200")                # Window size
root.configure(bg="#0f172a")              # Dark premium background
root.resizable(False, False)              # Disable resizing

# ------------------ IMAGE PATHS ------------------
img_paths = [
    r"C:\Users\smart\Downloads\WhatsApp Image 2025-10-27 at 12.19.16 AM.jpeg",
    r"C:\Users\smart\Downloads\lin-mei-NYyCqdBOKwc-unsplash.jpg",
    r"C:\Users\smart\Downloads\sora-sagano-8sOZJ8JF0S8-unsplash.jpg",
    r"C:\Users\smart\Downloads\dex-ezekiel-IxDPZ-AHfoI-unsplash.jpg",
    r"C:\Users\smart\Downloads\richard-tao-jlJFU9QBfFc-unsplash.jpg"
]

# ------------------ IMAGE LOADING ------------------
img_size = (1080, 1080)                   # Target image size
images = []                               # List to store processed images

for path in img_paths:
    img = Image.open(path).resize(img_size)  # Open & resize image
    images.append(img)                        # Store image

photo_imgs = [ImageTk.PhotoImage(img) for img in images]  # Convert for Tkinter

# ------------------ IMAGE LABEL ------------------
image_frame = tk.Frame(root, bg="#020617", bd=4, relief="ridge")
image_frame.pack(pady=20)

label = tk.Label(image_frame, bg="#020617")  # Label to show images
label.pack()

# ------------------ STATUS TEXT ------------------
status = tk.Label(
    root,
    text="Click Start to Play Slideshow",
    fg="#e5e7eb",
    bg="#0f172a",
    font=("Segoe UI", 12)
)
status.pack(pady=10)

# ------------------ SLIDESHOW LOGIC ------------------
slideshow = cycle(images)               # Infinite loop over images
running = False                          # Control slideshow state

def fade_in(pil_image, step=0):
    """
    Creates fade-in effect by gradually increasing brightness
    """
    if not running:
        return

    enhancer = ImageEnhance.Brightness(pil_image)
    bright_img = enhancer.enhance(step / 10)

    photo = ImageTk.PhotoImage(bright_img)
    label.config(image=photo)
    label.image = photo                  # Prevent garbage collection

    if step < 10:
        root.after(50, fade_in, pil_image, step + 1)
    else:
        root.after(2500, show_next_image)

def show_next_image():
    """
    Shows next image with fade-in effect
    """
    if not running:
        return

    img = next(slideshow)                # Get next image
    fade_in(img)                          # Apply fade effect

def start_slideshow():
    """
    Start slideshow
    """
    global running
    if not running:
        running = True
        status.config(text="▶ Slideshow Running")
        show_next_image()

def stop_slideshow():
    """
    Stop slideshow
    """
    global running
    running = False
    status.config(text="⏸ Slideshow Stopped")

# ------------------ BUTTONS ------------------
btn_frame = tk.Frame(root, bg="#0f172a")
btn_frame.pack(pady=20)

start_btn = tk.Button(
    btn_frame,
    text="▶ Start",
    font=("Segoe UI", 12, "bold"),
    bg="#22c55e",
    fg="white",
    padx=20,
    command=start_slideshow
)
start_btn.grid(row=0, column=0, padx=10)

stop_btn = tk.Button(
    btn_frame,
    text="⏸ Stop",
    font=("Segoe UI", 12, "bold"),
    bg="#ef4444",
    fg="white",
    padx=20,
    command=stop_slideshow
)
stop_btn.grid(row=0, column=1, padx=10)

# ------------------ FOOTER ------------------
footer = tk.Label(
    root,
    text="Created by Rixz • Premium Python GUI",
    fg="#64748b",
    bg="#0f172a",
    font=("Segoe UI", 10)
)
footer.pack(side="bottom", pady=10)

# ------------------ MAIN LOOP ------------------
root.mainloop()                          # Start the GUI event loop
