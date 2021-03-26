import sqlalchemy as sal
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import insert

engine = sal.create_engine('mssql+pyodbc://Teste')
Session = sessionmaker(bind=engine)
session = Session()

# define meta information
metadata = MetaData(bind=engine)
mytable = Table('tblLog', metadata, autoload=True)

s = mytable.select() # or:
result = session.execute(s)
out = result.fetchall()
print(out)

print('ANTES')
i = insert(mytable)
i = i.values({"Estado": "va", "Sigla": "Va", "ErrorCode": "2", "ErrorColumn": "1"})
session.execute(i)
session.commit()

# update
u = update(mytable)
u = u.values({"Estado": "Sao Paulo"})
u = u.where(mytable.c.Sigla == "SP")
session.execute(u)
session.commit()

# update
u = delete(mytable)
u = u.where(mytable.c.Sigla == "RJ")
session.execute(u)
session.commit()

