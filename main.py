import pymysql
from auth import myDataBase, mySQLServer, user, passwodr
import sys
import re

try:
    connection = pymysql.connect(host = mySQLServer,port = 3306,database = myDataBase,user = user,password = passwodr,cursorclass = pymysql.cursors.DictCursor)
    print('Мы смогли подключиться к базе данных')
    while True:
        go = int(input('Что бы вы хотели сделать с вашими заметками?\n1-Посмотреть все заметки\n2-Удалить заметку\n3-Изменить заметку\n4-Создать заметку\n5-Поиск по дате\n6-Выйти\n'))

        if go == 1:
            with connection.cursor() as cursor:
                select_name_grup = "SELECT id 'Номер заметки', data 'Дата заметки', name 'Заметка' DATE_FORMAT(data, '%d.%m.%Y') FROM Zametki;"
                cursor.execute(select_name_grup)
                rows = cursor.fetchall()
                for i in rows:
                    print(i)
                print('\n')
        
        if go == 2:
            delete=int(input('Номер заметки которую вы хотите удалить: '))
            with connection.cursor() as cursor:
                select_name_grup = f"DELETE FROM Zametki WHERE id = {delete};"
                cursor.execute(select_name_grup)
                rows = cursor.fetchall()
                print('Ваша запись удалена\n')
                
        if go == 3:
            izmena=int(input('Введите номер заметки которую хотите изменить: '))
            nameizmen=input('Введите новую заметку: ')
            with connection.cursor() as cursor:
                select_name_grup = f"UPDATE Zametki SET name = '{nameizmen}' WHERE id = {izmena};"
                cursor.execute(select_name_grup)
                rows = cursor.fetchall()
                print('Ваша запись изменена\n')

        if go == 4:
            datamet=(input('Напишите пожалуйста дату заметки через точку (Формат записи 2023.12.01): '))
            namezamtki=(input('Напишите пожалуйста вашу заметку: '))
            with connection.cursor() as cursor:
                select_name_grup = f"INSERT INTO Zametki (data, name) VALUES ('{datamet}', '{namezamtki}');"
                cursor.execute(select_name_grup)
                rows = cursor.fetchall()
                print('Ваша запись добавлена\n')
        
        if go == 5:
            datapoisk=(input('Напишите пожалуйста дату заметки через точку (Формат записи 2023.12.01): '))
            chars = '.,!/'
            datapoisk1=datapoisk.translate(str.maketrans('', '', chars))
            print(int(datapoisk1))
            with connection.cursor() as cursor:
                select_name_grup = f"SELECT id 'Номер заметки', data 'Дата заметки', name 'Заметка' FROM Zametki WHERE `data`={datapoisk1};"
                cursor.execute(select_name_grup)
                rows = cursor.fetchall()
                for i in rows:
                    print(i)
                
        if go == 6:
            sys.exit()

except Exception as ex:
    print('Connection refused')
    print('ex')