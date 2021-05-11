#猜歌游戏

from wechat import WeChatManager, MessageType

wechat_manager = WeChatManager(libs_path='../../libs')
import json

hvSize={'巫毒师 巴蒂斯特': 15, '盲豹 格雷': 6,'鹰眼 凯思卓': 6,'天使 奥达基': 14,'机械战姬 阿尔法': 15,'刀锋魅影 安卡': 15,'护卫 亚丹': 8}
hNickname={'巫毒师 巴蒂斯特': ['巴蒂斯特','巴蒂'], '盲豹 格雷': 6,'鹰眼 凯思卓': 6,'天使 奥达基': 14,'机械战姬 阿尔法': 15,'刀锋魅影 安卡': 15,'护卫 亚丹': 8}

def guessHero(client_id, chatRoom):


def sentVoice(client_id, chatRoom, file, id):
    wechat_manager.send_video(client_id, chatRoom, file)
