import mysql.connector
from mysql.connector import Error
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        if connection.is_connected():
            print("Successfully connected to the database")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def get_user_by_login(login):
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM uzytkownik WHERE login = %s", (login,))
    user = cursor.fetchone()
    cursor.close()
    connection.close()
    print(f"User found: {user}")
    return user

def check_if_is_any_user():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM uzytkownik")
    users = cursor.fetchall()
    if len(users) > 0:
        rodzaj_konta = 0
    else:
        rodzaj_konta = 1

    return rodzaj_konta

def register_user_database(login, haslo):
    connection = create_connection()
    cursor = connection.cursor()
    if(check_if_is_any_user()):
        cursor.execute("INSERT INTO uzytkownik (login, haslo, rodzaj_konta) VALUES (%s, %s, %s)",
                       (login, haslo, 1))
    else:
        cursor.execute("INSERT INTO uzytkownik (login, haslo, rodzaj_konta) VALUES (%s, %s, %s)",
                       (login, haslo, 0))

    connection.commit()
    cursor.close()
    connection.close()

def add_trening_database(serie_input, weight_input, repeats_input, time_input,cwiczenie_input, partia_input):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Element_Treningu (serie_plan, waga_plan, powtorzenia_plan, czas) VALUES (%s, %s, %s, %s)",
                   (serie_input, weight_input, repeats_input, time_input))
    connection.commit()
    cursor.close()
    connection.close()
