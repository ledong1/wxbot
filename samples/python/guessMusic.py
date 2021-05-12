#猜歌游戏

from wechat import WeChatManager, MessageType

wechat_manager = WeChatManager(libs_path='../../libs')
import json,random,os,os.path

hvSize={'巫毒师 巴蒂斯特': 15, '盲豹 格雷': 6,'鹰眼 凯思卓': 6,'天使 奥达基': 14,'机械战姬 阿尔法': 15,'刀锋魅影 安卡': 15,'护卫 亚丹': 8}
hNickname={'巫毒师 巴蒂斯特': ['巴蒂斯特','巴蒂'], '盲豹 格雷': ['盲豹', '格雷'],'鹰眼 凯思卓': ['鹰眼', '凯思卓'],'天使 奥达基': ['天使', '奥达基', '鸟人'],'机械战姬 阿尔法': ['机械战姬', '阿尔法'],'刀锋魅影 安卡': ['刀锋魅影', '安卡'],'护卫 亚丹': ['亚丹','亚当','二蛋']}

def guessHero():
    currentHero = random.choice(list(hNickname.keys()))

    fileAddress = '../herovoice/{}/{}'.format(currentHero, random.choice(
        list(os.listdir('../herovoice/{}'.format(currentHero)))))
    # print(fileAddress, hNickname[currentHero])
    # hNickname[currentHero]
    addr = os.getcwd()  # 获取当前路径

    # print(addr.rstrip("\python")+fileAddress.lstrip("..").replace("/", "\\"))
    # addr = os.path.join(addr,fileAddress.lstrip(".."))
    # path += fileAddress.lstrip("..")
    # path.replace("\\", '/')
    result = addr.rstrip("\python")+fileAddress.lstrip("..").replace("/", "\\")

    return result, hNickname[currentHero]

#
# def sentVoice(client_id, chatRoom, file, id):
#     wechat_manager.send_video(client_id, chatRoom, file)
#     pass

guessHero()