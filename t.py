import csv, sqlite3

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("CREATE TABLE t (id,book_id,isbn,authors,publication_year,title,language_code,average_rating,genre);") # use your column names here

with open('output.csv','rb') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['col1'], i['col2']) for i in dr]

cur.executemany("INSERT INTO t (id,book_id,isbn,authors,publication_year,title,language_code,average_rating,genre) VALUES (?, ?,?, ?,?, ?,?, ?,?);", to_db)
con.commit()
con.close()