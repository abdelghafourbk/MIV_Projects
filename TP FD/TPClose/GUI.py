import tkinter as tk
from PIL import Image, ImageTk
import definitions

data = [['A', 'B', 'C', 'D', 'E'],
        [1, 0, 0, 1, 1],
        [0, 0, 1, 1, 1],
        [1, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 1, 1]]


# Create the main window and start the event loop

def main():
    min_support = textarea.get()
    definitions.close(int(min_support), data)


master = tk.Tk()
master.title("My GUI")

# Load the background image
image = Image.open("data-miningBG.webp")
photo = ImageTk.PhotoImage(image)

# Create a frame with the same dimensions as the image
frame = tk.Frame(master, width=photo.width(), height=photo.height())
frame.pack()

# Set the background image of the frame
label = tk.Label(frame, image=photo)
label.place(x=0, y=0, relwidth=1, relheight=1)
label.image = photo

# Components:
# Create a canvas and draw a rectangle on it
canvas = tk.Canvas(frame, width=200, height=200, bg='white')
canvas.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

label_text = tk.Label(frame, text="Enter the minSup:")
label_text.pack()

textarea = tk.Entry(frame)
textarea.pack()

button = tk.Button(frame, text="START MINING!", command=main)
button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

master.mainloop()
