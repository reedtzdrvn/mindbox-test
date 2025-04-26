from app.infrastructure.db.common.base import SessionLocal
from app.infrastructure.db.common.models import CategoryModel, ProductModel

INITIAL_CATEGORIES = [
    {'name': 'Electronics'},
    {'name': 'Books'},
    {'name': 'Food'},
    {'name': 'Health'},
]

INITIAL_PRODUCTS = [
    {'name': 'IPhone 16', 'categories': ['Electronics']},
    {'name': 'Xiaomi Mi Band 4', 'categories': ['Electronics', 'Health']},
    {'name': 'Withings Body+ Smart Scale', 'categories': ['Electronics', 'Health']},
    {'name': 'Apple Watch Series 7', 'categories': ['Electronics', 'Health']},
    {'name': 'Apple', 'categories': ['Food']},
    {'name': 'Banana', 'categories': ['Food']},
    {'name': 'Orange', 'categories': ['Food']},
    {'name': 'Judge and Punishment', 'categories': ['Books']},
    {'name': 'The Great Gatsby', 'categories': ['Books']},
    {'name': '1984', 'categories': ['Books']},
]

def seed_db():
    with SessionLocal() as db:
        with db.begin():
            cat_count = db.query(CategoryModel).count()
            prod_count = db.query(ProductModel).count()

            if cat_count == 0 and prod_count == 0:
                categories = []
                for cat_data in INITIAL_CATEGORIES:
                    cat = CategoryModel(name=cat_data['name'])
                    db.add(cat)
                    categories.append(cat)

                for prod_data in INITIAL_PRODUCTS:
                    prod = ProductModel(name=prod_data['name'])
                    for cat_name in prod_data["categories"]:
                        cat = next((c for c in categories if c.name == cat_name), None)
                        if cat:
                            prod.categories.append(cat)
                    db.add(prod)
            else:
                return


