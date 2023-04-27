import tkinter as tk
from PIL import Image, ImageTk
import customtkinter #you need to install it sir using the command: pip install customtkinter==0.3
import definitions

#Data Matrix
data = [['A', 'B', 'C', 'D', 'E'],
        [1, 0, 0, 1, 1],
        [0, 0, 1, 1, 1],
        [1, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 1, 1]]
data1 = [['A', 'B', 'C', 'D', 'E'],
        [1, 1, 0, 1, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 1, 1]]

def main():
    min_support = textarea.get()
    fermutureArray, Gen1, assocs, minsupport, isFrequent, Gen2, isFrequent2, assocs2, Gen3, isFrequent3, assocs3 = definitions.close(int(min_support), data1)
    resultOutput.delete("1.0", tk.END)
    #Displaying fermutures in the results output
    for i in range(len(fermutureArray)):
        resultOutput.insert(tk.END, "Fermuture: " +fermutureArray[i]+ "\n")
    #Displaying the Gen1
    resultOutput.insert(tk.END, "\nGen-1:\n")
    resultOutput.insert(tk.END, Gen1)
    #Displaying associations of GEN-1 
    resultOutput.insert(tk.END, "\nLes associations de  GEN-1 :\n")
    resultOutput.insert(tk.END, assocs)
    resultOutput.insert(tk.END, "\n\nMin Support:"+ str(minsupport) + "\n")
    #Displaying done in case its not frequent
    if not isFrequent:
        resultOutput.insert(tk.END, "\nDone after GEN-1!!")
    else:
        #Displaying thhe associations of GEN-2  
        if Gen2:
            #Displaying the Gen2
            resultOutput.insert(tk.END, "\nGen-2:\n")
            resultOutput.insert(tk.END, Gen2)
            #Displaying associations of GEN-2
            resultOutput.insert(tk.END, "\n\nLes associations de  GEN-2 :\n")
            resultOutput.insert(tk.END, assocs2)
            #Displaying done in case the itemset in GEN2 is not frequent
            if not isFrequent2:
                resultOutput.insert(tk.END, "\n\nDone after Gen-2!!")
            else:
                #Displaying thhe associations of GEN-3
                if Gen3:
                    #Displaying the Gen2
                    resultOutput.insert(tk.END, "\nGen-3:\n")
                    resultOutput.insert(tk.END, Gen3)
                    #Displaying associations of GEN-3
                    resultOutput.insert(tk.END, "\nLes associations de  GEN-3 :\n")
                    resultOutput.insert(tk.END, assocs3)
                #Displaying done in case the itemset in GEN3 is not frequent
                if not isFrequent3:
                    resultOutput.insert(tk.END, "\n\nGEN-2 == GEN-3!!")


master = tk.Tk()
master.geometry('600x500')
master.title("Data Mining -Close Algorithm-")
master.configure(bg="#15307d")

#Font
myFont =("Halvetica",12, "bold")

image = Image.open("TPClose/datamining-BG.png")
photo = ImageTk.PhotoImage(image)

#Set the background image of the frame
label = tk.Label(master, image=photo)
label.place(x=0, y=0, relwidth=1, relheight=1)
label.pack(pady=20)
label.image = photo

#Components
label_text = tk.Label(master, text="Enter the minSup:", bg='#15307d', fg='white')
label_text.pack(pady=8)
label_text.configure(font=myFont)

#First input for the minsup
textarea = tk.Entry(master)
textarea.pack(pady=2, ipady=3)

#Button to start the execution
# miningButton = customtkinter.CTkButton(master, text="START MINING!", bg_color="eeb448", fg_color="white" ,width=20, height=10, corner_radius=24, command=main)

miningButton = tk.Button(master, text="START MINING!", bg='#eeb448', fg='white', command=main)
miningButton.pack(pady=10)
miningButton.configure(font=myFont)

#Output to show results
resultLabel = tk.Label(master, text="Results:", bg='#15307d', fg='white')
resultLabel.pack(pady=4)
resultLabel.configure(font=myFont)

resultOutput = tk.Text(master, height=30, width=80)
resultOutput.pack()

master.mainloop()