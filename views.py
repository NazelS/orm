import peewee 
from models import Category, Product




def post_category(category_name):
    try:
       category = Category(name=category_name)
       category.save()
       print('SAVED!!!!')
    except peewee.IntegrityError:
        print('ТАКАЯ КОТЕГОРИЯ УЖЕ СУШЕСТВУЕТ !!!!')

def get_categories():
    categories = Category.select()
    for category in categories:
        print(f'{category.id}--{category.name}--{category.created_at}')


def delete_categories(category_id):
    try:
        category = Category.get(id=category_id)
        category.delete_instance()
        # print('DELETED!!!!')
    except peewee.DoesNotExist:
        print('категория не найдена')

def update_category(category_id, new_name):
    try:
        category = Category.get(id=category_id)
        category.name = new_name
        category.save()
        print('обновили ')
    except peewee.DoesNotExist:
        print('Категория не найдена !!!')
 
def detail_category(id_category):
    try:
        category = Category.get(id=id_category)
        print(category.id)
        print(category.name)
        print(category.created_at)
        for i in category.products:# [p1, p2 ,p1, p2, p2]
            print(f'{i.name}--{i.price}--{i.amount}')
    except peewee.DoesNotExist:
        print('нет такой котегории !!!')

def post_product(name,price,amount, category):
    try:
        product=Product(name=name, price=price, amount=amount, category=category)
        product.save()
    except peewee.IntegrityError:
        print('такой категории не существует!!!')

def get_products():
    products=Product.select()
    for i in products:
        print(f'{i.name}--{i.price}--{i.amount}--{i.cotegory.name}--{i.cotegory.id}')


def get_product_by_name(name):
    products=Product.select().where(name==name)# select * from product where name='product'
    for i in products:
        print(i.name, i.price)
    

get_product_by_name('product2')
# get_products()#увидеть все котегории 
# post_product('product6', 30, 10, 2)
# posr_product('product1', 30, 10, 4) #один ко многим 2 разных обьекта 
# # post_category('game2')
# get_categories()
# update_category(2)
# get_categories()
# get_categories()
detail_category(2)