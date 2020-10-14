import sqlite3

def create_table(lang):
    conn = sqlite3.connect("vocabulary.db")
    conn.cursor().execute(f""" CREATE TABLE {lang}(
    id INT PRIMARY KEY,
    {lang.split('_')[0]} CHAR(25),
    {lang.split('_')[1]} CHAR(25)
    );""")
    conn.commit()

def delete_table(name):
    conn = sqlite3.connect("vocabulary.db")
    conn.cursor().execute(f"DROP TABLE {name}")
    conn.close()
def get_vocs(lang):
    """loads all vocabularys from a database

    Args:
        lang (String):name of table    

    Returns:
        [list]: [list of tuples of all vocabulary]
    """
    conn = sqlite3.connect("vocabulary.db")
    cur = conn.cursor()
    
    cur.execute("SELECT  * FROM "+lang)
    rows = cur.fetchall()
    print("\n [+] Querying the data \n")
    return rows

def add_voc(lang, voc1, voc2):
    conn = sqlite3.connect("vocabulary.db")
    cur = conn.cursor()
    lang1= lang.split("_")[0]
    lang2= lang.split("_")[1]
    try:
        cur.execute("SELECT max(id) FROM "+lang)
        print(cur.fetchone()[0])
        try:
            id = int(intcur.fetchone()[0])+1
        except:
            id=0
    except:
        create_table(lang)
        cur.execute("SELECT max(id) FROM "+lang)
        id = 0
    
    #cur.execute(f"INSERT INTO vocs (id ,{lang1},{lang2}) VALUES ({id},{voc1},{voc2})")
    cur.execute(f"INSERT INTO {lang} (id ,{lang1},{lang2}) VALUES ({id},'{voc1}','{voc2}')")
    conn.commit()

#add_voc("german_french", "Guten Tag", "Bonjour")
if __name__ == "__main__":
    conn = sqlite3.connect("vocabulary.db")
    cur = conn.cursor()
    cur.execute("DROP TABLE german_french")