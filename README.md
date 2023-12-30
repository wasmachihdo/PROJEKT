# **Todo-Anwendung**

## **Einführung / Projektidee**

- **Projektauftrag:** Im Rahmen des Moduls Programmieren 2 soll mit Hilfe des Microframeworks Flask eine Webapplikation entwickelt werden.

- **Ausgangspunkt:** Die Entwicklung einer Todo-Anwendung entstand aus dem Bedarf an einem einfachen, aber effektiven Werkzeug zur Verwaltung täglicher Aufgaben. Die Anwendung wurde mit Flask entwickelt und bietet eine benutzerfreundliche Übersicht, um Aufgaben mit Fälligkeitsdaten hinzuzufügen, zu aktualisieren und zu löschen.
- **Ziel:** Ziel war es, eine benutzerfreundliche Anwendung so zu programmieren, dass der Code nachvollziehbar ist. 

## **Funktionen**

- **Aufgaben hinzufügen:** Benutzer können neue Aufgaben (Tasks) mit Titeln und optionalen Fälligkeitsdaten hinzufügen.
- **Aufgaben anzeigen:** Alle Aufgaben werden auf der Hauptseite aufgelistet, überfällige Aufgaben werden in roter Farbe hervorgehoben.
- **Aufgabenstatus aktualisieren:** Aufgaben können als abgeschlossen oder nicht abgeschlossen markiert werden. Die Voreinstellung einer neuen Aufgabe ist 'not completed' (nicht abgeschlossen) und kann mit dem Button 'Modify Status' geändert werden.
- **Aufgaben löschen:** Benutzer können Aufgaben löschen (Button 'Delete').
- **Kategorisierung von Aufgaben:** Benutzer können den Aufgaben Kategorien ('Personal', 'Work', 'Urgent') zuteilen und die Tasks anschliessend basierend auf diesen Kategorien filtern.

## **Installation und Einrichtung**

### **Voraussetzungen:**

- Python 3
- Flask
- Flask-SQLAlchemy

### **Installation:**

1. **Repository klonen**
    
2. **Einrichten einer virtuellen Umgebung**
 
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

- **Aufgaben zuteilen und filtern:**
  - Aufgaben können Kategorien zugeteilt werden. um sie nachher zu filtert.

## **Datenmanagement**
- **Einlesen:** Die App lädt die Aufgaben beim Start aus einer SQLite-Datenbank.
- **Speichern:** Änderungen an Aufgaben werden automatisch in der Datenbank gespeichert.
- **Ausgeben:** Verschiedene Ansichten ermöglichen eine bessere Übersicht der Aufgaben.

## Kommentare im Code
- Jeder Funktion und Klasse im Code sind erklärende Kommentare vorangestellt, welche Zweck und Funktionsweise erläutern. 
- Wichtige Codeblöcke, etwa solche mit komplexerer Logik, sind mit Inline-Kommentaren versehen.

## **Verwendete Technologien**

- **primäre Programmiersprache:** Python
- **Backend:** Flask
- **Datenbank:** SQLAlchemy (SQLite)
- **Frontend:** HTML, CSS
