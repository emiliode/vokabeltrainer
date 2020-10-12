from dearpygui.core import  *
import sqlite3
#add_additional_font("arial.ttf", 20, )
#add_text("Vokabel trainer")
#def start_clicked(sender, data):
#    print("clicked: "+sender )
#add_button("start" , callback = start_clicked)

#start_dearpygui()

def get_vocs(lang):
    conn = sqlite3.connect(lang+".db", )
    cur = conn.cursor()
    cur.execute("SELECT  * FROM vocs")
    rows = cur.fetchall()
    print("\n [+] Querying the data \n")
    return rows

def add_voc(lang, voc1, voc2):
    conn = sqlite3.connect(lang+".db", )
    cur = conn.cursor()
    lang1= lang.split("-")[0]
    lang2= lang.split("-")[1]
    cur.execute("SELECT max(id) FROM vocs")
    id =cur.fetchone()[0]+1
    #cur.execute(f"INSERT INTO vocs (id ,{lang1},{lang2}) VALUES ({id},{voc1},{voc2})")
    cur.execute(f"INSERT INTO vocs (id ,{lang1},{lang2}) VALUES ({id},'{voc1}','{voc2}')")
    conn.commit()
get_vocs("german-englisch")
add_voc("german-englisch", "Gut","good")

