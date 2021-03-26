from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import insert
import sqlalchemy as sal
from .irepository import IRepository

class LogRepository(IRepository):

    def __init__(self, obj) -> None:
        self.engine = sal.create_engine('mssql+pyodbc://Teste')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.metadata = MetaData(bind=self.engine)
        self.table = Table(obj.TableName, self.metadata, autoload=True)
        self.obj = obj

    def add(self):
        i = insert(self.table)
        i = i.values({"Estado": self.obj.status,
                      "Sigla": self.obj.sigla,
                      "ErrorCode": self.obj.erroCode,
                      "ErrorColumn": self.obj.erroColumn})
        self.session.execute(i)
        self.session.commit()

    def delete(self):
        u = delete(self.table)
        u = u.where(self.table.c.Sigla == self.obj.sigla)
        self.session.execute(u)
        self.session.commit()

    def update(self):
        u = update(self.table)
        u = u.values({"Estado": self.obj.status,
                      "Sigla":self.obj.sigla,
                      "ErrorCode":self.obj.erroCode,
                      "ErrorColumn":self.obj.errorColumn})
        u = u.where(self.table.c.Sigla == self.obj.sigla)
        self.session.execute(u)
        self.session.commit()


    def all(self):
        print("all")

    def findById(self):
        print('Find')
