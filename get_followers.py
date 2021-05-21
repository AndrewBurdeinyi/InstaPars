
from del_cheked import uniq
from instabot import Bot


bot = Bot()
bot.login(username="draftbrandi", password="krzJrodB", use_cookie=False)
file = 'data/followers_list.csv'

get_list = ['taplink_master', 'dashliss', 'miss_taplink', 'vidyukova_taplink', 'taplink_pustovalova',
            'taplink_podobashina', 'lilya_dit', 'annakind_taplink', 'kate.mist', 'malva_design_taplink', 'wera.website']
for i in get_list:
    print(f'Собираю подписоту у {i}')
    user_followers = bot.get_user_followers(i)

    with open(f'data/followers_list_{i}.csv', 'w') as f:
        for user in user_followers:
            f.write(f'{user},')











