from flask import Flask,request
import modulok.html_utility as hu
import pickle


app=Flask(__name__)
try:
    szotar = pickle.load(open("nagyszotart.dat", "rb")) #type:dict
except Exception as hiba:
    print("hiba")


@app.route("/")
def index():
    html="""
    <h2>Fooldal</h2>
    <a href='/angolszotar'>Angol-Magyar szotar</a><br>
    <a href='/szoszedet'>Angol-Magyar szoszedet</a>
    """
    return hu.correct_html("Fooldal",html)

@app.route("/angolszotar")
def angolszotar():
    html="""
    <form>
    Kerem az angol kifejezest:
    <input type='text' name='angol'>
    <input type='submit' value='Forditsd'>
    </form>
    """
    if request.args:
        angol=request.args.get("angol")
        html+="<b>{}</b> - {}".format(angol,szotar.get(angol,"Nem talalhato a szotarban"))
    return hu.correct_html("Angol Szotar", html)

@app.route("/szoszedet")
def szoszedet():
    html="<h2>Szoszedet</h2>"
    html+="<ol>"
    for szopar in szotar.items():
        angol,magyar=szopar
        html+="<li>{} = {}<li>".format(angol,magyar)
    html+="</ol>"
    return hu.correct_html("Szoszedet",html)

if __name__=="__main__":
    app.run()