import pymysql
from auth import myDataBase, mySQLServer, user, passwodr

try:
    connection = pymysql.connect(host = mySQLServer,port = 3306,database = myDataBase,user = user,password = passwodr,cursorclass = pymysql.cursors.DictCursor)
    print('Мы смогли подключиться к базе данных')
    while True:
        go = int(input('Что бы вы хотели сделать с вашими заметками?\n1-Посмотреть все заметки\n2-Удалить заметку\n3-Изменить заметку\n4-Создать заметку\n'))

        if go == 1:
            with connection.cursor() as cursor:
                select_name_grup = "SELECT id('Номер заметки'), data, name FROM Zametki;"
                cursor.execute(select_name_grup)
                rows = cursor.fetchall()
                for i in rows:
                    print(i)
        
        if go == 4:
            with connection.cursor() as cursor:
                select_name_grup = "SELECT id, data, name FROM Zametki;"
                cursor.execute(select_name_grup)
                rows = cursor.fetchall()
                for i in rows:
                    print(i)


except Exception as ex:
    print('Connection refused')
    print('ex')