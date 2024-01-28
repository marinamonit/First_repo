from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, select, text

from sqlalchemy.orm import declarative_base, relationship, sessionmaker, joinedload

Base = declarative_base()


class Clients(Base):
    __tablename__ = 'clients'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(20))

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


class Orders(Base):
    __tablename__ = 'orders'

    id = Column(Integer, autoincrement=True, primary_key=True)
    cost = Column(Integer)
    name = Column(String(20))
    client_id = Column(Integer, ForeignKey('clients.id'))
    client = relationship('Clients', back_populates='orders')

    def __init__(self, cost, name, client_id):
        self.cost = cost
        self.name = name
        self.client_id = client_id

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


Clients.orders = relationship('Orders', back_populates='client')

connection_string = "sqlite:///C:\\Users\My\PycharmProjects\pythonProject1\identifier.sqlite"
engine = create_engine(connection_string, echo=True)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


# session = Session()
#
# order_1 = Orders(25, 'podushka Komfort', 1)
# order_2 = Orders(32, 'odeyalo Komfort+', 2)
# order_3 = Orders(15, 'jaket Kiyaro', 3)
# order_4 = Orders(18, 'jinsy Levis', 4)
# order_5 = Orders(56, 'nabor kosmetyki Dior', 5)
# order_6 = Orders(7, 'polotentse Bannoe', 6)
# order_7 = Orders(10, 'detskaya igryshka Slon', 7)
# order_8 = Orders(30, 'Igra nastolnaya Mafia', 8)
# order_9 = Orders(10, 'nabor speziy Indiya', 9)
# order_10 = Orders(7, 'bumaga A5', 10)
#
# session.add_all([order_1, order_2, order_3, order_4, order_5, order_6, order_7, order_8, order_9, order_10])
#
# client_0 = Clients('Nina')
# client_1 = Clients('Hanna')
# client_2 = Clients('Dima')
# client_3 = Clients('Sasha')
# client_4 = Clients('Inessa')
# client_5 = Clients('Denis')
#
# session.add_all([client_0, client_1, client_2, client_3, client_4, client_5])
# session.commit()
#
# clients = session.query(Clients).all()
# for client in clients:
#     print(f"client {client.name}:")
#     for order in client.orders:
#         print(f" {(order.name)}")
# session.close()


def get_order(name):
    session = Session()
    stmt = select(Orders).where(Orders.name == name)
    my_order = session.scalar(stmt)
    session.close()
    return my_order


def get_orders():
    session = Session()
    stmt = session.execute(select(Orders))
    my_orders = stmt.scalars().all()
    session.close()
    return my_orders





