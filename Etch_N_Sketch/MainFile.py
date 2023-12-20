
# Christian Ilog 
# 06.28.20
# Purpose: To create a program that utilizes the if, if-else, & elif functions along-side the turtle graphics module.

# Imports ----------------------------------------------------
from turtle import * # Graphics Library
from tkinter import * # GUI Library

def etchCreate(): # Etch n' Sketch background code
# Canvas -----------------------------------------------------
  
    print("Prepping Etch n' Sketch, please wait...")
    print("---")
    title("Etch N' Sketch")
    # Pen Pre-defines ------------------------------------------
    tabMaker = Turtle()    
    tabMaker.speed("fastest") 
    screensize(8000, 8000)
    setworldcoordinates(0, 0, 8000, 8000)
    bgcolor("crimson")
    tabMaker.color("light grey", "light grey")
    tabMaker.begin_fill()
    

    # Pen Positioning ------------------------------------------
    tabMaker.penup()
    tabMaker.setpos(1000, 1500)
    tabMaker.seth(90)
    tabMaker.pendown()

    for screen in range(4): 
        tabMaker.forward(6000)
        tabMaker.right(90) 
# Dials ------------------------------------------------------

    # Left Dial Shadow ---------------------------------------
    tabMaker.penup()
    tabMaker.end_fill()
    tabMaker.setpos(850, 350)
    tabMaker.seth(0)    
    tabMaker.color("dark red")
    tabMaker.pensize(15)
    tabMaker.pendown()

    tabMaker.circle(500, 110)

    tabMaker.penup()
    tabMaker.setpos(850, 350)
    tabMaker.seth(0)    
    tabMaker.pendown()

    tabMaker.circle(500, -45)

    # Right Dial Shadow ---------------------------------------
    tabMaker.penup()
    tabMaker.setpos(6950, 350)
    tabMaker.seth(0)
    tabMaker.pendown()

    tabMaker.circle(500, 110)

    tabMaker.penup()
    tabMaker.setpos(6950, 350)
    tabMaker.seth(0)
    tabMaker.pendown()

    tabMaker.circle(500, -45)
    # Main dials (Left) ---------------------------------------
    tabMaker.penup()
    tabMaker.setpos(850, 350)
    tabMaker.seth(0)    
    tabMaker.color("gainsboro", "gainsboro")
    tabMaker.pensize(0)
    tabMaker.begin_fill()
    tabMaker.pendown()

    tabMaker.circle(500)

    # Main Dial (Right) ---------------------------------------
    tabMaker.penup()
    tabMaker.setpos(6950, 350)
    tabMaker.seth(0)
    tabMaker.pendown()

    tabMaker.circle(500)

    tabMaker.end_fill()
# Logo -------------------------------------------------------
    tabMaker.penup()
    tabMaker.setpos(1750, 500)
    tabMaker.seth(0)
    tabMaker.color("gold")
    tabMaker.pensize(4)
    tabMaker.pendown()

    # E --------------------------------------------------------
    tabMaker.forward(500)
    tabMaker.backward(500)
    tabMaker.left(90)
    tabMaker.forward(500)
    tabMaker.right(90)
    tabMaker.forward(300)
    tabMaker.backward(300)
    tabMaker.right(90)
    tabMaker.forward(250)
    tabMaker.left(90)
    tabMaker.forward(200)
    tabMaker.backward(200)
    tabMaker.right(90)
    tabMaker.forward(250)
    tabMaker.left(90)
    tabMaker.forward(500)

    # T --------------------------------------------------------
    tabMaker.left(90)
    tabMaker.forward(500)
    tabMaker.backward(250)
    tabMaker.right(90)
    tabMaker.backward(200)
    tabMaker.forward(300)
    tabMaker.backward(100)
    tabMaker.right(90)   
    tabMaker.forward(250)
    tabMaker.left(90)
    tabMaker.forward(300)

    # C --------------------------------------------------------
    tabMaker.left(90)
    tabMaker.forward(250)
    tabMaker.right(90)
    tabMaker.forward(250)
    tabMaker.backward(250)
    tabMaker.right(90)
    tabMaker.forward(250)
    tabMaker.left(90)
    tabMaker.forward(400)

    # H --------------------------------------------------------
    tabMaker.left(90)
    tabMaker.forward(500)
    tabMaker.backward(250)
    tabMaker.right(90)
    tabMaker.forward(200)
    tabMaker.right(90)
    tabMaker.forward(250)
    tabMaker.left(90)
    tabMaker.forward(250)

    # N --------------------------------------------------------
    tabMaker.left(90)
    tabMaker.forward(300)
    tabMaker.backward(100)
    tabMaker.right(90)
    tabMaker.forward(150)
    tabMaker.right(90)
    tabMaker.forward(200)

    # S --------------------------------------------------------
    tabMaker.left(90)
    tabMaker.forward(400)
    tabMaker.left(90)
    tabMaker.forward(200)
    tabMaker.left(90)
    tabMaker.forward(200)
    tabMaker.right(90)
    tabMaker.forward(200)
    tabMaker.right(90)
    tabMaker.forward(200)
    tabMaker.backward(200)
    tabMaker.right(90)
    tabMaker.forward(200)
    tabMaker.left(90)
    tabMaker.forward(200)
    tabMaker.right(90)
    tabMaker.forward(200)

    # K --------------------------------------------------------
    tabMaker.left(90)
    tabMaker.forward(200)
    tabMaker.left(90)
    tabMaker.forward(500)
    tabMaker.backward(350)
    tabMaker.right(45)
    tabMaker.forward(300)
    tabMaker.backward(300)
    tabMaker.right(45)
    tabMaker.forward(200)
    tabMaker.right(90)
    tabMaker.forward(150)
    tabMaker.left(90)
    tabMaker.forward(200)

    # E --------------------------------------------------------
    tabMaker.left(90)
    tabMaker.forward(250)
    tabMaker.right(90)
    tabMaker.forward(200)
    tabMaker.right(90)
    tabMaker.forward(150)
    tabMaker.right(90)
    tabMaker.forward(200)
    tabMaker.left(90)
    tabMaker.forward(100)
    tabMaker.left(90)
    tabMaker.forward(500)

    # T --------------------------------------------------------
    tabMaker.left(90)
    tabMaker.forward(500)
    tabMaker.backward(250)
    tabMaker.right(90)
    tabMaker.backward(200)
    tabMaker.forward(300)
    tabMaker.backward(100)
    tabMaker.right(90)   
    tabMaker.forward(250)
    tabMaker.left(90)
    tabMaker.forward(300)

    # C --------------------------------------------------------
    tabMaker.left(90)
    tabMaker.forward(250)
    tabMaker.right(90)
    tabMaker.forward(250)
    tabMaker.backward(250)
    tabMaker.right(90)
    tabMaker.forward(250)
    tabMaker.left(90)
    tabMaker.forward(400)

    # H --------------------------------------------------------
    tabMaker.left(90)
    tabMaker.forward(500)
    tabMaker.backward(250)
    tabMaker.right(90)
    tabMaker.forward(200)
    tabMaker.right(90)
    tabMaker.forward(250)
    tabMaker.left(90)
    tabMaker.forward(250)
# Details ----------------------------------------------------

    # Screen Depression Detail --------------------------------
    tabMaker.penup()
    tabMaker.setpos(1000, 1500)
    tabMaker.seth(0)
    tabMaker.color("silver", "silver")
    tabMaker.begin_fill()
    tabMaker.pendown()

    tabMaker.forward(200)
    tabMaker.left(90)
    tabMaker.forward(5800)
    tabMaker.right(90)
    tabMaker.forward(5800)
    tabMaker.left(90)
    tabMaker.forward(200)
    tabMaker.left(90)
    tabMaker.forward(6000)
    tabMaker.left(90)
    tabMaker.forward(6000)

    # Dial Concaves -----------------------------------------

    # Left Dial ---------------------------------------------
    tabMaker.end_fill()
    tabMaker.penup()
    tabMaker.setpos(850, 550)
    tabMaker.seth(0)    
    tabMaker.color("light grey", "light grey")
    tabMaker.pensize(0)
    tabMaker.begin_fill()
    tabMaker.pendown()

    tabMaker.circle(300)

    # Right Dial --------------------------------------------
    tabMaker.penup()
    tabMaker.setpos(6950, 550)
    tabMaker.seth(0)
    tabMaker.pendown()

    tabMaker.circle(300)

    tabMaker.end_fill()
    tabMaker.ht()
etchCreate()

def tutorialCode():
# Console Explanations/commands ------------------------------

    # Frame Pre-Defines --------------------------------------
    root = Tk()  # this creates a blank window
    root.title("Info Page") # window title
    topFrame = Frame(root)  # creates an invisible window for placing things
    topFrame.pack()  # places top boarder on window
    bottomFrame = Frame(root)  # creates bottom frame
    bottomFrame.pack(side=BOTTOM) # places boarder @ the bottom of the window
# Window Explanation Printing --------------------------------

    intro = Label(root, text="Welcome to Etch n' Sketch! Here is a simple explanation on how to use this program:", fg="black") # text = text, fg = text color
    indent = Label(root, text="---", fg="black")
    explan = Label(root, text="When the tablet finishes prepping, an input box will ask you for a command.", fg="black")
    explan2 = Label(root, text="Select one of the three:", fg="black")
    indent2 = Label(root, text="---", fg="black")
    e_Direct = Label(root, text="Direction -- Changes the direction of the cursor.", fg="black")
    e_Direct2 = Label(root, text="The cursor starts by facing North; direction choices references compass directions.", fg="black")
    indent3 = Label(root, text="---", fg="black")
    e_Move = Label(root, text="Movement -- Determines movement of the cursor.", fg="black")
    e_Move2 = Label(root, text="There are only two types of movement: Forward and Backward.", fg="black")
    e_Move3 = Label(root, text="After selecting a type of movement, the program will ask for a distance.", fg="black")
    e_Move4 = Label(root, text="Please note, the drawing area is in increments of 1 (pixel). To see notable work, 100 is a good place to start.", fg="black")
    indent4 = Label(root, text="---", fg="black")
    e_Shake = Label(root, text ="Shake -- Clears the Etch n' Sketch of your drawing", fg="black")
    indent5 = Label(root, text = "---", fg="black")
    e_quit = Label(root, text="Quit -- Quits the program.", fg="black")
    indent6 = Label(root, text="---", fg="black")
    e_Tip = Label(root, text="If you didn't mean to select a certain command, it's ok, type in Redo and you'll be prompted to select a new command.", fg="black")
    e_Tip2 = Label(root, text="Canceling Direction will reset the cursor back to facing North. Canceling Movement will not change direction, nor will it move.", fg="black")
    e_Tip3 = Label(root, text="AVOID PRESSING THE ACTUAL CANCEL BUTTON, THIS WILL GET RID OF THE INPUT BOX, MAKING YOU HAVE TO RESTART THE PROGRAM!!", fg="black")
    e_Tip4 = Label(root, text="If you want to save your artwork, use the 'windows key + shift + s' keyboard shortcut to snip the Etch n' Sketch window or screenshot and crop.", fg="black")
    e_Tip5 = Label(root, text="The input boxes will constantly loop until you decide to quit so don't worry and have fun drawing!", fg="black")
    e_Tip6 = Label(root, text= "The inputs are in all caps, so turn on caps lock and draw away!")
    indent7 = Label(root, text="---", fg="black")
    thanks = Label(root, text= "Thank you!", fg="black")
    happy_face = Label(root, text= "＼（＾○＾）／", fg="black")
# Window Explanation Packing ---------------------------------

    intro.pack(fill=Y) # Places the corresponding label into the window.
    indent.pack(fill=Y)
    explan.pack(fill=Y)
    explan2.pack(fill=Y)
    indent2.pack(fill=Y)
    e_Direct.pack(fill=Y)
    e_Direct2.pack(fill=Y)
    indent3.pack(fill=Y)
    e_Move.pack(fill=Y)
    e_Move2.pack(fill=Y)
    e_Move3.pack(fill=Y)
    e_Move4.pack(fill=Y)
    indent4.pack(fill=Y)
    e_Shake.pack(fill=Y)
    indent5.pack(fill=Y)
    e_quit.pack(fill=Y)
    indent6.pack(fill=Y)
    e_Tip.pack(fill=Y)
    e_Tip2.pack(fill=Y)
    e_Tip3.pack(fill=Y)
    e_Tip4.pack(fill=Y)
    e_Tip5.pack(fill=Y)
    e_Tip6.pack(fill=Y)
    indent7.pack(fill=Y)
    thanks.pack(fill=Y)
    happy_face.pack(fill=Y)
# Console Explanaton Printing --------------------------------

    print("Welcome to Etch n' Sketch! Here is a simple explanation on how to use this program:")
    print("---")
    print("When the tablet finishes prepping, an input box will ask you for a command.")
    print("Select one of the three:")
    print("---")
    print("Direction -- Changes the direction of the cursor.")
    print("The cursor starts by facing North; direction choices references compass directions.")
    print("---")
    print("Movement -- Determines movement of the cursor.")
    print("There are only two types of movement: Forward and Backward.")
    print("After selecting a type of movement, the program will ask for a distance.")
    print("Please note, the drawing area is in increments of 1 (pixel). To see notable work, 100 is a good place to start.")
    print("---")
    print("Quit -- Quits the program.")
    print("---")
    print("If you didn't mean to select a certain command, it's ok, type in Redo and you'll be prompted to select a new command.")
    print("Canceling Direction will reset the cursor back to facing North. Canceling Movement will not change direction, nor will it move.")
    print("AVOID PRESSING THE ACTUAL CANCEL BUTTON, THIS WILL GET RID OF THE INPUT BOX, MAKING YOU HAVE TO RESTART THE PROGRAM!!")
    print("If you want to save your artwork, use the 'windows key + shift + s' keyboard shortcut to snip the Etch n' Sketch window or screenshot and crop.")
    print("The input boxes will constantly loop until you decide to quit so don't worry and have fun drawing!")
    print("---")
    print("Thank you!")
    print("＼（＾○＾）／")
tutorialCode()

def main(): # Where user input code
# Pre Defines ------------------------------------------------

    tabCursor = Turtle()
    tabCursor.penup()
    tabCursor.setpos(4000, 4000)
    tabCursor.seth(90)
    tabCursor.color("grey")
    tabCursor.pensize(0)
    tabCursor.pendown() 
# Input Requests ---------------------------------------------

    print("Requesting input")
    inputBoy = textinput("Welcome to Etch n' Sketch!", "What shall we do? (DIRECTION, MOVEMENT, SHAKE, or QUIT)")
    while(True):
# Cursor Direction -------------------------------------------

        if (inputBoy == "DIRECTION"):
            print("Direction Command Selected")
            angle = textinput("What direction shall we face?", "NORTH, SOUTH, EAST, WEST, or REDO?")

            if(angle == "NORTH"):
                angle = 90          # Action when condition is met
                print("Heading = North") 

            elif(angle == "SOUTH"):
                angle = 270         # Action when condition is met
                print("Heading = South")

            elif(angle == "EAST"):
                angle = 0          # Action when condition is met
                print("Heading = East")
        
            elif(angle == "WEST"): 
                angle = 180        # Action when condition is met
                print("Heading = West")
            
            elif(angle == "REDO"):
                angle = 90         # Action when condition is met
                print("No change in heading ")

            else: 
                print("Invalid Response, asking again")
                angle = textinput("What direction shall we face?", "NORTH, SOUTH, EAST, WEST, or REDO?")

            tabCursor.seth(angle)
            print("Requesting Next Command")
            inputBoy = textinput("Next command", "What shall we do? (DIRECTION, MOVEMENT, SHAKE, or QUIT)")
# Cursor Movement --------------------------------------------

        elif(inputBoy == "MOVEMENT"):
            print("Movement Command Selected")
            movement = textinput("How shall we move?", "FORWARD, BACKWARD, or REDO?")

            if (movement == "FORWARD"):
                print("Forward Command Selected")
                count = (textinput("Plotting Movement", "How far shall we move? (Ex: 100)"))
                tabCursor.forward(int(count))
                print("Cursor moving forward " +count+ " pixels.") # Actions when condition is met
            
            elif(movement == "BACKWARD"): 
                print("Backward Command Selected")
                count = (textinput("Plotting Movement", "How far shall we move? (Ex: 100)"))
                tabCursor.backward(int(count))
                print("Cursor moving backward " +count+ " pixels.") # Actions when condition is met
            
            elif(movement == "REDO"):
                movement = 0
                print("No change in movement") # Action when condition is met

            else: 
                print("Invalid Response, asking again")
                movement = textinput("How shall we move?", "FORWARD, BACKWARD, or REDO?") # Actions when condition is met

            print("Requesting Next Command")
            inputBoy = textinput("Next Command", "What shall we do? (DIRECTION, MOVEMENT, SHAKE, or QUIT)")
# Reset Etch n' Sketch ---------------------------------------

        elif(inputBoy == "SHAKE"):
            print("clearing drawing")
            tabCursor.clear() # Clears the TABCURSOR'S work, this prevents erasing the entire grid and redrawing the bg. 
            # Pen Reset --------------------------------------

            tabCursor.penup()
            tabCursor.setpos(4000, 4000)
            tabCursor.seth(90)
            tabCursor.pendown() 
            inputBoy = textinput("Next Command", "What shall we do? (DIRECTION, MOVEMENT, SHAKE, or QUIT)") # Actions when condition is met
# System Exit ------------------------------------------------

        elif(inputBoy == "QUIT"): 
            bye()
            print("Exiting Etch n' Sketch ")

        else: 
            print("Invalid Response, asking again")
            inputBoy = textinput("Next Command", "What shall we do? (DIRECTION, MOVEMENT, SHAKE, or QUIT)") # Actions when condition is met
main()

mainloop() # Keeps the windows open until terminated. 
