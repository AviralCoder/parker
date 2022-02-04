import json

def loadData(path: str) -> dict:
    file = open(path)
    data = json.load(file)
    file.close()
    return data