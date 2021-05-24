import os.path
import json
def read_students():
    if os.path.isfile('json/students.json'):
        with open('json/students.json') as json_file:
            data=json.load(json_file)
        return data
    else:
        return 0

def read_questions():
    if os.path.isfile('json/questions.json'):
        with open('json/questions.json') as json_file:
            data=json.load(json_file)
        return data
    else :
        return 0

def write_questions(data):
        with open('json/questions.json','w') as json_file:
            json.dump(data,json_file)

def write_students(data):
        with open('json/students.json','w') as json_file:
            json.dump(data,json_file)
