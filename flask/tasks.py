import json

class ToDo():
    def __init__(self):
        pass

    def add_task(self, task_name, task_date, username):
        f = open(f"users/tasks_{username}.json", "r")
        data = json.load(f)
        data[task_name] = task_date
        print(data)
        data1 = json.dumps(data)
        f.close()
        f = open(f"users/tasks_{username}.json", "w")
        f.write(data1)

    def fetch_task(self, username):
        f = open(f"users/tasks_{username}.json", "r")
        data = json.load(f)
        return data

    def delete_task(self, task_name, username):
        data = self.fetch_task(username)
        task_names = []
        for a in data:
            if task_name in a:
                task_name = a
        data = dict(data)
        print(task_name)
        data.pop(task_name)
        data_w = json.dumps(data)
        f = open(f"users/tasks_{username}.json", "w")
        f.write(data_w)

    def fetch_homework(self, username):
        f = open(f"users/homework_{username}.json", "r")
        data = json.load(f)
        return data

    def add_homework(self, name, subject, when, username):
        data = self.fetch_homework(username)
        data[name] = [subject, when]
        data1 = json.dumps(data)
        f = open(f"users/homework_{username}.json", "w")
        f.write(data1)

    def delete_homework(self, homework_name, username):
        data = self.fetch_homework(username)
        homework_names = []
        for a in data:
            if homework_name in a:
                homework_name = a
        data = dict(data)
        data.pop(homework_name)
        data_w = json.dumps(data)
        f = open(f"users/homework_{username}.json", "w")
        f.write(data_w)

    def fetch_notes(self, username):
        f = open(f"users/notes_{username}.json", "r")
        data = json.load(f)
        return data

    def add_note(self, name, username):
        data = self.fetch_notes(username)
        data[name] = "note content"
        data1 = json.dumps(data)
        f = open(f"users/notes_{username}.json", "w")
        f.write(data1)

    def update_note(self, note_content, note_name, username):
        data = self.fetch_notes(username)
        #note_name.replace("%20", " ")
        data[note_name] = note_content
        data = json.dumps(data)
        f = open(f"users/notes_{username}.json", "w")
        f.write(data)

    def delete_note(self, id, username):
        data = self.fetch_notes(username)
        homework_names = []
        for a in data:
            if id in a:
                id = a
        data = dict(data)
        data.pop(id)
        data_w = json.dumps(data)
        f = open(f"users/notes_{username}.json", "w")
        f.write(data_w)
