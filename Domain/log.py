from .entity import Entity

class Log(Entity):
    Id = 0
    TableName = 'tblLog'

    # default constructor
    def __init__(self,status,sigla,errorCode,errorColumn,id = 0):
        Id = id
        self.status = status
        self.sigla = sigla
        self.errorCode = errorCode
        self.errorColumn = errorColumn