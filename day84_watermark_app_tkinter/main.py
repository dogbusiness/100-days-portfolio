from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import watermark

# Initializing #

window = Tk()
window.title('Watermarking')
window.minsize(width=280, height=80)
window.config(padx=20, pady=20)

mainframe = ttk.Frame(window, padding="20 20 20 20")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

# Constant Elements #
ttk.Label(mainframe, text="Image Path").grid(column=0, row=0, sticky=W)
image_path = StringVar()
image_entry = ttk.Entry(mainframe, width=50, textvariable=image_path)
image_entry.grid(column=0, row=1, sticky=(W, E))

# Disappearing Watermark Options Variables #
wt_text = StringVar()
wt_logo_path = StringVar()
disappearing_options = []

# Watermark options depending on radio buttons #
def show_options():
	global disappearing_options
	row = 4
	if wt_option.get() == 'text':
		disappearing_options = []
		text_label = ttk.Label(mainframe, text="Enter the text:")
		text_entry = ttk.Entry(mainframe, width=50, textvariable=wt_text)
		disappearing_options.append(text_label)
		disappearing_options.append(text_entry)
		for element in disappearing_options:
			row += 1
			element.grid(column=0, row=row, sticky=(W, E))
	elif wt_option.get() == 'logo':
		disappearing_options = []
		logo_label = ttk.Label(mainframe, text="Logo path:")
		logo_entry = ttk.Entry(mainframe, width=50, textvariable=wt_logo_path)
		disappearing_options.append(logo_label)
		disappearing_options.append(logo_entry)
		for element in disappearing_options:
			row += 1
			element.grid(column=0, row=row, sticky=(W, E))

# Radio Buttons #
wt_option = StringVar()
ttk.Label(mainframe, text="Watermark by:").grid(column=0, row=2, sticky=W)
text_check = ttk.Checkbutton(mainframe, text='Text',
		command=show_options, variable=wt_option,
		onvalue='text')
text_check.grid(column=0, row=3, sticky=(W, E))
logo_check = ttk.Checkbutton(mainframe, text='Logo',
		command=show_options, variable=wt_option,
		onvalue='logo')
logo_check.grid(column=0, row=4, sticky=(W, E))

# Confirm Button #
def watermarking():
	try:
		if wt_option.get() == 'text':
			watermark.wt_text(image_path.get(), wt_text.get())
			messagebox.showinfo(title='Watermark created', message='Your image in "out" folder')
		else:
			watermark.wt_logo(image_path.get(), wt_logo_path.get())
			messagebox.showinfo(title='Watermark created', message='Your image in "out" folder')
	except FileNotFoundError:
		messagebox.showerror(title='Watermark is not created', message='There is no such file')
	except AttributeError:
		messagebox.showerror(title='Watermark is not created', message='Please type choose what to watermark by')
	except:
		messagebox.showerror(title='Watermark is not created', message='Unexpected error has occurred. Try to relaunch')

confirm = ttk.Button(mainframe, text="Confirm", command=watermarking)
confirm.grid(column=0, row=7, pady=20)

window.mainloop()
