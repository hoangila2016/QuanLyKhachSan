from app.models import Category,Product

def get_category():
    return Category.query.all()

def get_product():
    return Product.query.all()