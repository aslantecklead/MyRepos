import pyodbc

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-K84V7A9L\MYSQLSERVER;DATABASE=Pilaf;Trusted_Connection=yes;')

cursor=connection.cursor()
cursor.execute("SELECT @@VERSION as version")

def AdminEnter(login, password):
    cursor.execute("SELECT * FROM [dbo].[Buyer]")
    for row in cursor.fetchall():
        print(row)


print(" 'Шаурма - и точка'/n Авторизация ")
login = input(" Введите логин: ")
password = input("Введите пароль: ")
AdminEnter(login, password)