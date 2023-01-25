import peewee
from peewee import PostgresqlDatabase



db = PostgresqlDatabase(   
    'orm_py25',
    user = 'hello',
    password = '1',
    host='localhost',
    port=5432
)
