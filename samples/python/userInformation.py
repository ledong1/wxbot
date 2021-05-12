#初始和修改用户信息
import json,goldSystem,PRsystem


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

def switchIdToName(id):
    submit = "../json/groupMembers.json"
    with open(submit, 'r') as r:
        load_dict = json.load(r)
        return load_dict[id]

class users():

    def __init__(self,userId):
        self.id = userId
        self.name = switchNameToID(userId)
        # init the info
        submit = "../json/userInfo.json"
        with open(submit, 'r') as r:
            load_dict = json.load(r)
            if userId not in load_dict:
                load_dict[id] = [self.name,self.getUserGod(userId),self.getUserRP(userId)]

        with open(submit, 'w') as w:
            json.dump(load_dict, w)


    # 获取用户金钱 后台
    def getUserGold(self, id):
        return goldSystem.getGoldAmount(id)

    # 获取用户RP 后台
    def getUserRP(self, id):
        return PRsystem.showRPBack(id)

    def addGold(self,amount,id):
        goldSystem.addGold(amount,id)
        self.updateStatus()


    def minsGold(self,amount,id):
        goldSystem.minsGold(amount,id)
        self.updateStatus()

    def addRP(self,amount,id):
        PRsystem.addRP(amount,id)
        self.updateStatus()

    def minsGold(self,amount, id):
        PRsystem.minsRP(amount, id)
        self.updateStatus()

    def updateStatus(self):
        submit = "../json/userInfo.json"
        with open(submit, 'r') as r:
            load_dict = json.load(r)
            load_dict[id] = [self.name, self.getUserGod(self.id), self.getUserRP(self.id)]

        with open(submit, 'w') as w:
            json.dump(load_dict, w)