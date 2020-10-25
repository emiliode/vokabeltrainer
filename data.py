import sqlite3
databasename = "vocs.db"


def create_table(lang):
    conn = sqlite3.connect(databasename)
    conn.cursor().execute(f""" CREATE TABLE {lang}(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    {lang.split('_')[0]} CHAR(25),
    {lang.split('_')[1]} CHAR(25)
    );""")
    conn.commit()
    conn.close()


def delete_table(name):
    conn = sqlite3.connect(databasename)
    conn.cursor().execute(f"DROP TABLE {name}")
    conn.commit()
    conn.close()


def delete_voc(lang, id):
    conn = sqlite3.connect(databasename)
    conn.cursor().execute(f"""DELETE FROM {lang}
                            WHERE id = {id}""")
    conn.commit()
    conn.close()


def get_vocs(lang):
    """loads all vocabularys from a database

    Args:
        lang (String):name of table

    Returns:
        [list]: [list of tuples of all vocabulary]
    """
    conn = sqlite3.connect(databasename)
    cur = conn.cursor()

    cur.execute("SELECT  * FROM " + lang)
    rows = cur.fetchall()
    conn.commit()
    return rows


def add_voc(lang, voc1, voc2):
    conn = sqlite3.connect(databasename)
    cur = conn.cursor()
    lang1 = lang.split("_")[0]
    lang2 = lang.split("_")[1]
    print(f"INSERT INTO {lang} ( {lang1},{lang2}) VALUES ( '{voc1}','{voc2}')")
    try:
        cur.execute(f"INSERT INTO {lang} ( {lang1},{lang2}) VALUES ( '{voc1}','{voc2}')")
    except:
        create_table(lang)
        cur.execute(f"INSERT INTO {lang} ( {lang1},{lang2}) VALUES ( '{voc1}','{voc2}')")
    conn.commit()
    conn.close()


if __name__ == "__main__":
    add_voc("german_englisch", "ich","I")