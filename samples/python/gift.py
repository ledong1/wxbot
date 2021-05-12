# 礼物系统
import json,goldSystem,userInformation,PRsystem
from wechat import WeChatManager, MessageType

wechat_manager = WeChatManager(libs_path='../../libs')


gift_dict = {
    "炸弹": ["\uff1a\ud83d\udca3\u70b8\u5f39",-1000, 10000],  #炸弹
    "棺材": ["\u26b0\u68fa\u6750",-500, 5000], #棺材
    "鸽子": ["\ud83d\udd4a\u9e3d\u5b50",-500, 5000],  #鸽子
    "大便": ["\ud83d\udca9\u5927\u4fbf",-100,1000], # 大便
    "刀片": ["\ud83d\udd2a\u5200\u7247",-50,500], #刀片
    "下饭": ["\ud83c\udf5a\u4e0b\u996d",-20,200], #下饭
    "口球": ["\u2b55\u53e3\u7403",-10,100], #口球
    "糖果": ["\ud83c\udf6c\u7cd6\u679c",1,10] ,#糖果
    "蛋糕": ["\ud83c\udf70\u86cb\u7cd5",5,50], #蛋糕
    "小熊": ["\ud83e\uddf8\u5c0f\u718a", 10, 100],  #小熊
    "跳蛋": ["\ud83e\udd5a\u8df3\u86cb",20,200], #跳蛋
    "内衣": ["\ud83d\udc59\u5185\u8863", 20, 200],  #内衣
    "女装": ["\ud83d\udc57\u5973\u88c5",100,1000], #女装
    "手办": ["\ud83e\udddc\ud83c\udffb\u200d\u2640\ufe0f\u624b\u529e",200,2000], #手办
    "口红": ["\ud83d\udc84\u53e3\u7ea2",300,3000], #口红
    "键盘": ["\u2328\ufe0f\u952e\u76d8",500,5000], #键盘
    "耳机": ["\ud83c\udfa7\u8033\u673a",800,8000], #耳机
    "钻戒": ["\ud83d\udc8d\u94bb\u6212",1000,10000], #钻戒
    "显卡": ["\ud83d\udcbe\u663e\u5361",3000,30000], #显卡
    "流星雨": ["\ud83c\udf20\u6d41\u661f\u96e8",5000,50000], #流星雨
    "十里桃花": ["\ud83c\udf38\u5341\u91cc\u6843\u82b1\u6797",9999,99999], #十里桃花

}

# 赠送礼物
def sendGift(client_id, chatRoom, fromid, toname, giftID, amount=1):
    submit = "../json/gift.json"
    # {"userId":
    #       {"giftid": 0}
    # }

    toid = userInformation.switchNameToID(toname)


    with open(submit, "r") as f:
        load_dict = json.load(f)
        # 用户不存在礼物列表
        if fromid not in load_dict:
            # 购买礼物
            result = buyGift(client_id, chatRoom, fromid, giftID, amount)
            # wechat_manager.send_chatroom_at_msg(client_id, chatRoom,
            #                                      "passed",[fromid])
            # 购买成功
            if result == 1:
                # 收到礼物
                getGift(client_id,chatRoom,toid,giftID,amount)
                # 甲方礼物减少
                amountMins(fromid, giftID, amount)
                wechat_manager.send_chatroom_at_msg(client_id,chatRoom, "{$@} 您成功赠送了:\n["+toname+"] "+gift_dict[giftID][0]+"*"+str(amount)
                                                    +"\n对方RP获得:"+str(gift_dict[giftID][1]*amount),[fromid])



        # 用户存在礼物列表
        else:
            if giftID in load_dict[fromid]:

                # 库存足够
                if load_dict[fromid][giftID] >= amount:
                    load_dict[fromid][giftID] -= amount
                    getGift(client_id, chatRoom, toid, giftID, amount)
                    amountMins(fromid, giftID, amount)
                    wechat_manager.send_chatroom_at_msg(client_id, chatRoom,
                                                        "{$@} 您成功赠送了:\n[" + toname + "] " + gift_dict[giftID][
                                                            0] + "*" + str(amount)
                                                        + "\n对方RP获得:" + str(gift_dict[giftID][1] * amount), [fromid])
                else:
                    # 购买礼物
                    result = buyGift(client_id, chatRoom, fromid, giftID, amount)
                    # 购买成功
                    if result == 1:
                        getGift(client_id, chatRoom, toid, giftID, amount)
                        amountMins(fromid, giftID, amount)
                        wechat_manager.send_chatroom_at_msg(client_id, chatRoom,
                                                            "{$@} 您成功赠送了:\n[" + toname + "] " + gift_dict[giftID][
                                                                0] + "*" + str(amount)
                                                            + "\n对方RP获得:" + str(gift_dict[giftID][1] * amount),
                                                            [fromid])
    with open(submit, "w") as write:
        json.dump(load_dict, write)


# 购买礼物
# 1 = 成功
# 0 = 失败
def buyGift(client_id, chatRoom, id, giftId, amount=1):

    money = gift_dict[giftId][2] * int(amount)
    balance = goldSystem.getGoldAmount(id)

    if int(balance) < int(money):
        wechat_manager.send_chatroom_at_msg(client_id, chatRoom, "{$@}余额不足, 无法购买...",[id])
        return 0
    else:
        amountAdd(id, giftId,amount)
        goldSystem.minsGold(money,id)
        return 1

# 收到礼物
def getGift(client_id, chatRoom, id, giftID, amount):
    amountAdd(id, giftID, amount)
    PRsystem.addRP(gift_dict[giftID][1]*amount,id)


# 返回库存列表， 后台使用
def returnGiftDict(id):
    submit = "../json/gift.json"
    with open(submit, 'r') as r:
        load_dict = json.load(r)
        if id in load_dict:
            return load_dict[id]

# 填充dict
def fillTheDict(dict):
    return dict


# 查询库存
def showGift(client_id, chatRoom, id):
    submit = "../json/gift.json"
    with open(submit, 'r') as r:
        load_dict = json.load(r)
        if id not in load_dict:
            load_dict[id] = {}
            wechat_manager.send_chatroom_at_msg(client_id, chatRoom, "{$@}您没有任何礼物库存了！快去赚钱买礼物~",[id])
        else:
            myDict = returnGiftDict(id)

# 库存增加
def amountAdd(id, giftid, amount):
    submit = "../json/gift.json"
    with open(submit, 'r') as r:
        # {"userId":
        #       {"giftid": 0}
        # }
        load_dict = json.load(r)
        # 第一次访问库存
        if id not in load_dict:
            load_dict[id] = {giftid: amount}

        else:
            load_dict[id][giftid] += amount

    with open(submit, "w") as w:
        json.dump(load_dict, w)

# 库存减少
def amountMins(id, giftid, amount):
    submit = "../json/gift.json"
    with open(submit, 'r') as r:
        # {"userId":
        #       {"giftid": 0}
        # }
        load_dict = json.load(r)
        # 第一次访问库存
        if id not in load_dict:
            load_dict[id] = {giftid: 0}

        else:
            load_dict[id][giftid] -= amount

    with open(submit, "w") as w:
        json.dump(load_dict, w)
