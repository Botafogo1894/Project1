from app_FLASK import db, User, Tweet

# creates the User & Tweet models and tables in the database
db.create_all()

daniel = User(username="Daniel")
jeff = User(username="Jeff")
rachel = User(username="Rachel")

daniel.tweets = [Tweet(text="I love hogs"), Tweet(text="Hogs are the best way to teach react"), Tweet(text="Programming is lyfe")]

jeff.tweets = [Tweet(text="Data Science is awesome"), Tweet(text="Python is pretty neat"), Tweet(text="Wishing I was chillin' in mexico rn")]

rachel.tweets = [Tweet(text="RPDR is the best show"), Tweet(text="I just made the coolest NPM package!"), Tweet(text="Running is so fun!")]

db.session.add(jeff)
db.session.add(rachel)
db.session.add(daniel)
db.session.commit()
