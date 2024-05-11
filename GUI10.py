
import tkinter as tk
import random
import threading
import PIL.Image
from pygame import mixer
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
        self.img1 = ImageTk.PhotoImage(Image.open(self.listOfImages[0][0]).resize(self.img_size))
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
        self.rows = 1
        self.cols = 1
        #Below is a list of the label which is to be used once the labels are initialized in the startThreadOne function
        #The reason why we don't just initialize now is because we change the labels a lot between here and when we initialize them again
        self.labelList = []
        self.count = 0
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

        # Create labels for each cell in the grid, (we end up only using one label so there was no need for the grid)
        self.Label = [[tk.Label(self.grid_frame, text='', width=2, height=4, font=('Helvetica', 190))
                       for j in range(self.cols)] for i in range(self.rows)]

        # Place the labels in the grid
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
            if (len(self.shownCardsOrder) != 0 and self.shownCardsOrder[len(self.shownCardsOrder) - 1] == self.listOfImages[value][0]):
                #this if checks the previous card shown to make sure its not the same
                value = random.randint(0,len(self.listOfImages)-1)
            elif (len(self.shownCardsOrder) != 0 and len(self.shownCardsOrder) != 1 and self.shownCardsOrder[len(self.shownCardsOrder) - 2] == self.listOfImages[value][0]):
                #this if checks the previous previous card shown to make sure its not the same
                value = random.randint(0,len(self.listOfImages)-1)
            else:
                break
        
        
        self.shownCardsOrder.append(self.listOfImages[value][0])
        #This new curr variable is to temporarily store the name of the card so that we can later use it to find the correct audio file
        self.curr = self.shownCardsOrder[len(self.shownCardsOrder)-1]
        self.img1 = ImageTk.PhotoImage(Image.open(self.listOfImages[value][0]).resize(self.img_size))
        self.img1.image = self.img1
        return self.img1
    
    def selectAudio(self, card):
        for item in self.listOfImages:
            if item[0] == card and item[1] != "None":
                mixer.init()
                mixer.music.load(item[1])
                mixer.music.set_volume(0.7)
                mixer.music.play()
                


    
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
        Card[0][0].configure(text = "Cards & Sound 2 ♦♠")
        Card[0][1].configure(text = "Cards ♦♠")
        Card[1][0].configure(text ="Cards & Sound 1 ♦♠")
        Card[1][1].configure(text = "Real Project")
        #Forgets previous Layer, we do it here because it is quick enough to not be visible and reduces flashing user
        self.landing.pack_forget()
        
        

    def cell_clicked(self, row, col):
        #This is where the cards that are shown get selected based on what button was clicked
        # top left = all 52, top right = house of hearts, bottom left = faces and ace of diamonds and spades, bottom right = numbers of clubs
        if (row == 0 and col == 0):
            self.listOfImages = [('Pictures/acespades.png','Audio/piano2.mp3'), ('Pictures/jackspades.png','Audio/piano5.mp3'),
                                ('Pictures/queenspades.png','Audio/piano8.mp3'),('Pictures/kingspades.png','Audio/piano11.mp3'),
                                ('Pictures/acediamonds.png','Audio/piano14.mp3'),('Pictures/jackdiamonds.png','Audio/piano17.mp3'),
                                ('Pictures/queendiamonds.png','Audio/piano20.mp3'),('Pictures/kingdiamonds.png','Audio/piano23.mp3')]
            self.root.after(10, self.Entry_slide)
        elif(row == 0 and col == 1):
            self.listOfImages = [('Pictures/acespades.png','None'), ('Pictures/jackspades.png','None'),
                                ('Pictures/queenspades.png','None'),('Pictures/kingspades.png','None'),
                                ('Pictures/acediamonds.png','None'),('Pictures/jackdiamonds.png','None'),
                                ('Pictures/queendiamonds.png','None'),('Pictures/kingdiamonds.png','None')]
            self.root.after(10, self.Entry_slide)
        elif(row == 1 and col == 0):
            self.listOfImages = [('Pictures/acespades.png','Audio/piano1.mp3'), ('Pictures/jackspades.png','Audio/piano4.mp3'),
                                ('Pictures/queenspades.png','Audio/piano7.mp3'),('Pictures/kingspades.png','Audio/piano10.mp3'),
                                ('Pictures/acediamonds.png','Audio/piano13.mp3'),('Pictures/jackdiamonds.png','Audio/piano16.mp3'),
                                ('Pictures/queendiamonds.png','Audio/piano19.mp3'),('Pictures/kingdiamonds.png','Audio/piano22.mp3')]
            self.root.after(10, self.Entry_slide)
        elif(row == 1 and col == 1):
            self.listOfImages = [('Pictures/acespades.png','Audio/piano3.mp3'), ('Pictures/jackspades.png','Audio/piano6.mp3'),
                                ('Pictures/queenspades.png','Audio/piano9.mp3'),('Pictures/kingspades.png','Audio/piano12.mp3'),
                                ('Pictures/acediamonds.png','Audio/piano15.mp3'),('Pictures/jackdiamonds.png','Audio/piano18.mp3'),
                                ('Pictures/queendiamonds.png','Audio/piano21.mp3'),('Pictures/kingdiamonds.png','Audio/piano24.mp3')]
            self.root.after(10, self.chooseCard)

        

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
        #Gets the audio going for this card
        self.selectAudio(self.curr)
        
        
        # Special instructions to show the Image
        self.card.pack(fill='both', expand=True)
        #Forgets previous Layer, we do it here because it is quick enough to not be visible and reduces flashing user
        self.card_label2.pack_forget()
        # Transition
        self.root.after(self.transition_duration, self.phasePost1)

    def chooseCard(self):
        self.card_label.pack_forget()
        # Defines Current Layer
        self.single = tk.Frame(self.root, bg="black")
        # Makes it visible
        self.single.pack()


        #!This is hardcoded for a 2x4 (rows x cols) with 8 cards, this will need to be changed if using more than that or less
        # Creates a Label that will show the subject the playing card
        

        self.cards = [[tk.Label(self.single, text='', width=2, height=4, font=('Helvetica', 190))
                       for j in range(4)] for i in range(2)]
        for i in range(2):
            for j in range(4):
                self.cards[i][j].grid(row=i, column=j, padx=15, pady=5)
        
        for row in range(len(self.cards)):
            for col in range(len(self.cards[row])):
                index = (row*4) + col
                #print(self.listOfImages[index][0])
                self.img1 = ImageTk.PhotoImage(Image.open(self.listOfImages[index][0]).resize(self.img_size))
                self.img1.image = self.img1
                self.cards[row][col].configure(fg= "white", bd= 0, bg="black", image=self.img1, width=self.img_size[0], height=self.img_size[1])
                
        
        
        # Special instructions to show the Image
        #self.cards.pack()
        #Forgets previous Layer, we do it here because it is quick enough to not be visible and reduces flashing user
        self.count2 = 0
        # Transition
        self.root.after(self.transition_duration, self.circleThroughOptions2)

    def circleAssist2(self, index):
        for row in range(len(self.cards)):
            for col in range(len(self.cards[row])):
                index = (row*4) + col
                #print(self.listOfImages[index][0])
                self.img1 = ImageTk.PhotoImage(Image.open(self.listOfImages[index][0]).resize(self.img_size))
                self.img1.image = self.img1
                self.cards[row][col].configure(fg= "white", bd= 0, image=self.img1, width=self.img_size[0], height=self.img_size[1])
        # This if statement checks the index of the labelList, the labelList for reference is just the order in which the cells appear, (snake pattern)
        if (self.count2 < 4):
            
            self.cards[0][self.count2].configure(bg="red")
            self.selectAudio(self.listOfImages[self.count2][0])
        else:
            self.cards[1][self.count2-4].configure(bg="red")
            self.selectAudio(self.listOfImages[self.count2][0])
            
        self.count2 += 1
        self.root.after(self.transition_duration, self.circleThroughOptions2)
        
        
            

    def circleThroughOptions2(self):
        """
        This is the Code that makes the images actually flash on and off
        One of the concerns I have with this code is that because we don't change the positions of the cards,
        we may change our test results.
        """
        #!The 30 seen below can be changed and the number that is put in is how many cards show before stopping
        if (self.count2 == 8):
            self.count2 = 0
            self.root.after(10, self.phasePost1)
        else:
            self.circleAssist2(self.count2)

    def phasePost1(self):
        """ Transition Slide
        Notes:
            Creates a layer called Card_label_2 and an object called Card,
             which must be pack_forget() in order to continue.
        """
        #Stops music because i reinitialized it (couldve paused but in the case we don't initialize the first time, problems arise)
        mixer.init()
        mixer.music.pause()
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
        self.root.after(self.transition_duration + 1000, self.startThreadOne)

    def startThreadOne(self):
        """
        Notes:
            In essence this actually creates the initial Grid of cards, with one set to show.
        """
        
        self.grid_frame.pack(pady=250)
        
        

        for row in range(len(self.Label)):
            for col in range(len(self.Label[row])):
                self.Label[row][col].configure(fg='white', width=2,
                                               height=2, bd=0)
        
        # Declaring all cells
        
        self.Label[0][0].configure(bg="black", image=self.chooseRandomImage(), width=self.img_size[0], height=self.img_size[1])
        #Gets the audio going for this card
        self.selectAudio(self.curr)

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
       
        

    def finishPart1(self):
        #Stop the looping of CircleThroughOptions
        mixer.music.pause()
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
        self.finalImage = ""
        self.shownCardsOrder = []
        self.labelList = []
        self.listIndex = 0
        self.count = 0
        # Create labels for each cell in the grid, (we end up only using one label so there was no need for the grid)
        self.Label = [[tk.Label(self.grid_frame, text='', width=2, height=4, font=('Helvetica', 190))
                       for j in range(self.cols)] for i in range(self.rows)]

        # Place the labels in the grid
        for i in range(self.rows):
            for j in range(self.cols):
                self.Label[i][j].grid(row=i, column=j)
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
    


    def circleAssist(self, index):
        
        # Turns off the Currently on Image
        self.labelList[index].configure(bg="black", fg="black", image=self.black)
        # Turns on the next image
        # This if statement checks the index of the labelList, the labelList for reference is just the order in which the cells appear, (snake pattern)
        #!This was prior to me changing the style of the GUI from snake pattern to just one card changing so this has become pretty useless
        #!However I have yet to change it so right now it is kind of a mess
        if (index == len(self.labelList) - 1):
            self.labelList[0].configure(bg="black", fg="red", image=self.chooseRandomImage(), width=self.img_size[0],
                        height=self.img_size[1])
            self.listIndex = 0
            #Gets the audio going for this card
            self.selectAudio(self.curr)
        else:
            
            self.labelList[index+1].configure(bg="black", fg="red", image=self.chooseRandomImage(), width=self.img_size[0],
                        height=self.img_size[1])
            self.listIndex += 1
            #Gets the audio going for this card
            self.selectAudio(self.curr)
            
        self.count += 1
        self.root.after(self.transition_duration, self.circleThroughOptions)
        
        
            

    def circleThroughOptions(self):
        """
        This is the Code that makes the images actually flash on and off
        One of the concerns I have with this code is that because we don't change the positions of the cards,
        we may change our test results.
        """
        #!The 30 seen below can be changed and the number that is put in is how many cards show before stopping
        if (self.count == len(self.labelList)*12):
            self.root.after(10, self.finishPart1)
        else:
            self.circleAssist(self.listIndex)
        
        


# Create the main window
window = tk.Tk()
#Placeholder List, only first index matters because we change the list that this is used for later on
placeholder = [('Pictures/acespades.png', "audiomass-output.mp3")]
# Create and run the SpellerGridApp
# If you want to replace the images I've made it possible, and it should be able to resize the images using a parameter
# , although it's untested and highly unlikely to work...
speller_grid_app = SpellerGridApp(window, images=placeholder, background_color='black', img_size=(300,525))
speller_grid_app.run()

