'''Описание проекта: программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля,
а также на то, какие символы требуется в него включить, а какие исключить.'''

import random

digits='123456789'
lowercase_letters='abcdefghjkmnpqrstuvwxyz'
uppercase_letters=lowercase_letters.upper()
punctuation='!#$%&*+-=?@^_'
dispute='il1Lo0O'
chars=''

coun=int(input('Количество паролей для генерации: '))
leng=int(input('Длина одного пароля: '))
c = input('Включать ли цифры 0123456789? (y/n) ')
if c=='y':
    chars+=digits
c1 = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n) ')
if c1=='y':
    chars+=uppercase_letters
c2 = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n) ')
if c2=='y':
    chars+=lowercase_letters
c3 = input('Включать ли символы !#$%&*+-=?@^_? (y/n) ')
if c3=='y':
    chars+=punctuation
c4 = input('Включать ли неоднозначные символы il1Lo0O? (y/n) ')
if c4=='y':
    chars+=dispute

print(chars)
def gener(a,let):
    p=''
    for i in range(let):
        p+=a[random.randint(0,len(a))]
    return p

for i in range(coun):
    print(gener(chars,leng))
