import json
from datetime import date

def proverka(time):
    res = False
    for item in dnevnik:
        if item['time'] == time:
            res = True
    return res

def findForTime(time):
    count = 0
    for item in dnevnik:
        if item['time'] == time:
            break
        count += 1
    return count 

def capitalize_after_dot(string):
    words = string.split('. ')
    new_string = []
    for word in words:
        if word:
            new_word = word[0].upper() + word[1:]
            new_string.append(new_word)
    return '. '.join(new_string)

def clear_console():
    import os
    operating_system = os.name
    if operating_system == 'posix':
        _ = os.system('clear')
    elif operating_system == 'nt' or operating_system == 'dos':
        _ = os.system('cls')
    else:
        print("Очистка консоли не поддерживается на данной операционной системе.")
clear_console()

def capitalize_after_space(word):
    word = word.replace(".", ". ")
    word = " ".join(word.replace(" ", " ").split())
    word = word.replace(' .', '.')
    word = capitalize_after_dot(word)
    if word[-1] not in ['.', '!', '?']:
        word = word[0].upper() + word[1:] + "."
    return word

def zapis():
    with open('dnevnik.py', 'w', encoding="utf-8") as file:
        word = f'messages = {messages}'
        file.write(word)

with open('new_dnevnil.json', encoding='utf-8') as file:
    dnevnik = json.load(file)

userMessage = input('Сообщение: ')
time = date.today().strftime('%d.%m.%Y')

if userMessage == 'смотреть':
    localTime = None
    for item in dnevnik:
        if item['time'] != localTime:
            localTime = item['time']
        print(f'\033[91m{localTime}\033[0m')
        for el in item['mess']:
            print(f'    {el}')
else:
    if proverka(time):
        dnevnik[findForTime(time)]['mess'].append(capitalize_after_space(userMessage))
    else:
        dnevnik.append({'mess': [capitalize_after_space(userMessage)], 'time': time})

    with open('new_dnevnil.json', 'w', encoding='utf-8') as file:
        json.dump(dnevnik, file, indent=4, ensure_ascii=False)

print('''
Выполнение кода завершено''')