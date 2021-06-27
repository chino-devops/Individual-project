from appdb import db, customers, orders
db.drop_all()
db.create_all() # Creates all table classes defined

first_entry = customers(name = 'david smith') #Add example to countries table
db.session.add(first_entry)
db.session.commit()

# Here we reference the country that london belongs to useing 'country', this is what we named the backref variable in db.relationship()
Stainless_daytona_41 = orders(order_name='stainless steel daytona 41', order_entry = first_entry)
chromemaster_41 = orders(order_name='chromemaster 41', order_entry = first_entry)
Skeleton_41 = orders(order_name='skeleton 41', order_entry = first_entry)
nautilus_41 = orders(order_name='nautilus 41', order_entry = first_entry)
overseas_41 = orders(order_name='overseas 41', order_entry = first_entry)


db.session.add(Stainless_daytona_41)
db.session.add(chromemaster_41)
db.session.add(skeleton_41)
db.session.add(nautilus_41)
db.session.add(overseas_41)
db.session.commit()