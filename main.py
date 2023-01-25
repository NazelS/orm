# import peewee
# ORM (Object Relational Mapping - объектно реляционное отображение) - технология которая связывает БД с концепциями объектно ориентированных языков программирования. ORM - прослойка между БД и кодом который пишет программист, которая позволяет создавать в программе объекты обновлять, удалять и получать их


# python:
#     peewee
#     sqlalchemy
#     DjangoORM


# класс - таблица в БД
# атрибут класса - поле в БД
# обЪект класса - строка в таблице
# """



# # объект(db) от класса (PostgresqlDatabase) - настройка соединения субд к файлу



# c1 \dt
# c2 
# p1 - c1 
# p2 - c1
# p3 - c1
# p4 - c1
# p5 - c2
# p6 - c2

from views import*
from settings import db

db.connect()
get_categories()
get_products()
db.close()


             ########ПОДГОТОВКА К ИНТЕРВЬЮ########

# class A:
#     __age =0
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self,new):
#         self.age=new
# object=A()
# object._A__age=3
# print(object)

# def func():
#     try:
#         return 0
#     finally:  #ПЕРЕЗАПИСЬ ЗНАЧЕНИЯ 
#         return 1
# print(func())
git@github.com:NazelS/orm.git





 