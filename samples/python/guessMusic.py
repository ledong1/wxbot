#猜歌游戏

from wechat import WeChatManager, MessageType

wechat_manager = WeChatManager(libs_path='../../libs')
import json

def sentVoice(client_id, chatRoom, file, id):
    wechat_manager.send_video(client_id, chatRoom, file)
