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

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def room_data(self):
        output = 'Room: {} \n'.format(self.name)
        for sensor in self.sensors:
            output += sensor.sensor_data() + '\n'
        return output

class Sensor(object):
    def __init__(self, name, status, pos=None):
        self.name = name
        self.status = status
        if pos == None:
            self.pos = []
        else:
            self.pos = pos
        self.img = w.create_rectangle(self.pos[0], self.pos[1], self.pos[2], self.pos[3], fill='red')

    def flip_status(self):
        if self.status == 'OPEN':
            self.status = 'CLOSED'
        else:
            self.status = 'OPEN'
        l.config(text=office.room_data())

    def check_status(self):
        root.after(200, lambda : self.check_status())
        if self.status == 'OPEN':
            w.itemconfig(self.img, fill='red') 
        else:
            w.itemconfig(self.img, fill='green')

    def sensor_data(self):
        return 'Sensor {} is currently {}'.format(self.name, self.status)

building = []

office = Room('Office', [50,50,300,300], [])
building.append(office)

window = Sensor('win0', 'OPEN', [170,295,200,305])
door = Sensor('door0', 'OPEN', [295,150,305,180])

office.add_sensor(window)
office.add_sensor(door)


b = Button(root, text='Unlock Door', command=lambda : door.flip_status())
b.pack()
c = Button(root, text='Unlock Window', command=lambda : window.flip_status())
c.pack()
l = Label(root, justify=LEFT)
l.pack()

for room in building:
    for item in room.sensors:
        root.after(200, item.check_status())

mainloop()