from flask import Flask, render_template, request, redirect, url_for  #Import flask
from flask_sqlalchemy import SQLAlchemy #Import Datenbank
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, DateTime #Datenarten: Zahl, Zeichenkette, Datum
from sqlalchemy.orm import Mapped, mapped_column
import datetime #Modul für Datum (Ablaufdatum des Tasks)

#--------------------------------------------------------------------------------------------------------------------------------------------------
#INITIALISIERUNG FLASK

app = Flask(__name__) 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite" #Setzt die Datenbank-URI für SQLAlchemy (Datenspeicherung)
db = SQLAlchemy() #Datenbank kreieren
db.init_app(app)

#--------------------------------------------------------------------------------------------------------------------------------------------------
#TABELLE ERSTELLEN

class Todo(db.Model): #Tabellendaten: ID, Titel, Ablaufdatum
    __tablename__="todo"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True) #id wird automatisch vergeben
    title: Mapped[str] = mapped_column(String(40), nullable=False) #maximal 40 Zeichen für die Eingabe des Tasks 
    due: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=False),nullable=True) #Eingabe Datum 
    complete: Mapped[bool] = mapped_column(db.Boolean, default=False)
    category: Mapped[str] = mapped_column(String(50)) # Kategorien oder Tags

#--------------------------------------------------------------------------------------------------------------------------------------------------
#QUERY MODELS

@app.route('/')
def index(): #alle Tasks 
    todo_list = Todo.query.order_by(Todo.id.desc()).all() #Abfrage der Todo-Liste in umgekehrter Reihenfolge (neueste zuerst) nach ID
    current_date = datetime.datetime.now() #aktuelles Datum soll mit Eingabe verglichen werden
    return render_template("base.html", todo_list=todo_list, current_date=current_date) # HTML in Template-Dateien ausgelagert und mit render_template versendet

#--------------------------------------------------------------------------------------------------------------------------------------------------
#TASK UND DATUM HINZUFÜGEN

@app.route("/add", methods=["POST"]) #Route definieren, die auf POST-Anfragen an "/add" reagiert
def add():
    title = request.form.get("title") #title aus dem Formular abrufen
    due_str = request.form.get("due") #Fälligkeitsdatum als String aus dem Formular abrufen
    due_date = datetime.datetime.strptime(due_str, "%Y-%m-%d") if due_str else None #Fälligkeitsdatum aus dem String konvertieren, falls vorhanden, ansonsten None setzen
    category = request.form.get("category")
    new_todo = Todo(title=title, due=due_date, category=category) #neues Todo-Objekt
    db.session.add(new_todo) #neues Todo-Objekt hinzufügen
    db.session.commit() 
    return redirect(url_for("index")) #Weiterleitung zur 'index'-Route

# --------------------------------------------------------------------------------------------------------------------------------------------------
#TASK UPDATEN

@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("index"))

# --------------------------------------------------------------------------------------------------------------------------------------------------
#TASK LÖSCHEN

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

#--------------------------------------------------------------------------------------------------------------------------------------------------
#FILTER KATEGORIE PERMANTENT ANZEIGEN

@app.route('/category/<category_name>')
def tasks_by_category(category_name):
    todo_list = Todo.query.filter_by(category=category_name).all()
    current_date = datetime.datetime.now()
    return render_template("base.html", todo_list=todo_list, current_date=current_date, current_category=category_name)

#--------------------------------------------------------------------------------------------------------------------------------------------------
#DATENBANKERSTELLUNG UND RUN APPLIKATION

if __name__ == "__main__":
    with app.app_context():
        db.create_all() #Erstellt alle Datenbanktabellen, welche gemacht wurden
        app.run(debug=True, port=5000) #Flask-Entwicklungsserver
 
#--------------------------------------------------------------------------------------------------------------------------------------------------




