# 金币系统

from wechat import WeChatManager, MessageType

wechat_manager = WeChatManager(libs_path='../../libs')
import json


# 添加金币
def addGold(amount, id):
    submit = '../json/goldSystem.json'
    with open(submit, 'r') as r:

        # 数据格式： {id:amount}
        load_dict = json.load(r)
        if id in load_dict:
            load_dict[id] += amount

        else:
            load_dict[id] = amount

    with open(submit, 'w') as f:
        json.dump(load_dict, f)


# 查询金币排行
def showGold(client_id, chatRoom, id):
    submit = '../json/goldSystem.json'
    with open(submit, 'r') as r:
        # 数据格式： {id:amount}
        load_dict = json.load(r)
        if id in load_dict:
            wechat_manager.send_chatroom_at_msg(client_id, chatRoom,
                                                "\ud83d\udcb5{$@}您的金币余额为：" + str(load_dict[id]),
                                                [id])
        else:
            load_dict[id] = 0
            wechat_manager.send_chatroom_at_msg(client_id, chatRoom,
                                                "\ud83d\udcb5{$@}您的金币余额为：0, 重新白手起家吧",
                                                [id])

    with open(submit, 'w') as f:
        json.dump(load_dict, f)


# 查询金币排行
def showRank(client_id, chatRoom, id):
    submit = '../json/goldSystem.json'

    with open(submit, 'r') as r:
        # 数据格式： {id:amount}
        load_dict = json.load(r)
        # value 排序
        load_dict = dict(sorted(load_dict.items(), key=lambda item: item[1], reverse=True))

        counter = -1
        idList = []
        amountList = []
        for x in load_dict:
            idList.append(x)
            amountList.append(load_dict[x])

        if id in load_dict:
            counter = list(load_dict.keys()).index(id)

        if counter != -1:
            wechat_manager.send_chatroom_at_msg(client_id, chatRoom,
                                                "===\ud83d\udcb5金币排行\ud83d\udcb5===\n"
                                                "\ud83d\udcb5["+str(amountList[0])+"]{$@}\n"
                                                "\ud83d\udcb5["+str(amountList[1])+"]{$@}\n"
                                                "\ud83d\udcb5["+str(amountList[2])+"]{$@}\n"
                                                "\ud83d\udcb5["+str(amountList[3])+"]{$@}\n"
                                                "\ud83d\udcb5["+str(amountList[4])+"]{$@}"
                                                "\n===============\n"                         
                                                "您当前排名为" + str(counter+1),[idList[0],idList[1],idList[2],idList[3],idList[4]])
        else:
            wechat_manager.send_chatroom_at_msg(client_id, chatRoom,"您还没有任何金币可以进行排名",[id])