from app import db, Countries, Cities
db.create_all() # Creates all table classes defined

first_entry = Customers(first_name = 'david', last_name = 'smith') #Add example to countries table
db.session.add(first_entry)
db.session.commit()

# Here we reference the country that london belongs to useing 'country', this is what we named the backref variable in db.relationship()
Stainless_daytona_41 = order_name(first_name='david',  Customers= first_entry)


db.session.add(Stainless_daytona_41)
db.session.commit()