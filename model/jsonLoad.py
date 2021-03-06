from pathlib import Path
import json


def preetyPrintJson(jsonString):
   print(json.dumps(jsonString, indent=4, sort_keys=True))


def import_json(file):
    """"
    function gating json file location and return array
    @:return array
    """
    my_file = Path(file)
    if my_file.is_file():
        data = json.load(open(file))
        return data
    else:
        print("json file or directory doesnt exist")
