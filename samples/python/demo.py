# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import datetime

import wechat
import json
import time
from wechat import WeChatManager, MessageType

wechat_manager = WeChatManager(libs_path='../../libs')


# 这里测试函数回调
@wechat.CONNECT_CALLBACK(in_class=False)
def on_connect(client_id):
    print('[on_connect] client_id: {0}'.format(client_id))


@wechat.RECV_CALLBACK(in_class=False)
def on_recv(client_id, message_type, message_data):
    print('[on_recv] client_id: {0}, message_type: {1}, message:{2}'.format(client_id,
                                                                            message_type, json.dumps(message_data)))


@wechat.CLOSE_CALLBACK(in_class=False)
def on_close(client_id):
    print('[on_close] client_id: {0}'.format(client_id))


# 这里测试类回调， 函数回调与类回调可以混合使用
class LoginTipBot(wechat.CallbackHandler):

    # 签到系统
    def signUp(self, client_id, chatRoom, id):
        nowDate = str(datetime.datetime.now())
        today = str(datetime.date.today())
        submit = './test.json'

        with open(submit, 'r') as r:
            # 全部的数据储存在同一dict中
            # 格式： [date1: [username1, username2]},
            #       {date2: [username1}]
            load_dict = json.load(r)

            # 时间为Key， 签到为value\
            # 如果已经有人签到
            if today in load_dict:
                if id not in load_dict[today]:
                    load_dict[today].append(id) # 添加用户到当前时间key
                    wechat_manager.send_chatroom_at_msg(client_id, chatRoom,
                                                        "\u2618\ufe0f{$@}\n\u2618\ufe0f签到成功！\n\u2618\ufe0f签到时间: " + nowDate + "\n\u2618\ufe0f今日排名: "+str(load_dict[today].index(id)+1)+" \n\u2618\ufe0f奖励: 100金币！",
                                                        [id])
                else:
                    wechat_manager.send_chatroom_at_msg(client_id, chatRoom,
                                                        "\u2618\ufe0f{$@}\n\u26a0\ufe0f您已经签到请勿重复签到！",
                                                        [id])

            # 无人签到
            else:
                load_dict[today] = [id]
                wechat_manager.send_chatroom_at_msg(client_id, chatRoom,
                                                    "\u2618\ufe0f{$@}\n\u2618\ufe0f签到成功！\n\u2618\ufe0f签到时间: " + nowDate + "\n\u2618\ufe0f今日排名: " +
                                                    str(load_dict[today].index(id)+1) + " \n\u2618\ufe0f奖励: 100金币！",
                                                    [id])



        with open(submit, 'w') as f:
            json.dump(load_dict, f)




    # 11046
    def inputText(self, client_id, message_data):
        menu = "======\u529f\u80fd\u83dc\u5355======\n\ud83c\udf40\u7b7e        \u5230\u2728\u4eba        \u54c1\ud83d\udc7b\n\ud83c\udf81\u793c        \u7269\u2728\u7ed3        \u5a5a\ud83c\udf8e\n\ud83c\udf29\u5929        \u6c14\u2728\u70b9        \u6b4c\ud83d\udcfb\n\ud83e\ude99\u4eba        \u54c1\u2728\u5ba0        \u7269\ud83d\udc08\n\ud83d\udcc6\u9ec4        \u5386\u2728\u89e3        \u68a6\ud83d\udd2e\n\ud83d\udce8\u62bd        \u7b7e\u2728\u89e3        \u7b7e\ud83d\udcc3\n\ud83d\udcb0\u6253        \u52ab\u2728\u76d1        \u72f1\u26d3\n\ud83d\ude4f\ud83c\udffb\u6c42  \u8d22  \u795e\u2728\u5f00  \u5b9d  \u7bb1\ud83d\udce6\n\ud83c\udfb6\u731c  \u6b4c  \u540d\u2728\u731c  \u82f1  \u96c4\u2753\n\u2652\u661f\u5ea7\u8fd0\u52bf\u2728\u661f\u5ea7\u7231\u60c5\u2650\n=======Wild Rift======\n\ud83c\udf92\u88c5\u5907\u67e5\u8be2\u2728\u5929\u8d4b\u6280\u80fd\ud83c\udf08\n\ud83d\udda5\u6559\u5b66\u89c6\u9891\u2728\u7248\u672c\u66f4\u65b0\ud83d\udcd6"

        print(message_data['from_wxid'])
        print(message_data['room_wxid'])
        chatRoom2 = '26095218987@chatroom'  # 老二测试
        chatRoom1 = '27352618533@chatroom'  # mainceshi
        myid = "wxid_3255602555615"

        if message_data['room_wxid'] == chatRoom1:

            # at bot
            # if(myid in message_data['at_user_list']):
            #     wechat_manager.send_chatroom_at_msg(client_id, chatRoom1, 'Test Passed!',  [message_data['from_wxid']])

            if (message_data['msg'] == '菜单'):
                wechat_manager.send_chatroom_at_msg(client_id, chatRoom1, menu,
                                                    [message_data['from_wxid']])
            if (message_data['msg'] == '签到'):
                self.signUp(client_id,chatRoom1,message_data['from_wxid'])

            if (message_data['msg'] == '巧克力'):
                wechat_manager.send_chatroom_at_msg(client_id, chatRoom1, "请注意体重{$@}",
                                                    [message_data['from_wxid']])


    @wechat.RECV_CALLBACK(in_class=True)
    def on_message(self, client_id, message_type, message_data):
        # 判断登录成功后，就向文件助手发条消息
        if message_type == MessageType.MT_USER_LOGIN:
            time.sleep(2)
            # wechat_manager.send_text(client_id, 'filehelper', '😂😂😂\uE052该消息通过wechat_pc_api项目接口发送')

            # wechat_manager.send_link(client_id,
            # 'filehelper',
            # 'wechat_pc_api项目',
            # 'WeChatPc机器人项目',
            # 'https://github.com/smallevilbeast/wechat_pc_api',
            # 'https://www.showdoc.com.cn/server/api/attachment/visitfile/sign/0203e82433363e5ff9c6aa88aa9f1bbe?showdoc=.jpg)')


        # text input
        if message_type == 11046: #text recieved
            self.inputText(client_id, message_data);




            # private message test passed
            # if message_data['from_wxid'] == 'wxid_opoo5fqu2f0x12':
            #     wechat_manager.send_text(client_id, 'wxid_opoo5fqu2f0x12', '多喝热水')




if __name__ == "__main__":
    bot = LoginTipBot()

    # 添加回调实例对象
    wechat_manager.add_callback_handler(bot)
    wechat_manager.manager_wechat(smart=True)

    # 阻塞主线程
    while True:
        time.sleep(0.5)
