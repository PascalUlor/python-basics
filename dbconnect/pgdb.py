import psycopg2

def create_table():
    conn=psycopg2.connect("dbname='db1' user='postgres' password='pculor' port='5432' host='localhost'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    # cur.execute("INSERT INTO store VALUES ('Wine Glass', 8,10.5)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn=psycopg2.connect("dbname='db1' user='postgres' password='pculor' port='5432' host='localhost'")
    cur=conn.cursor()
    # cur.execute("INSERT INTO store VALUES ('%s','%s','%s')" % (item,quantity,price))
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)",(item,quantity,price))
    conn.commit()
    conn.close()


def view():
    conn=psycopg2.connect("dbname='db1' user='postgres' password='pculor' port='5432' host='localhost'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn=psycopg2.connect("dbname='db1' user='postgres' password='pculor' port='5432' host='localhost'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn=psycopg2.connect("dbname='db1' user='postgres' password='pculor' port='5432' host='localhost'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity,price,item))
    conn.commit()
    conn.close()


create_table()
insert('Grapes',12,12)
delete('Grapes')
update(55,100,'Apple')
print(view())
    #
    # delete("Coffee cup")
    # update(200,500,"Wine Glass")
    # insert("PC",10,5.4)
    #
    # print(view())
