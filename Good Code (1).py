from tkinter import simpledialog
import tkinter as tk
import random
from tkinter import messagebox

class SpellerGridApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Speller Grid")

        # Set the grid size
        self.rows = 1
        self.cols = 1

        # Create a 2D list to store the letters
        self.grid_data = [['' for _ in range(self.cols)] for _ in range(self.rows)]

        # Create a frame to hold the speller grid
        self.grid_frame = tk.Frame(root)
        self.grid_frame.pack(padx=10, pady=10)

        # Create buttons for each cell in the grid
        self.buttons = [[tk.Button(self.grid_frame, text='', width=4, height=1, font=('Helvetica', 250),command=lambda i=i, j=j: self.cell_clicked(i, j))
                         for j in range(self.cols)] for i in range(self.rows)]

        # Place the buttons in the grid
        for i in range(self.rows):
            for j in range(self.cols):
                self.buttons[i][j].grid(row=i, column=j, padx=8, pady=8)
        

        #LINE 33 SHOULD BE UNCOMMENTED!!!! IN FINAL VERSION
        self.phase0()
                
        #self.buttons[0][0].configure(text="♠", bg="black")
        #self.buttons[0][1].configure(text="♥", bg="black")
        #self.buttons[1][0].configure(text="♦", bg="black")
        #self.buttons[1][1].configure(text="♣", bg="black")
        
        
        
        #self.flash_colors_and_letters()

    #def cell_clicked(self, row, col):
        # Open a dialog to input the letter
        #letter = simpledialog.askstring("Enter Letter", f"Enter a letter for cell ({row}, {col}):")
        
        # Check if a letter is entered
        #if letter:
            # Update the button text and grid data
            #self.buttons[row][col].configure(text=letter)
            #self.grid_data[row][col] = letter

    def run(self):
        self.root.mainloop()

    def phase0(self):
        self.buttons[0][0].configure(text="Here is your card",bg="white", fg="black", width=18, height=6, font=('Helvetica', 75))
        self.root.after(2500, self.phase1)
    
    def phase1(self):
        value = random.randint(1,4)
        if (value == 1):
            self.buttons[0][0].configure(text="♠", bg="white",fg="black",width=4, height=1, font=('Helvetica', 250))
        elif(value == 2):
            self.buttons[0][0].configure(text="♥", bg="white",fg="red",width=4, height=1, font=('Helvetica', 250))
        elif(value == 3):
            self.buttons[0][0].configure(text="♣", bg="white",fg="black",width=4, height=1, font=('Helvetica', 250))
        elif(value == 4):
            self.buttons[0][0].configure(text="♦", bg="white",fg="red",width=4, height=1, font=('Helvetica', 250))

        self.root.after(2500, self.phasePost1)

    def phasePost1(self):
        #change sizing temporarily
        self.buttons[0][0].configure(text="Now Find Your Card...",bg="white", fg="black", width=18, height=6, font=('Helvetica', 75))
        self.root.after(2500, self.phasePre2)
        
    def phasePre2(self):
        #change sizing back
        #The below line is technically phase 2 but I am too lazy to change the name
        self.buttons[0][0].configure(text="♠", bg="black",fg="black",width=4, height=1, font=('Helvetica', 250))
        self.root.after(1500, self.flash_colors_and_letters)


    def flash_colors_and_letters(self):
        # Function to flash colors and letters on buttons
        #This should be part of phase 2
        #somewhere in here whether at the end or the beginning, should look for the input from the p300 wave to go onto phase 3
        
        if (self.buttons[0][0].cget('text') == "♠" and self.buttons[0][0].cget('bg') == "black"):
            self.buttons[0][0].configure(text="♠", bg="white", fg = "black") 
        
        elif(self.buttons[0][0].cget('text') == "♠" and self.buttons[0][0].cget('bg') == "white"):
            self.buttons[0][0].configure(text="♥", bg="black", fg = "black")

        elif(self.buttons[0][0].cget('text') == "♥" and self.buttons[0][0].cget('bg') == "black"):
            self.buttons[0][0].configure(text="♥", bg="white", fg = "red")   

        elif(self.buttons[0][0].cget('text') == "♥" and self.buttons[0][0].cget('bg') == "white"):
            self.buttons[0][0].configure(text="♣", bg="black", fg = "black")   

        elif(self.buttons[0][0].cget('text') == "♣" and self.buttons[0][0].cget('bg') == "black"):
            self.buttons[0][0].configure(text="♣", bg="white", fg = "black")

        elif(self.buttons[0][0].cget('text') == "♣" and self.buttons[0][0].cget('bg') == "white"):
            self.buttons[0][0].configure(text="♦", bg="black", fg = "black")

        elif(self.buttons[0][0].cget('text') == "♦" and self.buttons[0][0].cget('bg') == "black"):
            self.buttons[0][0].configure(text="♦", bg="white", fg = "red")  

        elif(self.buttons[0][0].cget('text') == "♦" and self.buttons[0][0].cget('bg') == "white"):
            self.buttons[0][0].configure(text="♠", bg="black", fg = "black")

        
            
        self.root.after(1500, self.flash_colors_and_letters)


# Create the main window
root = tk.Tk()

# Create and run the SpellerGridApp
speller_grid_app = SpellerGridApp(root)
speller_grid_app.run()
