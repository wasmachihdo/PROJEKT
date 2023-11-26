from flask import Flask, render_template, request #Import flask
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

#--------------------------------------------------------------------------------------------------------------------------------------------------
#QUERY MODELS -> 24.11

@app.route('/')
def index(): #alle Tasks  
    todo_list = Todo.query.all() #Liste generieren  
    return render_template("base.html", todo_list=todo_list) # HTML in Template-Dateien ausgelagert und mit render_template versendet

#--------------------------------------------------------------------------------------------------------------------------------------------------
#Task hinzufügen
#def add()
#complete=false

#--------------------------------------------------------------------------------------------------------------------------------------------------
#datetime


#--------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        new_todo = Todo(title="task 1") #Hinzugügen eines neuen Tasks (Nummer weitergehen??)
        db.session.add(new_todo)
        db.session.commit()
    app.run(debug=True, port=5000)
 
#--------------------------------------------------------------------------------------------------------------------------------------------------




