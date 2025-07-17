from ext import db, app
from models import Item,  User

with app.app_context():
    db.drop_all()
    db.create_all()
    item1 = Item(name="Bunny-20 GEL", image="photo2.png")
    item2 = Item(name="Dino-15 GEL", image="photo1.png")
    item3 = Item(name="Duck-15 GEL", image="photo3.png")
    item4 = Item(name="Hello kitty-20 GEL", image="pr1.png")
    item5 = Item(name="Red bag with a white bow-30 GEL", image="pr2.png")
    item6 = Item(name="Pouch with bows-15 GEL", image="pr3.png")
    item7 = Item(name="Book cover-15 GEL", image="pr4.png")
    item8 = Item(name="Asymmetrical green top-15 GEL", image="pr5.png")
    item9 = Item(name="Blue valentine's bag-15 GEL", image="pr6.png")

    db.session.add_all([item1, item2, item3, item4, item5, item6, item7, item8, item9])
    db.session.commit()
