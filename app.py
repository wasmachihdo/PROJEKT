from flask import Flask, render_template



app = Flask(__name__)



@app.route('/')
def index():
    return render_template("base.html") # HTML in Template-Dateien ausgelagert und mit render_template versendet



if __name__ == "__main__":
    app.run(debug=True, port=5000)
 
 



