from flask import Flask, render_template, request, redirect, url_for  #Import flask
from flask_sqlalchemy import SQLAlchemy #Import der SQLAlchemy-Erweiterung für Flask
from sqlalchemy.orm import DeclarativeBase #Import von DeclarativeBase aus SQLAlchemy -> Declarative Mapping 
from sqlalchemy import Integer, String, DateTime #Datenarten: Zahl, Zeichenkette, Datum
from sqlalchemy.orm import Mapped, mapped_column #Import von Mapped und mapped_column aus SQLAlchemy ORM, für Definition von Attributen in ORM-Modellen
import datetime #Modul für Datum (Ablaufdatum des Tasks)

from models import Todo, db

#--------------------------------------------------------------------------------------------------------------------------------------------------
#INITIALISIERUNG FLASK

app = Flask(__name__) 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite" #Setzt die Datenbank-URI für SQLAlchemy (Datenspeicherung)
db.init_app(app)


#--------------------------------------------------------------------------------------------------------------------------------------------------
#QUERY MODELS

@app.route('/')
def index(): #alle Tasks 
    todo_list = Todo.query.order_by(Todo.complete, Todo.id.desc()).all()   # Abfrage, die zuerst nicht abgeschlossene und dann abgeschlossene Todos anzeigt
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
    return redirect(url_for("index")) # Redirect zur Indexpage, um die Gesamtübersicht anzuzeigen

# --------------------------------------------------------------------------------------------------------------------------------------------------
#TASK UPDATEN

@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first() # Findet das Todo anhand seiner ID
    todo.complete = not todo.complete # Ändert den Status von abgeschlossen/nicht abgeschlossen
    db.session.commit() # Speichert die Änderung
    return redirect(url_for("index")) # Redirect immer zur Indexpage, um die Gesamtübersicht anzuzeigen

# --------------------------------------------------------------------------------------------------------------------------------------------------
#TASK LÖSCHEN

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first() # Findet das zu löschende Todo
    db.session.delete(todo) # Löscht das Todo aus der Datenbank
    db.session.commit() # Speichert die Änderung
    return redirect(url_for("index")) # Redirect immer zur Indexpage, um die Gesamtübersicht anzuzeigen

#--------------------------------------------------------------------------------------------------------------------------------------------------
#FILTER KATEGORIE PERMANTENT ANZEIGEN

@app.route('/category/<category_name>')
def tasks_by_category(category_name):
    todo_list = Todo.query.filter_by(category=category_name).all() # Filtert Todos nach Kategorie
    current_date = datetime.datetime.now()
    return render_template("base.html", todo_list=todo_list, current_date=current_date, current_category=category_name)

#--------------------------------------------------------------------------------------------------------------------------------------------------
#DATENBANKERSTELLUNG UND RUN APPLIKATION

if __name__ == "__main__":
    with app.app_context():
        db.create_all() # Erstellt alle Datenbanktabellen, welche gemacht wurden
        app.run(debug=True, port=5000) # Startet den Flask-Entwicklungsserver
 
#--------------------------------------------------------------------------------------------------------------------------------------------------