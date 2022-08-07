import json

class users():
    def __init__(self):
        pass

    def check_login(self, login, password):
        data = self.fetch_login_file()
        try:
            password_actual = data[login]
        except:
            return "Account doesnt exist!"
        if password == password_actual:
            return True
        else:
            return "Bad password"

    def create_account(self, login, password):
        data = self.fetch_login_file()
        data[login] = password
        f = open("assets/accounts.json", "w")
        data = json.dumps(data)
        f.write(data)
        return "done"

    def fetch_login_file(self):
        f = open("assets/accounts.json", "r")
        data = json.load(f)
        return data


