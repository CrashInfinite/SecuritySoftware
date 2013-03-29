from Tkinter import *

root = Tk()

w = Canvas(root, width=500, height=500)
w.pack()

class Room(object):
    def __init__(self, name, pos=None, sensors=None):
        self.name = name
        if pos == None:
            self.pos = []
        else:
            self.pos = pos
        if sensors == None:
            self.sensors = []
        else:
            self.sensors = sensors
        w.create_rectangle(self.pos[0],self.pos[1], self.pos[2], self.pos[3])

    def addSensor(self, sensor):
        self.sensors.append(sensor)

class Sensor(object):
    def __init__(self, name, status, pos=None):
        self.name = name
        self.status = status
        if pos == None:
            self.pos = []
        else:
            self.pos = pos
        self.img = w.create_rectangle(self.pos[0], self.pos[1], self.pos[2], self.pos[3], fill='red')

    def flipStatus(self):
        if self.status == 'OPEN':
            self.status = 'CLOSED'
        else:
            self.status = 'OPEN'
        print '{} - {}'.format(self.name, self.status)

    def checkStatus(self):
        root.after(200, lambda : self.checkStatus())
        if self.status == 'OPEN':
            w.itemconfig(self.img, fill='red') 
        else:
            w.itemconfig(self.img, fill='green')

building = []

office = Room('Office', [50,50,300,300], [])
building.append(office)

window = Sensor('win0', 'OPEN', [170,295,200,305])
door = Sensor('door0', 'OPEN', [295,150,305,180])

office.addSensor(window)
office.addSensor(door)


b = Button(root, text='Unlock Door', command=lambda : door.flipStatus())
b.pack()
c = Button(root, text='Unlock Window', command=lambda : window.flipStatus())
c.pack()

for item in office.sensors:
    root.after(200, item.checkStatus())

mainloop()