# pythonRepository

pythonRepository is a basic framework for creating the repository layer. The goal is to be a basic model for creating the persistence layer using SQLAlchemy and abc — Abstract Base Classes.

## Install

pip install SQLAlchemy


make a clone of the project.

https://github.com/santanna106/pythonRepository.git

## Use

To use the framework create the domain class and then the repository class following the example below

### Abstract class of the Domain 
```
import abc

class Entity(metaclass=abc.ABCMeta):

    @property
    def Id(self):
        raise NotImplementedError
```
        
### Domain class

```
from .entity import Entity

class Log(Entity):
    Id = 0

    # default constructor
    def __init__(self,status,sigla,errorCode,errorColumn,id = 0):
        Id = id
        self.status = status
        self.sigla = sigla
        self.errorCode = errorCode
        self.errorColumn = errorColumn
```        
        
### Repository class   

```
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import insert
import sqlalchemy as sal
from .irepository import IRepository

class LogRepository(IRepository):

    __table = 'table Name'

    def __init__(self) -> None:
        self.engine = sal.create_engine('connection String')
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

```





## License
[MIT](https://choosealicense.com/licenses/mit/)

