from Tkinter import *

root = Tk()

w = Canvas(root, width=500, height=500)
w.pack()

room = w.create_rectangle(50,50,300,300)
window = w.create_rectangle(150,295,200,305, fill='green')
window_state = 0

def switch(state):
    print state
    if state == 0:
    	state = 1
    else:
    	state = 0

b = Button(root, text='switch', command=switch(window_state))
b.pack()

mainloop()