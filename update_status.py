def collect_titles():
    titles = []  # Список для хранения заголовков
    while True:
        title = input("Введите заголовок заметки (или оставьте пустым для завершения): ")
        if title == '':
            break  # Выход из цикла, если строка пустая
        titles.append(title)  # Добавляем заголовок в список
    return titles  # Возвращаем список заголовков


def collect_tasks():
    tasks = []  # Список для хранения задач
    while True:
        task = input("Введите задачу (или оставьте пустым для завершения): ")
        if task == '':
            break  # Выход из цикла, если строка пустая
        tasks.append(task)  # Добавляем задачу в список
    return tasks  # Возвращаем список задач


def update_status():
    print("\nВыберите новый статус заметки:")
    print("1. Выполнено")
    print("2. В процессе")
    print("3. Отложено")



    statuses = {
        '1': 'выполнено',
        '2': "в процессе",
        '3': "отложено"
    }
    while True:  # Запускаем цикл для повторного запроса при неправильном вводе
        choice = input("Ваш выбор: ")
        if choice in statuses:  # Проверяем правильность ввода
            new_status = statuses[choice]  # Получаем новый статус по выбору
            print(f"Статус заметки успешно обновлён на: \"{new_status}\"")
            break  # Выход из цикла при правильном вводе
        else:
            print("Неверный выбор. Пожалуйста, повторите попытку.")  # Сообщаем о неверном вводе

# Сбор заголовков и задач от пользователя
user_titles = collect_titles()  # Сбор заголовков
user_tasks = collect_tasks()  # Сбор задач

# Вывод всех данных
print("\nВы ввели следующие данные:")
print("Заголовки заметок:")
for title in user_titles:
    print("-", title)

print("\nЗадачи:")
for task in user_tasks:
    print("-", task)

# Обновление статуса
update_status()  # Функция для изменения статуса

#Можно в цикле при добавлении заголовка. Сделать в одну строку.
#
# note["titles"] = []
#
# for i in range(3):
#
# note["titles"].append(input(f"Введите заголовок заметки {i + 1}: ").strip().capitalize())