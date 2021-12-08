import vk_api
from vk_api import audio
import requests
import time
import os

vk_file = "vk_config.v2.json"
REQUEST_STATUS_CODE = 200
name_dir = 'music_vk'  # Папка, куда буду скачены песни

login = ''  # Номер телефона
password = ''  # Пароль
my_id = ''  # Ваш id
path = os.path.join("C:", "Users", "d3coy", "Music", "vk_music2", name_dir)  # Нужно прописать путь, где будет создана папка music_vk

if not os.path.exists(path):
    os.makedirs(path)

vk_session = vk_api.VkApi(login=login, password=password)
vk_session.auth()
vk = vk_session.get_api()
vk_audio = audio.VkAudio(vk_session)

os.chdir(path)



i = vk_audio.get(owner_id=my_id)[0]
r = requests.get(i["url"])
if r.status_code == REQUEST_STATUS_CODE:
    try:
        with open(i["artist"] + '_' + i["title"] + '.mp3', 'wb') as output_file:
            output_file.write(r.content)
    except OSError:
        with open(i["artist"] + '_' + i["title"] + '.mp3', 'wb') as output_file:
            output_file.write(r.content)
a = 0
time_start = time.time()
for i in vk_audio.get(owner_id=my_id):
    try:
        a += 1
        r = requests.get(i["url"])
        if r.status_code == REQUEST_STATUS_CODE:
            with open(i["artist"] + '_' + i["title"] + '.mp3', 'wb') as output_file:
                output_file.write(r.content)
    except OSError:
        print(a)
    
    time.sleep(2)

time_finish = time.time()
print("Time seconds:", time_finish - time_start)