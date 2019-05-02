import json


class Settings:
    def __init__(self):
        with open('settings.json') as json_file:
            self.settings = json.load(json_file)

    def getSetting(self, key):
        return self.settings[key]



def setSettings(key, value, secondKey=False):
    settings = getSettings()
    if secondKey:
        settings[key][secondKey] = value
    else:
        settings[key] = value
    with open('settings.json', 'w') as json_file:
        json_file.write(json.dumps(settings))


def getSettings():
    with open('settings.json') as json_file:
        settings = json.load(json_file)
    return settings





def getSetting(key):
    with open('settings.json') as json_file:
        settings = json.load(json_file)
    return settings[key]        

