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
