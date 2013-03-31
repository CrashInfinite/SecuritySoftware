from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlSetTables import RoomTable, SensorTable

	
engine = create_engine('sqlite:///security5.db', echo=False)

Session = sessionmaker(bind=engine)
session = Session()

new_room = RoomTable('office')
new_room.sensors = [SensorTable('win0', 'OPEN'), SensorTable('door0', 'OPEN')]

session.add(new_room)
session.commit()

# session.query(RoomTable).delete()

# query1 = session.query(SensorTable).filter(SensorTable.name=='win0').first()
# query1.status = 'CLOSED'
# session.commit()

res = session.query(SensorTable).all()
for x in res:
    print x.sensor_data()

