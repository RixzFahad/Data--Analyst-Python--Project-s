from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.title("Rixz SlideShow")

# list of images path
img_paths = [
    r"C:\Users\smart\Downloads\WhatsApp Image 2025-10-27 at 12.19.16 AM.jpeg",
    r"C:\Users\smart\Downloads\lin-mei-NYyCqdBOKwc-unsplash.jpg",
    r"C:\Users\smart\Downloads\sora-sagano-8sOZJ8JF0S8-unsplash.jpg",
    r"C:\Users\smart\Downloads\dex-ezekiel-IxDPZ-AHfoI-unsplash.jpg",
    r"C:\Users\smart\Downloads\richard-tao-jlJFU9QBfFc-unsplash.jpg"
]

# resize images
img_size = (1080, 1080)
images = [Image.open(path).resize(img_size) for path in img_paths]
photo_imgs = [ImageTk.PhotoImage(img) for img in images]

# label
label = tk.Label(root)
label.pack()

# slideshow iterator
slideshow = cycle(photo_imgs)

def update_image():
    photo = next(slideshow)
    label.config(image=photo)
    label.image = photo  # prevent garbage collection
    root.after(3000, update_image)  # change image every 3 seconds

def start_slideshow():
    update_image()

playbutton = tk.Button(root, text="Start", command=start_slideshow)
playbutton.pack()

root.mainloop()
