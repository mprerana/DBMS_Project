from main1 import Database as db
import json


class Composing:
    def __init__(self):
        self.conn = db.getConnection()
        self.cursor = self.conn.cursor()

    
    def subject(self):
        self.cursor.execute('SELECT id, name, hours, code, description, instructors, divisible, type FROM subjects')
        subjects = self.ltod(self.cursor.fetchall())
        subjects = self.jsonToList(subjects, 4)
        subjects = self.convertor(subjects, 4)
        return subjects



    def room(self):
        self.cursor.execute('SELECT id, name, type, schedule FROM rooms WHERE active = 1')
        rooms = self.ltod(self.cursor.fetchall())
        rooms = self.jsonToList(rooms, 2)
        return rooms



    def getSharings(self):
        self.cursor.execute('SELECT id, subjectId, sections FROM sharings WHERE final = 1')
        sharings = self.ltod(self.cursor.fetchall())
        sharings = self.jsonToList(sharings, 1)
        sharings = self.convertor(sharings, 1)
        return sharings  


    def convertor(self, dictionary, index):
        for key, value in dictionary.items():
            dictionary[key][index] = list(map(int, value[index]))
        return dictionary      

    


    def instructor(self):
        self.cursor.execute('SELECT id, name, hours, schedule FROM instructors WHERE active = 1')
        instructors = self.ltod(self.cursor.fetchall())
        instructors = self.jsonToList(instructors, 2)
        return instructors


    def ltod(self, toDict):
        return {entry[0]: list(entry[1:]) for entry in toDict}    
    

    def getSections(self):
        self.cursor.execute('SELECT id, name, schedule, subjects, stay FROM sections WHERE active = 1')
        sections = self.ltod(self.cursor.fetchall())
        sections = self.jsonToList(sections, 1)
        sections = self.jsonToList(sections, 2)
        sections = self.convertor(sections, 2)
        return sections

    

    

    def jsonToList(self, dictionary, index):
        for key, value in dictionary.items():
            dictionary[key][index] = json.loads(value[index])
        return dictionary

    

    def closeConnection(self):
        self.conn.commit()
        self.conn.close()

    def getdata(self):
        data = {
            'instructors': self.instructor(),
            'sharings': self.getSharings(),
            'sections': self.getSections(),
            'subjects': self.subject(),
            'rooms': self.room()
        }
        self.closeConnection()
        return data
