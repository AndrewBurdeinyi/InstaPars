from instabot import Bot
import re
from del_cheked import del_akk

# SETTINGS
file = 'data/followers_list.csv'
stop = 400

akks = []

for akk in akks:

    login = akk[0]
    pswd = akk[1]

    print(f'Стартую с аккаунтом {login}, {pswd}')

    bot = Bot()
    bot.login(username=login, password=pswd, use_cookie=False)

    with open(file, 'r') as f:
        data = f.read()
    user_followers = data.split(',')

    all_user = len(user_followers)
    index = 1
    taplink = 0
    for user in user_followers:
        if index > stop:
            print(f'{stop} аккаунтов отработано, удаляю их со списка')
            del_akk(file, stop)
            print('Пора сменить акк!')
            break
        user_info = bot.get_user_info(user)
        link = user_info['external_url']
        if re.search(r'\btaplink\b', link):
            taplink += 1
            with open('result.csv', 'r') as f:
                data = f.read()
            username = bot.get_username_from_user_id(user)
            with open('result.csv', 'w') as f:
                f.write(f'{data}\n{username},{link}')
        print(f'Обработано {index} из {all_user}, с таплинком {taplink}')
        index += 1
