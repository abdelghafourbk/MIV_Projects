import tkinter as tk
import tkinter.font as font
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
master.geometry('600x500')
master.title("Data Mining")
master.configure(bg="#15307d")

#font
myFont =("Comic Sans MS",12, "bold")

image = Image.open("TPClose/datamining-BG.png")
photo = ImageTk.PhotoImage(image)

# Set the background image of the frame
label = tk.Label(master, image=photo)
label.place(x=0, y=0, relwidth=1, relheight=1)
label.pack(pady=20)
label.image = photo

#Components
label_text = tk.Label(master, text="Enter the minSup:", bg='#15307d', fg='white')
label_text.pack(pady=8)
label_text.configure(font=myFont)

textarea = tk.Entry(master)
textarea.pack(pady=2)

miningButton = tk.Button(master, text="START MINING!", bg='#eeb448', fg='white', command=main)
miningButton.pack(pady=10)
miningButton.configure(font=myFont)

resultLabel = tk.Label(master, text="Results:", bg='#15307d', fg='white')
resultLabel.pack(pady=4)
resultLabel.configure(font=myFont)

resultOutput = tk.Text(master, height=10, width=50)
resultOutput.pack()

master.mainloop()
