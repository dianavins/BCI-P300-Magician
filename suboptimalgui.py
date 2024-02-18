from tkinter import simpledialog
import tkinter as tk
import random
import threading
from tkinter import messagebox



class SpellerGridApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Speller Grid")
        self.root.configure(bg="black")
        root.attributes('-fullscreen', True)
        
        # Set the grid size
        self.rows = 2
        self.cols = 2

        # Create a 2D list to store the letters
        self.grid_data = [['' for _ in range(self.cols)] for _ in range(self.rows)]

        # Create a frame to hold the speller grid
        self.grid_frame = tk.Frame(root, bg="black")
        self.grid_frame.pack(padx=10, pady=25)

        # Create buttons for each cell in the grid, (we end up only using one button so there was no need for the grid)
        self.buttons = [[tk.Button(self.grid_frame, text='', width=3, height=1, font=('Helvetica', 190),command=lambda i=i, j=j: self.cell_clicked(i, j))
                         for j in range(self.cols)] for i in range(self.rows)]

        # Place the buttons in the grid
        for i in range(self.rows):
            for j in range(self.cols):
                self.buttons[i][j].grid(row=i, column=j, padx=8, pady=8)
        
        '''
        self.user_input = tk.StringVar()

        # Entry widget to receive input
        self.input_entry = tk.Entry(root, textvariable=self.user_input)
        self.input_entry.pack(pady=10)

        # Label to display the result
        self.result_label = tk.Label(root, text="Waiting for input...")
        self.result_label.pack(pady=10)
        '''
        self.phase0()
        
        

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
        self.buttons[0][0].configure(text="Here is your card",bg="white", fg="black", width=int(root.winfo_screenwidth()/58), height=int(root.winfo_screenheight()/108), font=('Helvetica', 75))
        self.root.after(2500, self.phase1)
    
    def phase1(self):
        value = random.randint(1,2)
        
        #if else statement kinda gross but its whatever
        
        
        if (value == 1):
            self.buttons[0][0].configure(text="♠", bg="white", fg="black", width=3, height=1, font=('Helvetica',190), bd=0)
            self.buttons[1][0].configure(text="♥", bg="black", fg="black", width=3, height=1, font=('Helvetica',190), bd=0)
            self.buttons[0][1].configure(text="♦", bg="black", fg="black", width=3, height=1, font=('Helvetica',190), bd=0)
            self.buttons[1][1].configure(text="♣", bg="black", fg="black", width=3, height=1, font=('Helvetica',190), bd=0)

        elif(value == 2):
            self.buttons[0][0].configure(text="♠", bg="black", fg="black", width=3, height=1, font=('Helvetica',190), bd=0)
            self.buttons[1][0].configure(text="♥", bg="white", fg="red", width=3, height=1, font=('Helvetica',190), bd=0)
            self.buttons[0][1].configure(text="♦", bg="black", fg="black", width=3, height=1, font=('Helvetica',190), bd=0)
            self.buttons[1][1].configure(text="♣", bg="black", fg="black", width=3, height=1, font=('Helvetica',190), bd=0)

        elif(value == 3):
            self.buttons[0][0].configure(text="♠", bg="black", fg="black", width=3, height=1, font=('Helvetica',190), bd=0)
            self.buttons[1][0].configure(text="♥", bg="black", fg="black", width=3, height=1, font=('Helvetica',190), bd=0)
            self.buttons[0][1].configure(text="♦", bg="white", fg="red", width=3, height=1, font=('Helvetica',190), bd=0)
            self.buttons[1][1].configure(text="♣", bg="black", fg="black", width=3, height=1, font=('Helvetica',190), bd=0)

        elif(value == 2):
            self.buttons[0][0].configure(text="♠", bg="black", fg="black", width=3, height=1, font=('Helvetica',190), bd=0)
            self.buttons[1][0].configure(text="♥", bg="black", fg="black", width=3, height=1, font=('Helvetica',190), bd=0)
            self.buttons[0][1].configure(text="♦", bg="black", fg="black", width=3, height=1, font=('Helvetica',190), bd=0)
            self.buttons[1][1].configure(text="♣", bg="white", fg="black", width=3, height=1, font=('Helvetica',190), bd=0)

        
        self.root.after(2500, self.phasePost1)

    def phasePost1(self):
        #change sizing temporarily
        self.buttons[0][0].configure(text="Now Find Your Card...", image = None, bg="white", fg="black", width=int(root.winfo_screenwidth()/58), height=int(root.winfo_screenheight()/108), font=('Helvetica', 75))
        self.root.after(2500, self.phasePre2)
        
    def phasePre2(self):
        #change sizing back
        
        
        t1 = threading.Thread(target=self.startThreadOne) 
        t2 = threading.Thread(target=self.startThreadTwo) 
        #self.root.after(1500, self.circleThroughOptions)
        t1.start()
        t2.start()


    def startThreadOne(self):
        #Thread 1, this thread, will circulate through all the cards endlessly until thread two gets a the needed input for a p300 spike where we will join the two threads for the end of the gui
        
        
        #insert_button = tk.Button(self.grid_frame, text='', width=3, height=1, font=('Helvetica', 190))
        #insert_button.grid(row=1,column = 0)
        #insert_button.grid(row=0,column = 1)
        #insert_button.grid(row=1,column = 1)
        
        self.buttons[0][0].configure(text="♠", bg="white", fg="black", width=3, height=1, font=('Helvetica',190), bd=0)
        self.buttons[1][0].configure(text="♥", bg="black", fg="black", width=3, height=1, font=('Helvetica',190), bd=0)
        self.buttons[0][1].configure(text="♦", bg="black", fg="black", width=3, height=1, font=('Helvetica',190), bd=0)
        self.buttons[1][1].configure(text="♣", bg="black", fg="black", width=3, height=1, font=('Helvetica',190), bd=0)
        self.root.after(1500, self.circleThroughOptions)

    def startThreadTwo(self):
        #Thread 2, this thread, will continuously check for the input where we can stop both the threads and start the end of the gui
        self.root.after(1500, self.checkForInput)

    def checkForInput(self):
        #!This needs to be finished
        #check for input check for input check for input
        print("woohoo") #this woohoo should print at the same time as line 115 of the circleThroughOptions function (NOTE: this line number may change)

        '''
        input_value = self.user_input.get()

        if input_value == "1":
            self.result_label.configure(text="Input is 1")
        elif input_value == "0":
            self.result_label.configure(text="Input is 0")
        else:
            self.result_label.configure(text="Waiting for input...")

        # Reschedule the function after 100 milliseconds
        self.root.after(100, self.checkForInput)
        '''
        #self.root.after(10000, self.finish)

    def finish(self):
        value = random.randint(1,2)
        
        #if else statement kinda gross but its whatever
        if (value == 1):
            self.buttons[0][0].configure(text="Here is your card: ♥",bg="white", fg="black", width=int(root.winfo_screenwidth()/58), height=int(root.winfo_screenheight()/108), font=('Helvetica', 75))

        elif(value == 2):
            self.buttons[0][0].configure(text="Here is your card: ♦",bg="white", fg="black", width=int(root.winfo_screenwidth()/58), height=int(root.winfo_screenheight()/108), font=('Helvetica', 75))

        elif(value == 3):
            self.buttons[0][0].configure(text="Here is your card: ♠",bg="white", fg="black", width=int(root.winfo_screenwidth()/58), height=int(root.winfo_screenheight()/108), font=('Helvetica', 75))

        elif(value == 2):
            self.buttons[0][0].configure(text="Here is your card: ♣",bg="white", fg="black", width=int(root.winfo_screenwidth()/58), height=int(root.winfo_screenheight()/108), font=('Helvetica', 75))
       


    def circleThroughOptions(self):
        # Function to flash colors and letters on buttons
        #This is technically Phase 2 but i'm too lazy to change the name
        #This is also techinically thread 1 but i'm too lazy to change the name
        

        #This if else statement is also very very gross but its whatever
        
        
        if(self.buttons[0][0].cget('bg') == "white"):
            self.buttons[0][0].configure(text="♠", bg="black", fg="black", width=3, height=1, font=('Helvetica',190))
            self.buttons[0][1].configure(text="♦", bg="white", fg="red", width=3, height=1, font=('Helvetica',190))
            self.root.after(1500, self.circleThroughOptions)
        
        elif(self.buttons[0][1].cget('bg') == "white"):
            self.buttons[0][1].configure(text="♦", bg="black", fg="black", width=3, height=1, font=('Helvetica',190))
            self.buttons[1][0].configure(text="♥", bg="white", fg="red", width=3, height=1, font=('Helvetica',190))
            self.root.after(1500, self.circleThroughOptions)

        elif(self.buttons[1][0].cget('bg') == "white"):
            self.buttons[1][0].configure(text="♥", bg="black", fg="black", width=3, height=1, font=('Helvetica',190))
            self.buttons[1][1].configure(text="♣", bg="white", fg="black", width=3, height=1, font=('Helvetica',190))
            self.root.after(1500, self.circleThroughOptions)

        elif (self.buttons[1][1].cget('bg') == "white"):
            self.buttons[1][1].configure(text="♣", bg="black", fg="black", width=3, height=1, font=('Helvetica',190))
            self.buttons[0][0].configure(text="♠", bg="white", fg="black", width=3, height=1, font=('Helvetica',190))
            self.root.after(1500, self.circleThroughOptions)

        
            
        


# Create the main window
root = tk.Tk()

# Create and run the SpellerGridApp
speller_grid_app = SpellerGridApp(root)
speller_grid_app.run()
