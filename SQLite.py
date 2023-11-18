import sqlite3

app.config["SQL_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQL_TRACK_MODIFICATIONS"] = False
db = sqlite3(app)



