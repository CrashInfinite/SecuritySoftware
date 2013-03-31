from Tkinter import *

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

class Sensor(object):
    def __init__(self, name, status, pos=None):
        self.name = name
        self.status = status
        
        if pos is None:
            pos = []
        self.pos = pos
        
    def draw_sensor(self,):
        i = w.create_rectangle(self.pos[0],self.pos[1],self.pos[0]+25,self.pos[1]+3)

        if self.status == 'OPEN':
            w.itemconfig(i, fill='red')
        else:
            w.itemconfig(i, fill='green')

    def flip_status(self):
        if self.status == 'OPEN':
            self.status = 'CLOSED'
        else:
            self.status = 'OPEN'
        l.config(text=self.sensor_data()) #only refers to one room, need to make universal

    def check_status(self):
        root.after(200, lambda : self.check_status())
        if self.status == 'OPEN':
            self.draw_sensor()
        else:
            self.draw_sensor()

    def sensor_data(self):
        return 'Sensor {} is currently {}'.format(self.name, self.status)


#creating GUI elements
root = Tk()

w = Canvas(root, width=500, height=500)
w.pack()

b = Button(root, text='Unlock Door', command=lambda : sensor1.flip_status())
b.pack(side=RIGHT)
l = Label(root, justify=LEFT)
l.pack()

#creating the actual layout and sensors
building1 = []

corners = [(100,100),(300,100),(350,130),(350,230),(300,250),(100,250),(100,100)]
sensor_pos = [200,100]

room1 = Room('room', corners)
room1.draw_room()
building1.append(room1)
sensor1 = Sensor('win0','CLOSED', sensor_pos)
sensor1.draw_sensor()
room1.add_sensor(sensor1)

#poll for changes to the status of all sensors
for room in building1:
    for item in room.sensors:
        root.after(200, item.check_status())

mainloop()
