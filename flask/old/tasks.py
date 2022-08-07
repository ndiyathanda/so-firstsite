import json

class ToDo():
    def __init__(self):
        pass

    def add_task(self, task_name, task_date):
        f = open("tasks.json", "r")
        data = json.load(f)
        data[task_name] = task_date
        print(data)
        data1 = json.dumps(data)
        f.close()
        f = open("tasks.json", "w")
        f.write(data1)

    def fetch_task(self):
        f = open("tasks.json", "r")
        data = json.load(f)
        return data

    def delete_task(self, task_name):
        data = self.fetch_task()
        task_names = []
        for a in data:
            if task_name in a:
                task_name = a
        data = dict(data)
        print(task_name)
        data.pop(task_name)
        data_w = json.dumps(data)
        f = open("tasks.json", "w")
        f.write(data_w)

    def fetch_homework(self):
        f = open("homework.json", "r")
        data = json.load(f)
        return data

    def add_homework(self, name, subject, when):
        data = self.fetch_homework()
        data[name] = [subject, when]
        data1 = json.dumps(data)
        f = open("homework.json", "w")
        f.write(data1)

    def delete_homework(self, homework_name):
        data = self.fetch_homework()
        homework_names = []
        for a in data:
            if homework_name in a:
                homework_name = a
        data = dict(data)
        data.pop(homework_name)
        data_w = json.dumps(data)
        f = open("homework.json", "w")
        f.write(data_w)

    def fetch_notes(self):
        f = open("notes.json", "r")
        data = json.load(f)
        return data

    def add_note(self, name):
        data = self.fetch_notes()
        data[name] = "note content"
        data1 = json.dumps(data)
        f = open("notes.json", "w")
        f.write(data1)

    def update_note(self, note_content, note_name):
        data = self.fetch_notes()
        #note_name.replace("%20", " ")
        data[note_name] = note_content
        data = json.dumps(data)
        f = open("notes.json", "w")
        f.write(data)

    def delete_note(self, id):
        data = self.fetch_notes()
        homework_names = []
        for a in data:
            if id in a:
                id = a
        data = dict(data)
        data.pop(id)
        data_w = json.dumps(data)
        f = open("notes.json", "w")
        f.write(data_w)
