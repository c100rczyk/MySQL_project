import mysql.connector
class LoginProcess:
    def __init__(self, mycoursor):
        self.mycoursor = mycoursor
        print(self.mycoursor)
    def login_to_app(self,input_login, putted_password):
        self.input_login = input_login
        self.putted_password = putted_password

        self.mycoursor.execute("SELECT haslo FROM uzytkownik WHERE login = %s", (self.input_login,))

        self.myresult = self.mycoursor.fetchone()[0]
        print(f"haslo w bazie: {self.myresult}")

        if putted_password == self.myresult:
            print("Logged in successfully")
        else:
            print("Wrong password")

