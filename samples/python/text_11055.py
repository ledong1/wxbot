# 猜歌系统
import json
from wechat import WeChatManager, MessageType

wechat_manager = WeChatManager(libs_path='../../libs')

def openSystem():
    submit = '../json/guessMusic.json'
    load_dict = {"GUESSMUSIC": ["start"], "ANSWER":[]}

    with open(submit, 'w') as w:
        json.dump(load_dict, w)


def closeSystem():
    submit = '../json/guessMusic.json'
    load_dict = {"GUESSMUSIC": [], "ANSWER":[]}
    with open(submit, 'w') as w:
        json.dump(load_dict, w)


def checkSystem():
    submit = '../json/guessMusic.json'
    with open(submit, 'r') as r:
        load_dict = json.load(r)
        if len(load_dict["GUESSMUSIC"]) > 0:
            return True
        else:
            return False

def addInfo(data):
    submit = '../json/guessMusic.json'
    if "~" in data:
        with open(submit, 'r') as r:
            load_dict = json.load(r)
            load_dict["GUESSMUSIC"].append(data)

        with open(submit, 'w') as w:
            json.dump(load_dict, w)

def addAnswer(data):
    print(data)
    submit = '../json/guessMusic.json'
    with open(submit, 'r') as r:
        load_dict = json.load(r)
        for x in data:
            load_dict["ANSWER"].append(x)

    with open(submit, 'w') as w:
        json.dump(load_dict, w)

# the answer
def checkAnswer(client_id, chatRoom, id, data):
    if "*" != data[0]:
        return False
    else:
        result = data.lstrip("*")
    submit = '../json/guessMusic.json'
    with open(submit, 'r') as r:
        load_dict = json.load(r)
        if "ANSWER" in load_dict:
            if result in load_dict["ANSWER"]:
                wechat_manager.send_chatroom_at_msg(client_id, chatRoom,
                                                    "{$@}你猜对啦! 获得金币10000!",
                                                    [id])
                closeSystem()
            else:
                wechat_manager.send_chatroom_at_msg(client_id, chatRoom,
                                                    "{$@}你猜错了! 再来一次吧!",
                                                    [id])

                staySystem()

def staySystem():
    submit = '../json/guessMusic.json'
    with open(submit, 'r') as r:
        load_dict = json.load(r)
    with open(submit, 'w') as w:
        json.dump(load_dict, w)