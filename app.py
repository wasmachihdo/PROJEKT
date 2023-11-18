from flask import Flask, render_template #Import flask
from flask_sqlalchemy import SQLAlchemy #Import Datenbank
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
import datetime


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite" #Generierung der Datei

db = SQLAlchemy() #Datenbank kreieren
db.init_app(app)

class Todo(db.Model):
    __tablename__="todo"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True) 
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    due: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=False),nullable=True) 





@app.route('/')
def index(): #show all todos 
    db.query(Todo) # recherchieren Query Models 
    return render_template("base.html") # HTML in Template-Dateien ausgelagert und mit render_template versendet



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        todo = Todo(title="task 1")
        db.session.add(todo)
        db.session.commit()
    app.run(debug=True, port=5000)
 
 



