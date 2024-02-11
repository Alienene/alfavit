# with open ("text.txt", "w") as file:
#     file.write('новий текст')

# with open ("text.txt", "r") as file:
#     data = file.read()

# print(data)
with open("text.txt", "r",encoding='utf-8') as file:
    data = file.read()

print(data)
result = ''
alfavit = 'абвгдеєзжиіїйклмнопрстуфхцчшщьюя'

for i in data:
    if i in alfavit:
        ind = alfavit.index(i)
        ind2 = ind + 1
        r = alfavit[ind2]
        result += r
    
print(result)