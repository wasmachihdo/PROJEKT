# **Todo-Anwendung**

## **Einführung**

Diese Todo-Anwendung ist ein einfaches, aber leistungsfähiges Werkzeug zur Verwaltung der täglichen Aufgaben. Die Anwendung wurde mit Flask entwickelt und bietet eine benutzerfreundliche Übersicht, um Aufgaben mit Fälligkeitsdaten hinzuzufügen, zu aktualisieren und zu löschen.

## **Funktionen**

- **Aufgaben hinzufügen:** Benutzer können neue Aufgaben (Tasks) mit Titeln und optionalen Fälligkeitsdaten hinzufügen.
- **Aufgaben anzeigen:** Alle Aufgaben werden auf der Hauptseite aufgelistet, überfällige Aufgaben werden in roter Farbe hervorgehoben.
- **Aufgabenstatus aktualisieren:** Aufgaben können als abgeschlossen oder nicht abgeschlossen markiert werden. Die Voreinstellung einer neuen Aufgabe ist 'not completed' (nicht abgeschlossen) und kann mit dem Button 'Modify Status' geändert werden.
- **Aufgaben löschen:** Benutzer können Aufgaben löschen (Button 'Delete').

## **Installation und Einrichtung**

### **Voraussetzungen:**

- Python 3
- Flask
- Flask-SQLAlchemy

### **Installation:**

1. **Repository klonen**
    
2. **Einrichten einer virtuellen Umgebung (venv)**

    
3. **Abhängigkeiten installieren (Flask-SQLAlchemy)**

    
4. **Anwendung starten (flask run)**

    
    Die Anwendung sollte nun unter `http://127.0.0.1:5000/` laufen.

## **Nutzung**

- **Eine Aufgabe hinzufügen:**
  - Titel der Aufgabe und Fälligkeitsdatum (optional) eingeben.
  - Auf den Button 'Add' klicken.

- **Aufgabenstatus aktualisieren:**
  - Auf den Button 'Modify Status' klicken.

- **Eine Aufgabe löschen:**
  - Auf den Button 'Delete' bei der zu entfernenden Aufgabe klicken.

## **Datenmanagement**
- **Einlesen:** Die App lädt die Aufgaben beim Start aus einer SQLite-Datenbank.
- **Speichern:** Änderungen an Aufgaben werden automatisch in der Datenbank gespeichert.
- **Ausgeben:** Verschiedene Ansichten ermöglichen eine bessere Übersicht der Aufgaben.

## **Verwendete Technologien**

- **primären Programmiersprache:** Python
- **Backend:** Flask
- **Datenbank:** SQLAlchemy (SQLite)
- **Frontend:** HTML, CSS
