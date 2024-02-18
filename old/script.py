from datetime import date
from dnevnik import messages

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


clear_console()
print('Ты в режиме записи заметок.')
print('Введите "mod" или "ред" что изменить заметку')
print('Введите "exit" или "выход" чтобы выйти из режима записи заметок')
print('Введите "cls" или "очистить" чтобы удалить заметки')
print()

while 1:
    message = input('Введи своё сообщение: ')
    if message.replace(' ', '') != '':
        if message.lower() == 'exit' or message == 'выход':
            print()
            print('\033[31mВы вышли из режима записи заметок\033[0m')
            break
        elif message.lower() == 'mod' or message.lower() == 'ред':
            modifyLine = int(input('\033[33mВведи номер строки которую хочешь периписать: \033[0m'))
            newMess = input('\033[33mВведи новую заметку: \033[0m')
            if newMess.replace(' ', '') != '':
                newMess = capitalize_after_space(newMess)
                messages[modifyLine - 1]['message'] = newMess
            else:
                del messages[modifyLine - 1]
            zapis()
            print()
            print('\033[33mРедактирование завершено\033[0m')
            print()
        elif message.lower() == 'cls' or message.lower() == 'очистить':
            messages.clear()
            zapis()
            print('Заметки успешно очищены')
        elif message.lower() == 'watch' or message.lower() == 'смотреть':
            timeVarible = None
            count = 0
            if messages == []:
                clear_console()
                print('У тебя нет заметок')
            else:
                clear_console()
                print('Твои заметки:')
                try:
                    for el in messages:
                        if messages[count]['time'] != timeVarible:
                            print()
                            print(f"    \033[31m{messages[count]['time']}\033[0m")
                            print()
                            timeVarible = messages[count]['time']
                        print(f"        { count + 1}) {messages[count]['message']}")
                        if messages[count]['time'] == messages[count+1]['time']:
                            print('        ----')
                        count += 1
                except IndexError:
                    pass
            print()
        else:
            time = date.today().strftime('%d.%m.%Y')
            message = capitalize_after_space(message)
            slovar = {'time': time, 'message': message}
            messages.append(slovar)
            zapis()