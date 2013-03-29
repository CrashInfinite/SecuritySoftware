from Tkinter import *
import Tkinter

master = Tk()

w = Canvas(master, width=500, height=500)
w.pack()

room_one = w.create_rectangle(50,50,300,300)
window_one = w.create_rectangle(250,295,280,305, fill="green")
window_one_state = ''

F2 = Tkinter.Frame()
lab = Tkinter.Label(F2)
def poll(state):
    lab.after(200, poll(state))
    if state == 'CLOSED':
    	lab.config(text='CLOSED')
    else:
    	lab.config(text='OPEN')
lab.pack()
F2.pack(side=Tkinter.TOP)

def flip(state):
	if state == 'CLOSED':
		state = 'OPEN'
	else:
		state = 'CLOSED'

switch = Button(master, text="flip", command=flip(window_one_state))
switch.pack()

poll(window_one_state)
Tkinter.mainloop()