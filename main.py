from Domain.log import Log
from Data.logrepository import LogRepository



if __name__ == '__main__':

    repository = LogRepository()
    retorno = repository.findById(1)
    print(retorno)
    log = Log('TTTT','TX',3,3)
    repository.add(log)
    retorno = repository.all()
    log.Id = 14
    repository.delete(log)
    log.Id = 10
    retorno = repository.update(log)
    print(retorno)

