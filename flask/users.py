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
        for a in data:
            if a == login:
                return "account with that username already exists"
        data[login] = password
        f = open("assets/accounts.json", "w")
        data = json.dumps(data)
        f.write(data)
        f = open("users/tasks_" + str(login) + ".json", "w")
        data1 = {}
        data1 = json.dumps(data1)
        f.write(data1)
        f.close()
        f = open("users/homework_" + str(login) + ".json", "w")
        data2 = {}
        data2 = json.dumps(data2)
        f.write(data2)
        f.close()
        f = open("users/notes_" + str(login) + ".json", "w")
        data3 = {}
        data3 = json.dumps(data3)
        f.write(data3)
        f.close()
        return "done"

    def fetch_login_file(self):
        f = open("assets/accounts.json", "r")
        data = json.load(f)
        return data


