from .entity import Entity

class Log(Entity):
    Id = 0
    TableName = 'tblLog'

    # default constructor
    def __init__(self,status,sigla,erroCode,errorColumn):
        self.status = status
        self.sigla = sigla
        self.erroCode = erroCode
        self.erroColumn = errorColumn