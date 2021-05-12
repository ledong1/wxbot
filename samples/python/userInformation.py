#初始和修改用户信息
import json


def initInfo(msg):
    submit = '../json/groupMembers.json'
    load_dict = {}
    for x in msg:
        print()
        load_dict[x["wxid"]] = x["nickname"]

    with open(submit, 'w') as f:
        json.dump(load_dict, f)


def switchNameToID(name):
    submit = "../json/groupMembers.json"
    with open(submit, 'r') as r:
        load_dict = json.load(r)
        return (list(load_dict.keys())[list(load_dict.values()).index(name)])

