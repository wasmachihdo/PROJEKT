# **Todo-Anwendung**

## **Einführung / Projektidee**

- **Projektauftrag:** Im Rahmen des Moduls Programmieren 2 soll mit Hilfe des Microframeworks Flask eine Webapplikation entwickelt werden.

- **Ausgangspunkt:** Die Entwicklung einer Todo-Anwendung entstand aus dem Bedarf an einem einfachen, aber effektiven Werkzeug zur Verwaltung täglicher Aufgaben. Die Anwendung wurde mit Flask entwickelt und bietet eine benutzerfreundliche Übersicht, um Aufgaben mit Fälligkeitsdaten hinzuzufügen, zu aktualisieren und zu löschen.
- **Ziel:** Ziel war es, eine benutzerfreundliche Anwendung so zu programmieren, dass der Code nachvollziehbar und verständlich ist. 

## **Funktionen**

- **Aufgaben hinzufügen:** Benutzer können neue Aufgaben (Tasks) hinzufügen und diese optional mit Fälligkeitsdatum versehen und zu einer Kategorie zuordnen.
- **Aufgaben anzeigen:** Alle Aufgaben werden auf der Hauptseite aufgelistet, überfällige Aufgaben werden in roter Farbe hervorgehoben.
- **Aufgabenstatus aktualisieren:** Aufgaben können als abgeschlossen oder nicht abgeschlossen markiert werden. Die Voreinstellung einer neuen Aufgabe ist 'not completed' (nicht abgeschlossen) und kann mit dem Button 'Modify Status' geändert werden. Abgeschlossene Aufgaben werden mit reduzierter Transparenz dargestellt, um sie visuell von den offenen Aufgaben abzuheben. 
- **Aufgaben löschen:** Benutzer können Aufgaben löschen (Button 'Delete').
- **Kategorisierung von Aufgaben:** Benutzer können den Aufgaben Kategorien ('Personal', 'Work', 'Urgent') zuteilen und die Tasks anschliessend basierend auf diesen Kategorien filtern. Die Zuteilung ist aber nicht erforderlich.

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
  - Titel der Aufgabe, Fälligkeitsdatum und Ketegorie angeben.
  - Auf den Button 'ADD' klicken.

- **Aufgabenstatus aktualisieren:**
  - Auf den Button 'Modify Status' klicken.

- **Eine Aufgabe löschen:**
  - Auf den Button 'Delete' bei der zu entfernenden Aufgabe klicken.

- **Aufgaben zuteilen und filtern:**
  - Aufgaben können Kategorien zugeteilt werden. um sie nachher zu filtert.

**Optimale Nutzung**

- **Anzeigeformat:** Die Anwendung ist flexibel einsetzbar und funktioniert auf verschiedenen Bildschirmgrössen. Sie wurde jedoch für die Nutzung in einem kleinen Fenster (die Hälfte bis ein Viertel der Bildschirmgrösse) optimiert.
- **Anwendungszweck:** Diese Grösseneinstellung wurde gewählt, um die App als praktisches Hilfsmittel für schnelle Notizen und Aufgabenlisten zu nutzen, die parallel zu anderen Aufgaben auf dem Desktop verwendet werden können. Nutzer können somit die Todo-Liste bequem neben ihren anderen Anwendungen offen halten, um effizient zwischen ihrer Todo-Liste und anderen Aktivitäten zu wechseln.

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
