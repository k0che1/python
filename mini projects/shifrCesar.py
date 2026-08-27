'''
Описание проекта: требуется написать программу, способную шифровать и дешифровать текст в соответствии с алгоритмом Цезаря.
Она должна запрашивать у пользователя следующие данные:

направление: шифрование или дешифрование;
язык алфавита: русский или английский;
шаг сдвига (со сдвигом вправо).
'''
e_l = 'abcdefghijklmnopqrstuvwxyz'
r_l = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
e_u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
r_u = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

def shifrovanie_low(al_l,sag,ind):
    if ind + sag >= len(al_l):
        return al_l[(ind + sag) - len(al_l)]

    else:
        return al_l[ind+sag]

def shifrovanie_up(al_u,sag,ind):
    if ind + sag >= len(al_u):
        return al_u[(ind + sag) - len(al_u)]

    else:
        return al_u[ind+sag]

def deshifrovanie_low(al_l,sag,ind):
    return al_l[ind-sag]

def deshifrovanie_up(al_u,sag,ind):
    return al_u[ind-sag]


fraz=input('Введите фразу ')
direction=input('шифрование или дешифрование (s / d) ')
alph=input('язык алфавита: русский или английский (r or e) ')
step=int(input('шаг сдвига '))
'''
fraz='Блажен, кто верует, тепло ему на свете!'
direction='s'
alph='r'
step=10'''
itog_fraz=''

al_l=e_l if alph=='e' else r_l
al_u=e_u if alph=='e' else r_u
if direction=='s':
    for i in range(len(fraz)):
        if fraz[i] in al_l:
            itog_fraz+=shifrovanie_low(al_l,step,al_l.index(fraz[i]))
        elif fraz[i] in al_u:
             itog_fraz+=shifrovanie_up(al_u,step,al_u.index(fraz[i]))
        else:
            itog_fraz+=fraz[i]


if direction=='d':
    for i in range(len(fraz)):
        if fraz[i] in al_l:
            itog_fraz+=deshifrovanie_low(al_l,step,al_l.index(fraz[i]))
        elif fraz[i] in al_u:
            itog_fraz+=deshifrovanie_up(al_u,step,al_u.index(fraz[i]))
        else:
            itog_fraz+=fraz[i]


print(itog_fraz)
