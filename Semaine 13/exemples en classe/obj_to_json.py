import json


class ObjTest:

    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2


obj1 = ObjTest(1, "test")
dict_obj = {"val1": obj1.val1, "val2": obj1.val2}
with open("obj.json", mode="wt", encoding="utf8") as fichier_json:
    json.dump(dict_obj, fichier_json)



