import sqlalchemy as sal
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import insert
from .irepository import IRepository


class Repository(IRepository):
    def __init__(self, obj) -> None:
        self.engine = sal.create_engine('mssql+pyodbc://Teste')
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.metadata = MetaData(bind=engine)
        self.table = Table('tblLog', self.metadata, autoload=True)


    def add(self):
        print('Add')

    def delete(self):
        print('Delete')

    def update(self):
        print('update')

    def all(self):
        print("all")

    def findById(self):
        print('Find')
