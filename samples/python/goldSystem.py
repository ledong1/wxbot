# 金币系统
import random,userInformation

from wechat import WeChatManager, MessageType

wechat_manager = WeChatManager(libs_path='../../libs')
import json, functions, PRsystem,random


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

# 减少金币
def minsGold(amount, id):
    submit = '../json/goldSystem.json'
    with open(submit, 'r') as r:

        # 数据格式： {id:amount}
        load_dict = json.load(r)
        if id in load_dict:
            load_dict[id] -= amount

        else:
            load_dict[id] = 0 - amount

    with open(submit, 'w') as f:
        json.dump(load_dict, f)


# 查询金币额度
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
        nicknameList = []
        for x in load_dict:
            idList.append(x)
            amountList.append(load_dict[x])

        file1 = submit = '../json/groupMembers.json'
        with open(file1, 'r') as read:
            load_dict2 = json.load(read)
            for x in idList:
                if x in load_dict2:
                    nicknameList.append(load_dict2[x])


        if id in load_dict:
            counter = list(load_dict.keys()).index(id)

        if counter != -1:
            wechat_manager.send_chatroom_at_msg(client_id, chatRoom,
                                                "===\ud83d\udcb5金币排行\ud83d\udcb5===\n"
                                                "\ud83d\udcb5["+str(amountList[0])+"]" + nicknameList[0] + "\n"
                                                "\ud83d\udcb5["+str(amountList[1])+"]" + nicknameList[1] + "\n"
                                                "\ud83d\udcb5["+str(amountList[2])+"]" + nicknameList[2] + "\n"
                                                "\ud83d\udcb5["+str(amountList[3])+"]" + nicknameList[3] + "\n"
                                                "\ud83d\udcb5["+str(amountList[4])+"]"+ nicknameList[4] +
                                                "\n===============\n"                         
                                                "您当前排名为" + str(counter+1),[idList[0],idList[1],idList[2],idList[3],idList[4]])
        else:
            wechat_manager.send_chatroom_at_msg(client_id, chatRoom,"您还没有任何金币可以进行排名",[id])


# 打劫：有几率大失败-大成功 自己扣钱对面加钱
# 被抓大失败 自己扣钱1.5倍 对方加钱1.5倍
# 大成功 抢劫翻1.5倍 对面扣1.5倍
# 成功 抢劫1倍 对面加一倍
# 失败 自几扣钱1倍 对面加一倍
def rob(client_id, chatRoom, fromid, toid):
    toid = userInformation.switchNameToID(toid)

    infos = '../json/groupMembers.json'
    with open(infos, 'r') as t:
        myInfoDict = json.load(t)
        if toid in myInfoDict:
            toName = myInfoDict[toid]
        else:
            return None

    amount = random.randint(1,99999)
    submit = '../json/goldSystem.json'
    rpFile = '../json/RP.json'
    p2 = 45
    p3 = 45
    # RP 提取
    with open(rpFile, 'r') as f:
        load_dict = json.load(f)
        if fromid in load_dict:
            p2 = 90 * load_dict[fromid][0]
            p3 = 90 * (1-load_dict[fromid][0])
            load_dict[fromid][1] += 1
        else:
            load_dict[fromid] = [50,0]



    # RP扣除在打劫之后
    PRsystem.minsRP(5, fromid)

    result = ["S","A","F","Z"]
    rate = [5,p2,p3,5]
    # 得出成功概率
    obj = functions.randomExm(result, rate)

    # 打开金币系统
    with open(submit, 'r') as r:
        load_dict = json.load(r)
        if fromid in load_dict:
            if obj == "S":
                wechat_manager.send_chatroom_at_msg(client_id, chatRoom, "{$@}大成功！获得抢劫金额1.5倍加成！"
                                                                         "本次抢劫获得\ud83d\udcb5 "+str(amount)+"*1.5 ["+str(amount*1.5)+"]金币\n"
                                                                        "对方失去\ud83d\udcb5 "+str(amount)+"*1.5 ["+str(amount*1.5)+"]金币",[fromid])
                addGold(amount*1.5, fromid)
                minsGold(amount*1.5, toName)

            elif obj == "A":
                wechat_manager.send_chatroom_at_msg(client_id, chatRoom, "{$@}成功！本次抢劫获得\ud83d\udcb5 ["+str(amount)+"]\n"
                                                                         "对方失去\ud83d\udcb5 ["+str(amount)+"]金币", [fromid])
                addGold(amount, fromid)
                minsGold(amount, toName)

            # elif obj == "F":
            #
            # elif obj == "Z":

            else:
                wechat_manager.send_chatroom_at_msg(client_id, chatRoom, "测试版本无法失败", [fromid])

# 返回用户金额额度， 后台使用
def getGoldAmount(id):
    submit = '../json/goldSystem.json'

    with open(submit, 'r') as r:
        # 数据格式： {id:amount}
        load_dict = json.load(r)
        if id in load_dict:
            amount = load_dict[id]

        else:
            load_dict[id] = 0
            amount = 0

    with open(submit, 'w') as f:
        json.dump(load_dict, f)

    return amount

