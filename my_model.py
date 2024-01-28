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





