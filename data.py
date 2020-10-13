import sqlite3


def get_vocs(lang):
    """loads all vocabularys from a database

    Args:
        lang (String):(name of database without .db)   

    Returns:
        [list]: [list of tuples of all vocabulary]
    """
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

