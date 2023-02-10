import pymysql
from auth import myDataBase, mySQLServer, user, passwodr

try:
    connection = pymysql.connect(host = mySQLServer,port = 3306,database = myDataBase,user = user,password = passwodr,cursorclass = pymysql.cursors.DictCursor)
    print('Мы смогли подключиться к базе данных')
    while True:
        go = int(input('Что бы вы хотели сделать с вашими заметками?\n1-Посмотреть все заметки\n2-Удалить заметку\n3-Изменить заметку\n4-Создать заметку\n'))

        if go == 1:
            with connection.cursor() as cursor:
                select_name_grup = "SELECT id 'Номер заметки', data 'Дата заметки', name 'Послание' FROM Zametki;"
                cursor.execute(select_name_grup)
                rows = cursor.fetchall()
                for i in rows:
                    print(i)
                print('\n')
        
        if go == 2:
            delete=int(input('Номер заметки которую вы хотите удалить'))
            with connection.cursor() as cursor:
                select_name_grup = f"DELETE FROM Zametki WHERE id = {delete};"
                cursor.execute(select_name_grup)
                rows = cursor.fetchall()
                print('Ваша запись удалена\n')

        if go == 4:
            datamet=(input('Напишите пожалуйста дату заметки через точку'))
            namezamtki=(input('Напишите пожалуйста вашу заметку'))
            with connection.cursor() as cursor:
                select_name_grup = f"ЗАПРОС"
                cursor.execute(select_name_grup)
                rows = cursor.fetchall()
                print('Ваша запись добавлена\n')

except Exception as ex:
    print('Connection refused')
    print('ex')