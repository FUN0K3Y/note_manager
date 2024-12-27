username = input("Ваше имя пользователя: ")
content = input("Описание заметки: ")
status = input("Статус заметки (Активна/Завершена): ")
created_date = input("Дата создания (в формате ДД-ММ-ГГ): ")
issue_date = input("Дата истечения (в формате ДД-ММ-ГГ): ")

first_title = input("Введите первый заголовок вашей заметки: ")
second_title = input("Введите второй заголовок вашей заметки: ")
third_title = input("Введите третий заголовок вашей заметки: ")
titles = [first_title, second_title, third_title]

print("Ваше имя пользователя: ", username)
print("Заголовки:", titles)
print("Описание:", content)
print("Статус:", status)
print("Дата создания:", created_date)
print("Дата истечения:", issue_date)