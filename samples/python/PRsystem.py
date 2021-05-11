# 人品系统
import json
from wechat import WeChatManager, MessageType

wechat_manager = WeChatManager(libs_path='../../libs')


def addRP(amount, id):
    submit = '../json/RP.json'
    with open(submit, 'r') as r:

        # 数据格式： {id:[amount, times]}
        load_dict = json.load(r)
        if id in load_dict:
            load_dict[id][0] += amount

        else:
            load_dict[id][0] = 50 + amount

    with open(submit, 'w') as f:
        json.dump(load_dict, f)


def minsRP(amount, id):
    submit = '../json/RP.json'
    with open(submit, 'r') as r:

        # 数据格式： {id:[amount, times]}
        load_dict = json.load(r)
        if id in load_dict:
            load_dict[id][0] -= amount

        else:
            load_dict[id] = [50,0]

    with open(submit, 'w') as f:
        json.dump(load_dict, f)


def showRP(client_id, chatRoom, id):
    # 查询RP额度

    submit = '../json/goldSystem.json'
    with open(submit, 'r') as r:
        # 数据格式： {id:amount}
        load_dict = json.load(r)
        if id in load_dict:
            wechat_manager.send_chatroom_at_msg(client_id, chatRoom,
                                                "\ud83d\udcb5{$@}您的RP余额为：" + str(load_dict[id][0]),
                                                [id])
        else:
            load_dict[id] = [50,0]
            wechat_manager.send_chatroom_at_msg(client_id, chatRoom,
                                                "\ud83d\udcb5{$@}您的RP余额为：50, 要好好做人哟",
                                                [id])

    with open(submit, 'w') as f:
        json.dump(load_dict, f)
