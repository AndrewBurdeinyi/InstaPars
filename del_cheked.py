
def del_akk(file, value):
    with open(file, 'r') as f:
        data = f.read()
        data = data.split(',')
    print(f'В списке было: {len(data)}')
    del data[0:value]
    print(f'В списке осталось: {len(data)}')
    with open(file, 'w') as f:
        for i in data:
            f.write(f'{i},')

def uniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output
