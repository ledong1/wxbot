import json
from wechat import WeChatManager, MessageType

wechat_manager = WeChatManager(libs_path='../../libs')

# init the user info
chatRoom3 = '17888521126@chatroom'  # test group
chatRoom2 = '26095218987@chatroom'  # 老二测试
chatRoom1 = '27352618533@chatroom'  # mainceshi
submit = '../json/groupMembers.json'

load_dict = wechat_manager.get_chatroom_members(1, chatRoom1)

with open(submit, 'w') as f:
    json.dump(load_dict, f)
