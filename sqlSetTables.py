from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///security5.db', echo=True)
Base = declarative_base()

class RoomTable(Base):
    """"""
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self,name):
        self.name = name

class SensorTable(Base):
    """"""
    __tablename__ = 'sensors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(String)

    room_id = Column(Integer, ForeignKey('rooms.id'))
    room = relationship('RoomTable', backref=backref('sensors', order_by=id))

    def __init__(self, name, status):
        self.name = name
        self.status = status

    def sensor_data(self):
        return '{} - {}'.format(self.name, self.status)

Base.metadata.create_all(engine)