##############################################################################
# tkinterDemo.py - program to test functionality for 
# security software
# Author: Shaun Preston (CrashInfinite)
##############################################################################

from Tkinter import *

##############################################################################

class Room(object):
    def __init__(self, name, corners=None, sensors=None):
        self.name = name
        
        if corners is None:
            corners = []
        self.corners = corners
        
        if sensors is None:
            sensors = []
        self.sensors = sensors
        
    def draw_room(self):
        for x in range(len(self.corners)-1):
            w.create_line(self.corners[x], self.corners[x+1])

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def room_data(self):
        output = 'Room: {} \n'.format(self.name)
        output += '\n'.join(sensor.sensor_data() for sensor in self.sensors)
        return output

##############################################################################

class Sensor(object):
    def __init__(self, name, status, pos=None):
        self.name = name
        self.status = status
        
        if pos is None:
            pos = []
        self.pos = pos
        
    def draw_sensor(self,):
        i = w.create_rectangle(
            self.pos[0],self.pos[1]-2,self.pos[0]+25,self.pos[1]+2)

        if self.status == 'OPEN':
            w.itemconfig(i, fill='red')
        else:
            w.itemconfig(i, fill='green')

    def flip_status(self): #eventually controlled by hardware
        if self.status == 'OPEN':
            self.status = 'CLOSED'
        else:
            self.status = 'OPEN'
        l.config(text=office.room_data()) 
        #only refers to one room, need to make universal

    def check_status(self):
        root.after(200, lambda : self.check_status())
        if self.status == 'OPEN':
            self.draw_sensor()
        else:
            self.draw_sensor()

    def sensor_data(self):
        return 'Sensor {} is currently {}'.format(self.name, self.status)

##############################################################################

#creating GUI elements
root = Tk()

w = Canvas(root, width=500, height=500)
w.pack()

f = Frame(root)
f.pack(side=BOTTOM)

b = Button(f, text='Unlock Door', command=lambda : sensor1.flip_status())
b.pack(side=LEFT)
c = Button(f, text='Unlock Window', command=lambda : sensor2.flip_status())
c.pack(side=LEFT)

l = Label(root, text='awaiting input', justify=LEFT)
l.pack(side=BOTTOM)

##############################################################################

#creating the actual layout and sensors

class System(object):
    def __init__(self, name, rooms=None):
        self.name = name

        if rooms == None:
            rooms = []
        self.rooms = rooms

    def insert_room(self, name):
        name.draw_room()
        self.rooms.append(name)

    def insert_sensor(self, room, sensor):
        sensor.draw_sensor()
        room.add_sensor(sensor)

chapel = System('chapel')

corners = [(100,100),(300,100),(350,130),(350,230),
            (300,250),(100,250),(100,100)]

office = Room('office', corners)
sensor1 = Sensor('win0', 'OPEN', [250,250])
sensor2 = Sensor('door0', 'CLOSED', [150,100])

chapel.insert_room(office)
chapel.insert_sensor(office, sensor1)
chapel.insert_sensor(office, sensor2)

#poll for changes to the status of all sensors
for room in chapel.rooms:
    for item in room.sensors:
        root.after(200, item.check_status())

mainloop()
