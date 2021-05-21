import os
import re
from del_cheked import uniq

files = os.listdir(path="data/")
print(files)
all_data = []
for file in files:
  if re.search(r'\.csv\b', file):
    with open(f'data/{file}', 'r') as f:
      data = f.read()
      data = data.split(',')
      for i in data:
        all_data.append(i)
print(f'Из все аккаунтов для сбора собрано: {len(all_data)} подписоты')
udata = uniq(all_data)
print(f'Из них уникальных: {len(udata)}')
with open('data/followers_list.csv', 'w') as f:
    for el in udata:
        f.write(f'{el},')