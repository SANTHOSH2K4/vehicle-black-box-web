import sqlite3
conn=sqlite3.connect('starcoders.db')
c=conn.cursor()
#c.execute("create table thing(thing text)")
#c.execute("insert into thing values('{}')".format("sos"))
#conn.commit()
li=c.execute("select thing from thing")
result=li.fetchone()[0]

print(result)
