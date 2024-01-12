from flask import Flask, render_template, request, redirect, url_for  #Import flask
from flask_sqlalchemy import SQLAlchemy #Import Datenbank
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, DateTime #Datenarten: Zahl, Zeichenkette, Datum
from sqlalchemy.orm import Mapped, mapped_column
import datetime #Modul für Datum (Ablaufdatum des Tasks)

db = SQLAlchemy() #Datenbank kreieren
#--------------------------------------------------------------------------------------------------------------------------------------------------

#TABELLE ERSTELLEN

class Todo(db.Model): #Tabellendaten: ID, Titel, Ablaufdatum
    __tablename__="todo"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True) #id wird automatisch vergeben
    title: Mapped[str] = mapped_column(String(40), nullable=False) #maximal 40 Zeichen für die Eingabe des Tasks 
    due: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=False),nullable=True) #Eingabe Datum 
    complete: Mapped[bool] = mapped_column(db.Boolean, default=False)
    category: Mapped[str] = mapped_column(String(50)) # Kategorien oder Tags



