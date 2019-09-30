import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint
from multiprocessing import Process
import time

vk_session = vk_api.VkApi(
    token='fffdd18f111d1aeaec537529fa93b8dab65daa3a7fc5c5e99d8c0a5355f6a1bd4ef0f277ef58af6cc89c8')
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()


def send_info():
    try:
        time.sleep(10)
        vk.messages.send(  # Отправляем сообщение
            user_id=event.user_id,
            message='Зайди в мой закреп и в комменты, там ссылка на группу, туда ты должен прислать код который найдёшь '
                    'на моей странице, код двузначный. Подсказок больше не дам.',
            random_id=randint(1, 12421344122222222222225)
        )
    except:
        pass


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        # Слушаем longpoll, если пришло сообщение то:
        msg = event.text
        if msg.lower() == 'sss':  # Если написали заданную фразу
            send_info()
