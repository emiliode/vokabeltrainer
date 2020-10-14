from data import *
from flask import  Flask , render_template , request, make_response , Response
import sqlite3
import random
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/learn", methods=["POST", "GET"])
def hello():
    vocs = get_vocs("german_englisch")
    richtig = ""
    if request.method == "POST":
        print("\n Got: "+request.form["eingabe"])
        try:
            index = int(request.cookies.get("usedvocs").split(" ")[-1])
        except:
            return render_template("learn.html", voc="Oops something went wrong please go back to the main page" )
        if vocs[index][2] == request.form["eingabe"]:
            richtig = "Juhu richtig"
        else:
            richtig = "leider falsch"
    print("test")
    
    if request.cookies.get("usedvocs") == None: # should return list of strings  
        usedvocs = []
    else:
        usedvocs =request.cookies.get("usedvocs").split(" ")
    if len(usedvocs) >= len(vocs):
                
        resp = make_response(render_template("learn.html", voc="YOU FINISHED", richtig=richtig))    
        resp.set_cookie("usedvocs", "", expires=0)
        return resp
    ivoc = random.randint(0,len(vocs)-1)
    while str(ivoc) in usedvocs:
        ivoc = random.randint(0,len(vocs)-1)
        
    usedvocs.append(str(ivoc))
    resp = make_response(render_template("learn.html", voc=vocs[ivoc][1], richtig = richtig))
    resp.set_cookie("usedvocs"," ".join(usedvocs))
    #return render_template("index.html", voc=vocs[0][1])
    return resp

@app.route("/add", methods=["POST","GET"])
def add():
    if request.method == "POST":
        lang = request.form["lang"]
        voc1 = request.form["voc1"]
        voc2 = request.form["voc2"]
        add_voc(lang,voc1,voc2)
    return render_template
if __name__ == "__main__":
    app.run(debug=True)