import random

"""Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого 
списка (могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию 
random); """


def create_list_names(strin, n):
    """
    Возвращает новый рандомный список из n элементов
    :param strin: список имен
    :param n: желаемая длина нового списка
    :return: список случайных имен
    """
    words = strin.split()
    lists = []
    for x in range(0, n + 1):
        lists.append(words[random.randint(0, len(words) - 1)])
    return lists


def print_most_freq_name(word_list):
    """
    Выводит самое популярное слово, его кол-во повторений и слова с такой же частотой
    :param word_list: список имен
    """
    if isinstance(word_list, list):
        pass
    else:
        print('Необходим список (list)')
        return
    counter = 0
    most_freq_word = ''
    addlist = []
    for x in word_list:
        count = word_list.count(x)
        if count > counter:
            counter = count
            most_freq_word = x
    for x in word_list:
        if counter == word_list.count(x):
            word = x
            addlist.append(word)
            same_freq = set(addlist)
            same_freq.remove(most_freq_word)
    if not same_freq:
        print(f'Самое частое имя: {most_freq_word}, встречается {counter} раз \n')
    else:
        print(
            f'Самое частое имя: {most_freq_word}, встречается {counter} раз, а также имена {same_freq} встречаются столько же раз\n')


def print_most_low_freq_letter(word_list):
    """
    Преобразует список слов в список из первых букв слов и выводит самые редкие
    :param word_list: список имен
    """
    if isinstance(word_list, list):
        pass
    else:
        print('Необходим список (list)')
        return
    counter = len(word_list)
    addlist = []
    word_list = list(map(lambda z: z[0], word_list))
    for x in word_list:
        count = word_list.count(x)
        if count < counter:
            counter = count
            most_rare_letter = x
    for x in word_list:
        if counter == word_list.count(x):
            word = x
            addlist.append(word)
            same_rare = set(addlist)
            same_rare.remove(most_rare_letter)
    if not same_rare:
        print(f'Самая редкая буква: {most_rare_letter}, встречается {counter} раз \n')
    else:
        print(
            f'Самая редкая буква: {most_rare_letter}, встречается {counter} раз, а также буквы {same_rare} настолько же редки \n')


# Первое задание
list_names = 'Денис Виктор Алена Вова Вадим Дарья Ева Захар Злата Григорий Матвей Яна Ася Петр Иван Дарина Галина ' \
             'Антон Алексей Виктор Влад Венера Дмитрий Лида Алина '
new_list_names = create_list_names(list_names, 50)
print(new_list_names, '\n')

# Второе задание
print_most_freq_name(new_list_names)

# Третье задание
print_most_low_freq_letter(new_list_names)


# Четвертое задание. В файле с логами найти дату самого позднего лога (по метке времени).

with open('log.txt', mode='rt', encoding='utf-8') as file:
    logs = file.read()

# print(logs)
logs = logs.split('\n')
last_log = max(logs, key=lambda x: x[:19])
print(f'Cамый поздний лог: \'{last_log}\', и его время: \'{last_log[:19]}\'')
