
import tkinter as tk
import random
import threading
import PIL.Image
from PIL import ImageTk, Image


class SpellerGridApp:
    def __init__(self, root, images, img_size=(300, 550), transition_duration=1200, background_color='black'):
        """
        root: Master Window
        King_of_Hearts: file path of the king of hearts card.
        King_of_Spades: file path of the king of spades card.
        King_of_Diamonds: file path of the king of diamonds card.
        King_of_Clubs: file path of the king of clubs card.
        img_size: The resizing tool for images. Unless absolutely needed, Don't mess with it.
        """

        # During Testing my computer screen was 1920 x 1080 if you have trouble resizing it.
        # Setting Up the screen size, although elements may be out of place for some screen sizes
        self.root = root
        self.background_color = background_color
        self.root.title("Speller Grid")
        self.root.configure(bg=background_color)
        root.attributes('-fullscreen', True)
        self.window_width = int(window.winfo_screenwidth() / 58)
        self.window_height = (self.window_width * 2)
        self.img_size = img_size
        # How long in ms each slide lasts
        # Note: When Showing them instructions and the card for the first time we give them more time.
        self.transition_duration = transition_duration
        # Resizing Images
        self.listOfImages = images
        self.img1 = ImageTk.PhotoImage(Image.open(self.listOfImages[0]).resize(self.img_size))
        # I create a custom image that serves to cover up images when we hide the cards.
        black_image = PIL.Image.new(mode='RGB', size=self.img_size, color=background_color)
        self.black = ImageTk.PhotoImage(black_image)
        # You must reference the image in order for python to keep the image
        
        self.black.image = self.black
        self.img1.image = self.img1

        #This variable stops the CircleThroughOptions method because I didn't know that joining the thread didn't actually stop it
        #So this variable will be used to keep track of when CircleThroughOptions will be looping or not; Basically when True, it stops
        self.stopThreadOne = False
        #This is used in the circleThroughOptions Method
        self.listIndex = 0
        # Set the grid size
        self.rows = 2
        self.cols = 4
        #Below is a list of the label which is to be used once the labels are initialized in the startThreadOne function
        #The reason why we don't just initialize now is because we change the labels a lot between here and when we initialize them again
        self.labelList = []
        #Below is a list of the images in the order that they appeared
        self.shownCardsOrder = []
        #Below was made to keep track of the rows and columns
        self.grid_row = []
        self.grid_column = []
        for i in range(self.rows):
            self.grid_row.append(i)
        for i in range(self.cols):
            self.grid_column.append(i)
        #Making list of tuples for efficieny when looping
        self.grid = []
        for i in self.grid_row:
            for j in self.grid_column:
                self.grid.append((i,j))
        
        # Create a frame to hold the speller grid
        self.grid_frame = tk.Frame(root, bg="black")
        self.grid_frame.pack(padx=10)

        # Create buttons for each cell in the grid, (we end up only using one button so there was no need for the grid)
        self.Label = [[tk.Label(self.grid_frame, text='', width=2, height=4, font=('Helvetica', 190))
                       for j in range(self.cols)] for i in range(self.rows)]

        # Place the buttons in the grid
        for i in range(self.rows):
            for j in range(self.cols):
                self.Label[i][j].grid(row=i, column=j)

        self.landingPage()

    def run(self):
        # starts the actual code.
        self.root.mainloop()

    def chooseRandomImage(self):
        value = random.randint(0,len(self.listOfImages)-1)
        #This if statement makes this random choosing, less random, but in a good way in that it reduces repeats, 
        #Increase the range value to make it less likely to repeat
        for i in range(4):
            if (len(self.shownCardsOrder) != 0 and self.shownCardsOrder[len(self.shownCardsOrder) - 1] == self.listOfImages[value]):
                #this if checks the previous card shown to make sure its not the same
                value = random.randint(0,len(self.listOfImages)-1)
            elif (len(self.shownCardsOrder) != 0 and len(self.shownCardsOrder) != 1 and self.shownCardsOrder[len(self.shownCardsOrder) - 2] == self.listOfImages[value]):
                #this if checks the previous previous card shown to make sure its not the same
                value = random.randint(0,len(self.listOfImages)-1)
            else:
                break
        
        
        self.shownCardsOrder.append(self.listOfImages[value])
        self.img1 = ImageTk.PhotoImage(Image.open(self.listOfImages[value]).resize(self.img_size))
        self.img1.image = self.img1
        return self.img1
    
    def landingPage(self):
        
        self.grid_frame.pack_forget()
        # Defines Current Layer
        self.landing = tk.Frame(self.root, width=self.window_width, height=self.window_height, bg="black")
        # Makes it visible
        self.landing.pack(expand=True, fill='both')
        self.card = tk.Label(self.landing,
                             bg='black', fg = "white",
                             width=20, height=5, font=('Helvetica', 100), bd=10)
        # Defines what Playing card is shown (Randomly)
        self.reset = tk.Button(self.landing, bg="black", fg="white", text='', width=6, height=2, font=('Helvetica', 25), bd=10, command=lambda: self.startMenu())
        self.card.configure(text = "BCI P300\nMagician Project",anchor='center')
        self.reset.configure(text="Start")
        # Special instructions to show the Image
        self.card.pack(side="top", expand=True)
        self.reset.pack(side='bottom', expand=True)
    
    def startMenu(self):
        #This is the start menu so that you can wait here before starting the gui and you can select exactly what you want
        #As of now there are only four options but we can easily change this by just changing the grid and changing the cell_clicked function
        
        self.card_label = tk.Frame(self.root)
        self.card_label.pack()
        Card = [[tk.Button(self.card_label, bg="black", fg="white", text='', width=18, height=6, font=('Helvetica', 50),command=lambda i=i, j=j: self.cell_clicked(i, j))
                         for j in range(2)] for i in range(2)]
        for i in range(2):
            for j in range(2):
                Card[i][j].grid(row=i, column=j, padx=8, pady=8)
        Card[0][0].configure(text = "52 Cards")
        Card[0][1].configure(text = "13 Cards ♥")
        Card[1][0].configure(text ="Faces + Ace ♦♠")
        Card[1][1].configure(text = "Numbers ♣")
        #Forgets previous Layer, we do it here because it is quick enough to not be visible and reduces flashing user
        self.landing.pack_forget()
        
        

    def cell_clicked(self, row, col):
        #This is where the cards that are shown get selected based on what button was clicked
        # top left = all 52, top right = house of hearts, bottom left = faces and ace of diamonds and spades, bottom right = numbers of clubs
        if (row == 0 and col == 0):
            self.listOfImages = ['Pictures/acehearts.png', 'Pictures/2hearts.png', 'Pictures/3hearts.png','Pictures/4hearts.png','Pictures/5hearts.png',
                                'Pictures/6hearts.png','Pictures/7hearts.png','Pictures/8hearts.png','Pictures/9hearts.png','Pictures/10hearts.png',
                                'Pictures/jackhearts.png','Pictures/queenhearts.png','Pictures/kinghearts.png', 'Pictures/acediamonds.png',
                                'Pictures/2diamonds.png', 'Pictures/3diamonds.png','Pictures/4diamonds.png','Pictures/5diamonds.png','Pictures/6diamonds.png',
                                'Pictures/7diamonds.png','Pictures/8diamonds.png','Pictures/9diamonds.png','Pictures/10diamonds.png','Pictures/jackdiamonds.png',
                                'Pictures/queendiamonds.png','Pictures/kingdiamonds.png', 'Pictures/aceclubs.png', 'Pictures/2clubs.png', 
                                'Pictures/3clubs.png','Pictures/4clubs.png','Pictures/5clubs.png','Pictures/6clubs.png','Pictures/7clubs.png',
                                'Pictures/8clubs.png','Pictures/9clubs.png','Pictures/10clubs.png','Pictures/jackclubs.png',
                                'Pictures/queenclubs.png','Pictures/kingclubs.png', 'Pictures/acespades.png', 'Pictures/2spades.png', 
                                'Pictures/3spades.png','Pictures/4spades.png','Pictures/5spades.png','Pictures/6spades.png','Pictures/7spades.png',
                                'Pictures/8spades.png','Pictures/9spades.png','Pictures/10spades.png','Pictures/jackspades.png',
                                'Pictures/queenspades.png','Pictures/kingspades.png']
        elif(row == 0 and col == 1):
            self.listOfImages = ['Pictures/acehearts.png', 'Pictures/2hearts.png', 'Pictures/3hearts.png','Pictures/4hearts.png','Pictures/5hearts.png',
                                'Pictures/6hearts.png','Pictures/7hearts.png','Pictures/8hearts.png','Pictures/9hearts.png','Pictures/10hearts.png',
                                'Pictures/jackhearts.png','Pictures/queenhearts.png','Pictures/kinghearts.png']
        elif(row == 1 and col == 0):
            self.listOfImages = ['Pictures/acespades.png', 'Pictures/jackspades.png','Pictures/queenspades.png','Pictures/kingspades.png',
                                'Pictures/acediamonds.png','Pictures/jackdiamonds.png','Pictures/queendiamonds.png','Pictures/kingdiamonds.png']
        elif(row == 1 and col == 1):
            self.listOfImages = ['Pictures/2clubs.png', 
                                'Pictures/3clubs.png','Pictures/4clubs.png','Pictures/5clubs.png','Pictures/6clubs.png','Pictures/7clubs.png',
                                'Pictures/8clubs.png','Pictures/9clubs.png','Pictures/10clubs.png']
        self.root.after(10, self.Entry_slide)

    def Entry_slide(self):
        """ This is the First slide, and leaves a remaining layer
         called that is pack_forgotten in the subsequent function
         returns: The first slide
         """
        
        
        self.card_label2 = tk.Frame(self.root)
        self.card_label2.pack()
        Card = tk.Label(self.card_label2,
                        text="Here is your card",
                        bg="black", fg="white",
                        width=int(self.window_width),
                        height=int(self.window_height), font=('Helvetica', 75))
        Card.pack()
        #Forgets previous Layer, we do it here because it is quick enough to not be visible and reduces flashing user
        self.card_label.pack_forget()
        self.root.after(self.transition_duration + 1000, self.show_one_card)

    def show_one_card(self):
        """
        Parameters:
            value: a random number between 1 and 4 by default, however can be directly assigned for testing.
        self.single: a tk frame that contains this layer
        self.card: the shown image depending on value.
        Notes:
            Leaves a layer called single that must be subsequently pack_forget() in order to move on.
        """
        
        
        
        # Defines Current Layer
        self.single = tk.Frame(self.root, width=self.window_width, height=self.window_height)
        # Makes it visible
        self.single.pack(expand=True, fill='both')
        # Creates a Label that will show the subject the playing card
        self.card = tk.Label(self.single,
                             bg='black',
                             width=self.window_width, height=self.window_height, font=('Helvetica', 190), bd=0)
        # Defines what Playing card is shown (Randomly)
        self.finalImage = self.chooseRandomImage()
        self.card.configure(fg="black", image=self.finalImage)
        
        # Special instructions to show the Image
        self.card.pack(fill='both', expand=True)
        #Forgets previous Layer, we do it here because it is quick enough to not be visible and reduces flashing user
        self.card_label2.pack_forget()
        # Transition
        self.root.after(self.transition_duration + 1000, self.phasePost1)

    def phasePost1(self):
        """ Transition Slide
        Notes:
            Creates a layer called Card_label_2 and an object called Card,
             which must be pack_forget() in order to continue.
        """
        
        self.card_label_2 = tk.Frame(self.root)
        self.card_label_2.pack()
        Card = tk.Label(self.card_label_2,
                        text="Now Find your Card...",
                        bg="black", fg="white",
                        width=int(self.window_width),
                        height=int(self.window_height), font=('Helvetica', 75))
        Card.pack()
        #Forgets previous Layer, we do it here because it is quick enough to not be visible and reduces flashing user
        self.single.pack_forget()
        self.root.after(self.transition_duration, self.phasePre2)

    def phasePre2(self):
        """
        Notes:
            Essentially just creates two threads, one of which is currently useless (t2).
            In addition, it sets up startThreadOne to be ready to actually define the matrix for the cards.
        """
        # change sizing back
        
        self.t1 = threading.Thread(target=self.startThreadOne)
        self.t2 = threading.Thread(target=self.startThreadTwo)
        # self.root.after(self.transition_duration, self.circleThroughOptions)
        self.t1.start()
        self.t2.start()

    def startThreadOne(self):
        """
        Notes:
            In essence this actually creates the initial Grid of cards, with one set to show.
        """
        
        self.grid_frame.pack()
        # Thread 1, this thread, will circulate through all the cards endlessly
        # until thread two gets the needed input for a p300 spike
        # where we will join the two threads for the end of the gui
        
        for row in range(len(self.Label)):
            for col in range(len(self.Label[row])):
                self.Label[row][col].configure(fg='white', width=2,
                                               height=2, bd=0)
        
        # Declaring all cells
        self.Label[0][0].configure(bg="black", image=self.chooseRandomImage(), width=self.img_size[0], height=self.img_size[1])

        #Here is where the efficiency from making a tuple list comes in
        for i in range(1, len(self.grid)):
            self.Label[self.grid[i][0]][self.grid[i][1]].configure(bg="black", image=self.black, width=self.img_size[0], height=self.img_size[1])

        #I call pack_forget here because since things happen so fast, it can actually forget after packing the next frame
        #However, if we forget too early, it turns out it is too slow between forgetting and putting in the next frame, and flashbangs the user
        self.card_label_2.pack_forget()

        for i in range(0, self.rows):
            if (i % 2 == 1):
                for j in range(self.cols-1, -1, -1):
                    self.labelList.append(self.Label[i][j])
            elif (i % 2 == 0):
                for j in range(0, self.cols):
                    self.labelList.append(self.Label[i][j])
        #print(len(self.labelList))
        
        self.root.after(self.transition_duration, self.circleThroughOptions)

    def startThreadTwo(self):
        # Thread 2 will continuously check for the input where we can stop both the threads and start the end of the gui
        #This count variable will be tracking how many times we've looped
        
        self.count = 0
        self.root.after(self.transition_duration, self.checkForInput)

    def checkForInput(self):
        # !This needs to be changed once we receive input but for now we can "cheese" it
        #*The 5 seen below can be changed and the number that is put in is how many times it loops before stopping
        #print(self.count)
        if (self.count == len(self.labelList)*3):
            self.root.after(10, self.finishPart1)
        else:
            self.root.after(self.transition_duration, self.checkForInput)

        """
        input_value = self.user_input.get()
        if input_value == "1":
            self.result_label.configure(text="Input is 1")
        elif input_value == "0":
            self.result_label.configure(text="Input is 0")
        else:
            self.result_label.configure(text="Waiting for input...")
        # Reschedule the function after 100 milliseconds
        self.root.after(100, self.checkForInput)
        """
       
        

    def finishPart1(self):
        # Is not finished.
        self.t1.join()
        #Stop the looping of CircleThroughOptions
        self.stopThreadOne = True
        
        self.card_label = tk.Frame(self.root)
        self.card_label.pack()
        Card = tk.Label(self.card_label,
                        text="Here is your card",
                        bg="black", fg="white",
                        width=int(self.window_width),
                        height=int(self.window_height), font=('Helvetica', 75))
        Card.pack()
        #Forgets previous Layer, we do it here because it is quick enough to not be visible and reduces flashing user
        self.grid_frame.pack_forget()
        self.root.after(self.transition_duration + 1000, self.finishPart2)

    def resetGUI(self):
        #Here we are resetting pretty much every variable that would need to have fresh slate for this program to go through the entire process again
        
        self.t2.join()
        self.stopThreadOne = False
        self.shownCardsOrder = []
        self.labelList = []
        self.listIndex = 0
        #Forgets previous Layer, we do it here because it is quick enough to not be visible and reduces flashing user
        self.single.pack_forget()
        self.root.after(10, self.landingPage())

    def finishPart2(self):
        # Forgets previous Layer
        
        # Defines Current Layer
        self.single = tk.Frame(self.root, width=self.window_width, height=self.window_height, bg="black")
        # Makes it visible
        self.single.pack(expand=True, fill='both')
        # Creates a Label that will show the subject the playing card
        self.card = tk.Label(self.single,
                             bg='black',
                             width=self.window_width, height=self.window_height, font=('Helvetica', 190), bd=0)
        # Defines what Playing card is shown (Randomly)
        self.reset = tk.Button(self.single, bg="black", fg="white", text='', width=6, height=2, font=('Helvetica', 25), bd=10, command=lambda: self.resetGUI())
        self.card.configure(fg="black", image=self.finalImage)
        self.reset.configure(text="Reset")
        # Special instructions to show the Image
        self.card.pack(fill='both', expand=True)
        self.reset.pack(fill='none', pady=10)
        #Forgets previous Layer, we do it here because it is quick enough to not be visible and reduces flashing user
        self.card_label.pack_forget()
        for i in range(len(self.shownCardsOrder)):
            self.shownCardsOrder[i] = self.shownCardsOrder[i][9:len(self.shownCardsOrder[i])-4]
        print(self.shownCardsOrder)
        print()
    
    def getCardsOrder(self):
        return self.shownCardsOrder
 


    def circleAssist(self, index):
        # Turns off the Currently on Image
        self.labelList[index].configure(bg="black", fg="black", image=self.black)
        # Turns on the next image
        # This if statement checks the index of the labelList, the labelList for reference is just the order in which the cells appear, (snake pattern)
        if (index == len(self.labelList) - 1):
            
            self.labelList[0].configure(bg="black", fg="red", image=self.chooseRandomImage(), width=self.img_size[0],
                        height=self.img_size[1])
            self.listIndex = 0
        else:
            self.labelList[index+1].configure(bg="black", fg="red", image=self.chooseRandomImage(), width=self.img_size[0],
                        height=self.img_size[1])
            self.listIndex += 1
        self.count += 1
        if (not self.stopThreadOne):
            self.root.after(self.transition_duration, self.circleThroughOptions)
        
        
            

    def circleThroughOptions(self):
        """
        This is the Code that makes the images actually flash on and off
        One of the concerns I have with this code is that because we don't change the positions of the cards,
        we may change our test results.
        """
        self.circleAssist(self.listIndex)
        
        


# Create the main window
window = tk.Tk()
#Placeholder List, only first index matters because we change the list that this is used for later on
placeholder = ['Pictures/acespades.png']
# Create and run the SpellerGridApp
# If you want to replace the images I've made it possible, and it should be able to resize the images using a parameter
# , although it's untested and highly unlikely to work...
speller_grid_app = SpellerGridApp(window, images=placeholder, background_color='black', img_size=(300,525))
speller_grid_app.run()
