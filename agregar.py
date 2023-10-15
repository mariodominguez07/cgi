#!C:/Python311/python.exe
import mysql.connector
import os
import cgi
import cgitb
cgitb.enable()
print("Content-type: text/html")
print()

metodo = os.environ["REQUEST_METHOD"]

if metodo == "POST":
    datos = cgi.FieldStorage()
    e = datos.getvalue("email")
    p = datos.getvalue("password")
    n = datos.getvalue("name")
    a = datos.getvalue("avatar")
    r = datos.getvalue("role")
    con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='foro')
    sql = "INSERT INTO users VALUES('{}',sha1('{}'),'{}','{}','{}')".format(e, p, n, a, r)
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    con.close()
    print("<h1>Usuario Agregado</h1>")
else:
    print("<h1>Método no permitido</h1>")