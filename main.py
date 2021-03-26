from Domain.log import Log
from Data.logrepository import LogRepository



if __name__ == '__main__':
    log = Log('Test','Te',1,1)
    repository = LogRepository(log)
    repository.add()
