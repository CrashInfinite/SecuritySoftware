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
            w.create_line(self.corners[x], self.corners[x+1], fill='white' )

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def room_data(self):
        return '\n'.join(sensor.sensor_data() for sensor in self.sensors)

##############################################################################

class Sensor(object):
    def __init__(self, name, status, pos=None):
        self.name = name
        self.status = status
        
        if pos is None:
            pos = []
        self.pos = pos
        
    def draw_sensor(self,):
        i = w.create_oval(
            self.pos[0]-3,self.pos[1]-3,self.pos[0]+3,self.pos[1]+3)

        if self.status == 'OPEN':
            w.itemconfig(i, fill='red')
        else:
            w.itemconfig(i, fill='green')

    def flip_status(self): #eventually controlled by hardware
        if self.status == 'OPEN':
            self.status = 'CLOSED'
        else:
            self.status = 'OPEN'
        l.config(text=chapel.return_data()) 
        #only refers to one room, need to make universal

    def check_status(self):
        root.after(200, lambda : self.check_status())
        if self.status == 'OPEN':
            self.draw_sensor()
        else:
            self.draw_sensor()

    def sensor_data(self):
        return 'Sensor {} - {}'.format(self.name, self.status)

##############################################################################

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

    def return_data(self):
        output = ''
        for room in self.rooms:
            output += 'Room: {} \n-------------\n'.format(room.name)
            output += '\n'.join(sensor.sensor_data() for sensor in room.sensors)
            output += '\n\n'
        return output


##############################################################################

#creating GUI elements
root = Tk()

w = Canvas(root, width=600, height=600, bg='black')
w.pack()

f = Frame(root)
f.pack()

b = Button(f, text='Trip Office Door', command=lambda : sensor1.flip_status())
b.pack(side=LEFT)
c = Button(f, text='Trip Office Window', command=lambda : sensor2.flip_status())
c.pack(side=LEFT)
c = Button(f, text='Trip Bedroom Window', command=lambda : sensor3.flip_status())
c.pack(side=LEFT)

l = Label(root, text='awaiting input', justify=LEFT, bg='black', fg='white')
l.place(x=400, y=100)

##############################################################################

#creating the actual layout and sensors
chapel = System('chapel')

office_corners = [(50,100),(250,100),(300,130),(300,230),
            (250,250),(50,250),(50,100)]

bedroom_corners = [(50,250), (120,250), (120,350), (110,370),
            (110,370), (70,370), (50,350), (50,250)]

office = Room('office', office_corners)
bedroom = Room('bedroom', bedroom_corners)
sensor1 = Sensor('win0', 'OPEN', [200,250])
sensor2 = Sensor('door0', 'CLOSED', [100,100])
sensor3 = Sensor('win1', 'OPEN', [120,300])

chapel.insert_room(office)
chapel.insert_room(bedroom)
chapel.insert_sensor(office, sensor1)
chapel.insert_sensor(office, sensor2)
chapel.insert_sensor(bedroom, sensor3)

#poll for changes to the status of all sensors
for room in chapel.rooms:
    for item in room.sensors:
        root.after(200, item.check_status())

mainloop()
