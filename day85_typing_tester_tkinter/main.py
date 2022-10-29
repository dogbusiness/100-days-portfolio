from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from words import Words
import time

# Initializing #
words = Words()

window = Tk()
window.title('Typing Speed Testing')
window.minsize(width=200, height=200)
window.config(padx=20, pady=20)

mainframe = ttk.Frame(window, padding="20 20 20 20")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

# Variables #
TIMER = 60
word_input = StringVar()
word_to_type = StringVar()
word_typed = BooleanVar()

# Events and functions
def enter_word(event):
    word = word_entry.get()
    word_input.set(word)
    words.words_input.append(word)
    word_entry.delete(0, 'end')
    word_typed.set(True)

def start():
    words.clear_lists()
    # Timer
    current_time = time.time()
    end_time = current_time + TIMER
    while current_time < end_time:
        current_time = time.time()
        word_to_be_typed = words.give_random_word()
        words.words_to_be_typed.append(word_to_be_typed)
        word_to_type.set(word_to_be_typed)
        # wait for input
        window.wait_variable(word_typed)

    points, incorrect_words, shown_words = words.show_results()
    word_out.delete(0, 'end')
    messagebox.showinfo(title='Time is up', message=f'Your Results:\nYour WPM (words per minute) is {points}\n'
                                                    f'You typed correctly {points} words out of {shown_words}')

# Elements #
lbl_txt = "Hi and welcome to Typing Speed Tester!\nWhen you click 'Start' button\nbe ready to type words\n" \
          "shown in the upper box to the box below.\n" \
          "When you done typing word press <Enter>\n" \
          "Good Luck!"

ttk.Label(mainframe, text=lbl_txt).grid(column=0, row=0, sticky=W)

word_out = ttk.Entry(mainframe, width=5, textvariable=word_to_type)
word_out.grid(column=0, row=1, sticky=(W, E))

word_entry = ttk.Entry(mainframe, width=50, textvariable=word_input)
word_entry.grid(column=0, row=2, sticky=(W, E))
word_entry.bind('<Return>', enter_word)

play = ttk.Button(mainframe, text="Start", command=start)
play.grid(column=0, row=3, pady=20)

window.mainloop()