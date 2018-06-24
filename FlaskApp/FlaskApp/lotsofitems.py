from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_bee_setup import Category, Item, Base, User

engine = create_engine('sqlite:///categorywithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create a user
User1 = User(name="Jim Barry", email="jbarry@pelicom.net",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Menu for Beekeeping Kits
category1 = Category(user_id=1, name="Beekeeping Kits")

session.add(category1)
session.commit()

item1 = Item(user_id=1, name="10 Frame Hive", description="10 frame super with telescoping top, inner cover, screened bottom board and 10 frames",
                     price="$237.50", category=category1)

session.add(item1)
session.commit()


item2 = Item(user_id=1, name="8 Frame Hive", description="8 frame super with telescoping top, inner cover, screened bottom board and 8 frames",
                     price="$212.40", category=category1)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="5 Frame Hive", description="5 frame super with telescoping top, inner cover, screened bottom board and 5 frames",
                     price="$41.40", category=category1)

session.add(item3)
session.commit()

# Menu for loaded supers with foundation
category2 = Category(user_id=1, name="Loaded Supers")

session.add(category2)
session.commit()


item1 = Item(user_id=1, name="10 Frame Deep", description="Deep Super with 10 Frames and Foundation",
                     price="$46.80", category=category2)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="8 Frame Deep", description="Deep Super with 8 Frames and Foundation",
                     price="$42.00", category=category2)

session.add(item1)
session.commit()


# Menu for Panda Garden
category3 = Category(user_id=1, name="Supers")

session.add(category3)
session.commit()

item1 = Item(user_id=1, name="10 Frame Super Unassembled", description="10 Frame Super Unassembled.",
                     price="$13.20", category=category3)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="10 Frame Super Assembled", description="10 Frame Super Assembled.",
                     price="$15.60", category=category3)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="8 Frame Super Unassembled", description="8 Frame Super Unassembled.",
                     price="$12.60", category=category3)

session.add(item3)
session.commit()

item4 = Item(user_id=1, name="8 Frame Super Assembled", description="8 Frame Super Assembled.",
                     price="$15.00", category=category3)

session.add(item4)
session.commit()

item5 = Item(user_id=1, name="5 Frame Super Unassembled", description="5 Frame Super Unassembled.",
                     price="$10.20", category=category3)

session.add(item5)
session.commit()

item6 = Item(user_id=1, name="5 Frame Super Assembled", description="5 Frame Super Assembled.",
                     price="$12.60", category=category3)

session.add(item6)
session.commit()


# Menu for Thyme for that
category4 = Category(user_id=1, name="Miscellaneous")

session.add(category4)
session.commit()


item1 = Item(user_id=1, name="Plastic Closure", description="Plastic closure for screen bottom.",
                     price="$1.20", category=category4)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Entrance Reducer", description="Entrance Reducer - 8 or 10 Frame.",
                     price="$1.20", category=category4)

session.add(item2)
session.commit()
print "added menu items!"
