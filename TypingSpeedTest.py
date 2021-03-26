# Modules / libraried required for testing the typing speed are imported.
# Message box for displaying and timer for checking the time taken


from tkinter import *
from tkinter import messagebox
from timeit import default_timer as timer
import random

# Setup the default size and color for the window 
root = Tk()
root.geometry('500x500')
root.configure(bg='Black')

# setting the outer window for displaying the name of the window
window = Tk()
window.geometry('550x500')
window.configure()

# reading the score from the txt file which will store the highest score so far achieved. 
# in the starting set it as 0
hs_file = open('highscore.txt', 'r+')
x = 0


# Create the game window
def game():
    global x
    if x == 0:
        root.withdraw()
        x = x + 1
    window.deiconify()
    def check_result():
        j = error = 0
        answer = entry.get("1.0", 'end-1c')
        end = timer()
        time_taken = end - start
        # wpm = [(no.of chars typed /5) - errors] / time taken(in min)
        # for calculating the error
        # if the len of actual word is greater then the answer typed.
        # elif the len of actual word is less than the answer typed.
        if len(words[word]) >= len(answer):
            error = len(words[word]) - len(answer)
            for i in answer:  # take shorter sentence
                if i == words[word][j]:
                    pass
                else:
                    error += 1
                j += 1
        elif len(words[word]) <= len(answer):
            error = len(answer) - len(words[word])
            for i in words[word]:
                if i == answer[j]:
                    pass
                else:
                    error += 1
                j += 1

            # calculate the WPM
        wpm = int(((len(answer) / 5) - error) / (time_taken / 60))
        # Now check with the highscore from the file
        hs_file.seek(0)
        line = int(hs_file.readline())
        # if score is greater than the highscore from the file. overwrite/Rewrite the file with the new score
        # display the new highscore or your score
        if wpm > line:
            hs_file.seek(0)
            hs_file.write(str(wpm))
            result = "Amazing! Your new highscore is : " + str(wpm) + " WPM"
            messagebox.showinfo("Score", result)
        else:
            result = "your score is: " + str(wpm) + "WPM \n Better luck next time !"
            messagebox.showinfo("Score", result)
            # if finished button is pressed, just close all the window and end the game.


    def finish():
        hs_file.close()
        window.destroy()
        root.destroy()

    # create the widget and give the words to type for checking the typing speed
    words = ['lary is kind', 'tom is coming here', 'Happy', 'Sad', 'Many']
    # stored the words in the list is displaying the random word at the time using random randint method.
    # words = ["An ever-growing number of complex and rigid rules plus hard-to-cope-with regulations are now being legislated from state to state. Key federal regulations were formulated by the FDA, FTC, and the CPSC. Each of these federal agencies serves a specific mission.", "Laws sponsored by the Office of the Fair Debt Collection Practices prevent an agency from purposefully harassing clients in serious debt. The Fair Packaging and Labeling Act makes certain that protection from misleading packaging of goods is guaranteed to each buyer of goods carried in small shops as well as in large supermarkets.", "Two common terms used to describe a salesperson are 'Farmer' and 'Hunter'. The reality is that most professional salespeople have a little of both. A hunter is often associated with aggressive personalities who use aggressive sales technique.", "A late 20th century trend in typing, primarily used with devices with small keyboards (such as PDAs and Smartphones), is thumbing or thumb typing. This can be accomplished using one or both thumbs.", "One study examining 30 subjects, of varying different styles and expertise, has found minimal difference in typing speed between touch typists and self-taught hybrid typists. According to the study, 'The number of fingers does not determine typing speed... People using self-taught typing strategies were found to be as fast as trained typists... instead of the number of fingers, there are other factors that predict typing speed.", "Closed captions were created for deaf or hard of hearing individuals to assist in comprehension. They can also be used as a tool by those learning to read, learning to speak a non-native language, or in an environment where the audio is difficult to hear or is intentionally muted.", "A freelancer or freelance worker, is a term commonly used for a person who is self-employed and is not necessarily committed to a particular employer long-term. Freelance workers are sometimes represented by a company or a temporary agency that resells freelance labor to clients; others work independently or use professional associations or websites to get work."]
    word = random.randint(0, (len(words) - 1))

    # setting x2, x3, b2, b3

    # x2 variable display the text msg by given font, color and background color at he positon (15, 10)
    x2 = Label(window, text=words[word], bg='black', fg='white', height=7, width=47, font='times 12', wraplength=500)
    x2.place(x=15, y=10)

    # x3 button for submitting the ans from the user
    x3 = Button(window, text='Submit', font='times 20', bg='#fc2828', command=check_result)
    x3.place(x=220, y=350)

    # Created the text box for user to entry the text. The text box with the height, width and at the position(100, 180)
    entry = Text(window)
    entry.place(x=100, y=180, height=150, width=350)

    # b2 Button created for user to confirm the typing is finished.
    # b2 Button placed at the position (155, 420)
    b2 = Button(window, text='Done', font='times 15', bg='#ffc003', width=12, command=finish)
    b2.place(x=155, y=420)

    # b3 button for creating the new game
    # b3 is placed the position ()
    b3 = Button(window, text='New Game', font='times 15', bg='#ffc003', command=game)
    b3.place(x=265, y=420)

    # timer is starting
    start = timer()

    window.mainloop()

    # Formating the Box to display at the starting of the window
    # x1 is used for showing the name of the game title at the position(100, 50)
    # setting the text, color, font for the X1 label


x1 = Label(root, text="Let's test your typing speed!", bg='black', fg='white', font='times 20')
x1.place(x=100, y=50)

# b1 is the button for starting the game and placed at the position (150, 120)
b1 = Button(root, text='Start', width=12, bg='#fcba03', font='times 20', command=game)
b1.place(x=150, y=120)

# highscore label display position at the window is (90, 240)
hs_text = Label(root, text='Highscore', width=12, bg='#03fcf8', font='times 30')
hs_text.place(x=90, y=240)

# Reading the score from file and displaying at the window on the position (110, 320) with the constumized color,
# font, background
hs = int(hs_file.readline())
hs_val = Label(root, text=str(hs) + " WPM", width=12, fg='#03fcf8', bg='black', font='times 20')
hs_val.place(x=110, y=320)

root.mainloop()
