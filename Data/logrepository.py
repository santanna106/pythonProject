from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import insert
import sqlalchemy as sal
from .irepository import IRepository

class LogRepository(IRepository):
    __table = 'tblLog'

    def __init__(self) -> None:
        self.engine = sal.create_engine('mssql+pyodbc://Teste')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.metadata = MetaData(bind=self.engine)
        self.table = Table(self.__table, self.metadata, autoload=True)


    def add(self,object):
        i = insert(self.table)
        i = i.values({"Estado": object.status,
                      "Sigla": object.sigla,
                      "ErrorCode": object.errorCode,
                      "ErrorColumn": object.errorColumn})
        self.session.execute(i)
        self.session.commit()

    def delete(self,object):
        u = delete(self.table)
        u = u.where(self.table.c.Id == object.Id)
        self.session.execute(u)
        self.session.commit()

    def update(self,object):
        u = update(self.table)
        u = u.values({"Estado": object.status,
                      "Sigla":object.sigla,
                      "ErrorCode":object.errorCode,
                      "ErrorColumn":object.errorColumn})
        u = u.where(self.table.c.Id == object.Id)
        self.session.execute(u)
        self.session.commit()


    def all(self):
        result = self.session.query(self.table).all()
        return result

    def findById(self,Id):
        return  self.session.query(self.table).filter_by(Id=Id).first()
