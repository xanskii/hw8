import sqlite3


conn = sqlite3.connect('hw__8')
cursor = conn.cursor()

while True:
    print('👉>>ДОБРО ПОЖАЛОВАТЬ<<👈')
    print('Начинаем')
    command = input('1) start\n'
                    '0) exit\n')
    if command == '1':
        print('continue')
    elif command == '0':
        print('stop')
        break
    else:
        print('!!ОШИБКА!!')
        break

    print("Вы можете отобразить список сотрудников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()
    for city in cities:
        print(city[0], city[1])
    city_id = int(input("id : "))
    if city_id == 0:
        print ('!!ОШИБКА!!')
        break
    else:

        cursor.execute('''SELECT  employees.first_name,  employees.lasr_name,  cities.title, countries.title
                          FROM employees 
                          INNER JOIN cities  ON  employees.city_id = cities.id
                          INNER JOIN countries  ON city.country_id = countryes.id
                          WHERE cities.id = ?''', (city_id,))
        employees = cursor.fetchall()
        if employees:
            for i  in employees:
                print("name ", i [0])
                print("surname", i [1])
                print("country",  i [2])
                print("live - city",  i [3])
                print()
        else:
            print()


conn.close()
