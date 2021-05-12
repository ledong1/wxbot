# coding:utf-8
import random


def weight_choice(list, weight):

    new_list = []
    for i, val in enumerate(list):
        new_list.extend(val * weight[i])
    return random.choice(new_list)


if __name__ == "__main__":
    gift_dict = {
        10001: ["\uff1a\ud83d\udca3\u70b8\u5f39", -1000, 10000],  # 炸弹
        10002: ["\u26b0\u68fa\u6750", -500, 5000],  # 棺材
        10003: ["\ud83d\udd4a\u9e3d\u5b50", -500, 5000],  # 鸽子
        10004: ["\ud83d\udca9\u5927\u4fbf", -100, 1000],  # 大便
        10005: ["\ud83d\udd2a\u5200\u7247", -50, 500],  # 刀片
        10006: ["\ud83c\udf5a\u4e0b\u996d", -20, 200],  # 下饭
        10007: ["\u2b55\u53e3\u7403", -10, 100],  # 口球
        10008: ["\ud83c\udf6c\u7cd6\u679c", 1, 10],  # 糖果
        10009: ["\ud83c\udf70\u86cb\u7cd5", 5, 50],  # 蛋糕
        10010: ["\ud83e\uddf8\u5c0f\u718a", 10, 100],  # 小熊
        10011: ["\ud83e\udd5a\u8df3\u86cb", 20, 200],  # 跳蛋
        10012: ["\ud83d\udc59\u5185\u8863", 20, 200],  # 内衣
        10013: ["\ud83d\udc57\u5973\u88c5", 100, 1000],  # 女装
        10014: ["\ud83e\udddc\ud83c\udffb\u200d\u2640\ufe0f\u624b\u529e", 200, 2000],  # 手办
        10015: ["\ud83d\udc84\u53e3\u7ea2", 300, 3000],  # 口红
        10016: ["\u2328\ufe0f\u952e\u76d8", 500, 5000],  # 键盘
        10017: ["\ud83c\udfa7\u8033\u673a", 800, 8000],  # 耳机
        10018: ["\ud83d\udc8d\u94bb\u6212", 1000, 10000],  # 钻戒
        10019: ["\ud83d\udcbe\u663e\u5361", 3000, 30000],  # 显卡
        10020: ["\ud83c\udf20\u6d41\u661f\u96e8", 5000, 50000],  # 流星雨
        10021: ["\ud83c\udf38\u5341\u91cc\u6843\u82b1\u6797", 9999, 99999],  # 十里桃花

    }

    toname = "abc@123#10000,1"  # abc@hello#10001,1
    value = toname[toname.index("#") + 1:]

    myList = value.split(",")

    print(myList[1])