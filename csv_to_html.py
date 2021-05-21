from yattag import Doc

doc, tag, text = Doc().tagtext()
linksA = []
linksB = []
index = 0
with open('result.csv', 'r') as f:
    data = f.read()
    data = data.split('\n')
    for i in data:
        i = i.split(',')
        if index % 2:
            linksA.append(i)
        else:
            linksB.append(i)
        index += 1

print(linksA)
print(len(linksA))
print(linksB)
print(len(linksB))

with tag('html'):
    with tag('body'):
        for i in linksB:
            with tag('a', href=i[1]):
                text(f'https://www.instagram.com/{i[0]}')

result = doc.getvalue()
with open('index2.html', 'w') as f:
    f.write(result)