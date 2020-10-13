from data import get_vocs, add_voc 
from flask import  Flask , render_template , request
import sqlite3
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def hello():
    if request.method == "POST":
        print("\n Got: "+request.form["eingabe"])
    vocs = get_vocs("german-englisch")
    print("test")
    return render_template("index.html", voc=vocs[0][1])





    
    

if __name__ == "__main__":
    app.run(debug=True)