from flask import Flask, render_template
import datetime


app=Flask(__name__)

#www.mojastrona.pl

@app.route("/")
def index():
    tekst="Witaj uzytkowniku"
    aktualna_data = datetime.datetime.now()
    imiona=["Adam","Rafal","Monika","Ewa"]

    return render_template("index.html",text=tekst,data=aktualna_data,tablica=imiona)

@app.route("/about")
def about():
    return render_template('about.html')

#Jinja2

if __name__ =="__main__":
    app.run()