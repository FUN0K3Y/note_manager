note = {}

note["username"] = input("Ваше имя пользователя: "),
note["content"] = input("Описание заметки: "),
note["status"] = input("Статус заметки (Активна/Завершена): "),
note["created_date"] = input("Дата создания (в формате ДД-ММ-ГГ): "),
note["issue_date"] = input("Дата истечения (в формате ДД-ММ-ГГ): "),

first_title = input("Введите первый заголовок вашей заметки: "),
second_title = input("Введите второй заголовок вашей заметки: "),
third_title = input("Введите третий заголовок вашей заметки: "),
note["titles"] = [first_title, second_title, third_title]

print("Ваша заметка: ", note)