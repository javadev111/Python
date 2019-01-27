# coding: utf-8


#  1. Дано предложение. Заменить группы пробелов одиночными, крайние пробелы удалить.
#  Все слова перевести в нижний регистр, первые буквы сделать заглавными.
#
#
#  2. Дана строка. Заменить все ссылки и email на ***** (количество звездочек равно длине заменяемого фрагмента).
#  Примеры ссылок: www.site.com, http://site.com и т.п.
#
#
#  3. Пользователь бесконечно вводит e-mail адреса. Вывести только те, которые не повторяются


# sentence = input("Введите предложение: ")
# while "  " in sentence:
#     sentence = sentence.replace("  ", " ")
# if sentence[:1] == " ":
#     sentence = sentence[1:]
# if sentence[-1:] == " ":
#     sentence = sentence[:-1]
# print(sentence)

# user_str = 'www.site.com, asdf.sdfs, asdfdgdf, http://site.com'
# list_str = user_str.split(", ")
# print(list_str)
# for i in range(len(list_str)):
#     if (list_str[i].startswith("www.") or list_str[i].startswith("http://")) and list_str[i].endswith(".com"):
#         list_str[i] = '*'*len(list_str[i])
# print(', '.join(list_str))

# email_list = []
# while True:
#     user_input = input("Введите email: ")
#     if user_input not in email_list:
#         print(user_input)
#         email_list.append(user_input)
