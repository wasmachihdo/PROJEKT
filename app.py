from flask import Flask, render_template, request, redirect, url_for  #Import flask
from flask_sqlalchemy import SQLAlchemy #Import Datenbank
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, DateTime #Datenarten: Zahl, Zeichenkette, Datum
from sqlalchemy.orm import Mapped, mapped_column
import datetime #Modul für Datum (Ablaufdatum des Tasks)

#--------------------------------------------------------------------------------------------------------------------------------------------------

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite" #Generierung der Datei zur Datenspeicherung
db = SQLAlchemy() #Datenbank kreieren
db.init_app(app)

#--------------------------------------------------------------------------------------------------------------------------------------------------

class Todo(db.Model): #Tabellendaten: ID, Titel, Ablaufdatum
    __tablename__="todo"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True) #id wird automatisch vergeben
    title: Mapped[str] = mapped_column(String(80), nullable=False) #maximal 80 Zeichen für die Eingabe des Tasks
    due: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=False),nullable=True) #Eingabe Datum 
    complete: Mapped[bool] = mapped_column(db.Boolean, default=False)

#--------------------------------------------------------------------------------------------------------------------------------------------------
#QUERY MODELS -> 24.11

@app.route('/')
def index(): #alle Tasks  
    todo_list = Todo.query.all() #Liste generieren  
    return render_template("base.html", todo_list=todo_list) # HTML in Template-Dateien ausgelagert und mit render_template versendet

#--------------------------------------------------------------------------------------------------------------------------------------------------
#Task hinzufügen
@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))

# --------------------------------------------------------------------------------------------------------------------------------------------------
#Task updaten
@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("index"))

# --------------------------------------------------------------------------------------------------------------------------------------------------
#Task löschen
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))




#--------------------------------------------------------------------------------------------------------------------------------------------------
#datetime


#--------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5000)
 
#--------------------------------------------------------------------------------------------------------------------------------------------------




