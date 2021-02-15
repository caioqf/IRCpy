import mysql.connector
import _md5
import sys

sys.path.insert(0, '/the/folder/path/name-package/')

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='test'
)
mycursor = mydb.cursor(buffered=True)


def register_user(usr, psw):
    sql = "INSERT INTO irc_logins (usr, psw) VALUES (%s, %s)"

    val = (usr, psw)
    mycursor.execute(sql, val)
    mydb.commit()
    print()


def check_user(user_to_check):
    sql = "SELECT EXISTS(SELECT * FROM irc_logins WHERE usr = '%s')" % (user_to_check)
    mycursor.execute(sql)
    mydb.commit()
    result = mycursor.fetchall()
    exist = True
    if result[0][0]:
        exist = True
    else:
        exist = False
    return exist


def check_pass(user, pass_to_check):
    sql = "SELECT psw FROM irc_logins WHERE psw = '%s'" % (pass_to_check)
    mycursor.execute(sql)
    mydb.commit()

    result = mycursor.fetchall()

    if not result:
        print(f'nao existe usuário {user} com senha {pass_to_check}')
        logged = False
    else:
        print('logou')
        logged = True
    return logged


check_pass('caio', 123)

