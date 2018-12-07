from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User
import datetime

# Create database
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Create category of Action Films
category1 = Category(user_id=1, name="Action Films")
session.add(category1)
session.commit()

# Create category of Adventure Films
category2 = Category(user_id=1, name="Adventure Films")
session.add(category2)
session.commit()

# Create category of Comedy Films
category3 = Category(user_id=1, name="Comedy Films")
session.add(category3)
session.commit()

# Create category of Drama Films
category4 = Category(user_id=1, name="Drama Films")
session.add(category4)
session.commit()

# Create category of Science Fiction Films
category5 = Category(user_id=1, name="Science Fiction Films")
session.add(category5)
session.commit()


# Add Items into categories

categoryItem1 = Item(user_id=1, title="The Secret Life of Pets",
                             description="The quiet life of a terrier \
                             named Max is upended when his owner takes \
                             in Duke, a stray whom Max instantly dislikes.",
                            date=datetime.datetime.now(),
                             category=category3)
session.add(categoryItem1)
session.commit()


categoryItem2 = Item(user_id=1, title="Hidden Figures",
                             description="The story of a team of female\
                              African-American mathematicians who served\
                               a vital role in NASA during the early years\
                                of the U.S. space program.",
                                date=datetime.datetime.now(),
                             category=category4)
session.add(categoryItem2)
session.commit()


categoryItem3 = Item(user_id=1, title="The Martian",
                             description="An astronaut becomes stranded on \
                             Mars after his team assume him dead, and must \
                             rely on his ingenuity to find a way to signal \
                             to Earth that he is alive.",
                             date=datetime.datetime.now(),
                             category=category5)
session.add(categoryItem3)
session.commit()


categoryItem4 = Item(user_id=1, title="Kingsman: The Golden Circle",
                             description="When their headquarters are \
                             destroyed and the world is held hostage, \
                             the Kingsman's journey leads them to the \
                             discovery of an allied spy organization in \
                             the US. These two elite secret organizations \
                             must band together to defeat a common enemy.",
                            date=datetime.datetime.now(),
                             category=category1)
session.add(categoryItem4)
session.commit()


categoryItem5 = Item(user_id=1, title="Dunkirk",
                             description="Allied soldiers from Belgium, \
                             the British Empire and France are surrounded\
                              by the German Army, and evacuated during a \
                              fierce battle in World War II.",
                            date=datetime.datetime.now(),
                             category=category4)
session.add(categoryItem5)
session.commit()


categoryItem6 = Item(user_id=1, title="Star Wars: The Last Jedi",
                             description="Having taken her first steps into\
                              a larger world in Star Wars: The Force Awakens\
                               (2015), Rey continues her epic journey with \
                               Finn, Poe, and Luke Skywalker in the next \
                               chapter of the saga.",
                            date=datetime.datetime.now(),
                             category=category5)
session.add(categoryItem6)
session.commit()

categoryItem7 = Item(user_id=1, title="Deadpool",
                             description="A fast-talking mercenary with \
                             a morbid sense of humor is subjected to a rogue\
                              experiment that leaves him with accelerated \
                              healing powers and a quest for revenge.",
                            date=datetime.datetime.now(),
                             category=category1)
session.add(categoryItem7)
session.commit()

categoryItem8 = Item(user_id=1,
                             title="Pirates of the Caribbean: \
                             Dead Men Tell No Tales",
                             description="Captain Jack Sparrow searches \
                             for the trident of Poseidon while being pursued\
                              by an undead sea captain and his crew.",
                            date=datetime.datetime.now(),
                             category=category2)
session.add(categoryItem8)
session.commit()


categoryItem9 = Item(user_id=1, title="Despicable Me 3",
                             description="Gru meets his long-lost charming,\
                              cheerful, and more successful twin brother Dru\
                               who wants to team up with him for one last\
                                criminal heist.",
                            date=datetime.datetime.now(),
                             category=category3)
session.add(categoryItem9)
session.commit()

print "added category items!"
