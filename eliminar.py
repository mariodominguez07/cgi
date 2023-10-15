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
    con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='foro')
    cursor = con.cursor()
    #sql = "DELETE from users WHERE email='{}'".format(e)
    sql = f"DELETE from users WHERE email='{e}'"
    cursor.execute(sql)
    con.commit()
    con.close()
    print("<h1>Usuario Eliminado</h1>")
else:
    print("<h1>Método no permitido</h1>")