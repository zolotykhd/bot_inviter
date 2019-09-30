import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint
from multiprocessing import Process
import time
vk_session = vk_api.VkApi(
    token='33d1b3adaa513cc6dcc7366f710763949c787e9ff0147045df4092be34acaad64d006d058c7ea1bd9b365')
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()


def send_info():
    try:
        time.sleep(10)
        vk.messages.send(  # Отправляем сообщение
            user_id=event.user_id,
            message='Вот тебе ссылка, молодец что нашел код, добро пожаловать в братство. Но не расслабляйся, ещё предстоят испытания.\n https://vk.me/join/AJQ1d1vP4BT3_VhNkfSEMe4X',
            random_id=randint(1, 12421344122222222222225)
        )
    except:
        pass


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        # Слушаем longpoll, если пришло сообщение то:
        msg = event.text
        if msg.lower() == 'хочу в sss':  # Если написали заданную фразу
            send_info()
