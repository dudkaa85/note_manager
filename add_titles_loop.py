def collect_titles():
    titles = []  # Список для хранения заголовков
    while True:
        title = input("Введите заголовок заметки (или оставьте пустым для завершения): ").strip().capitalize()
        if title == '':
            break  # Выход из цикла, если строка пустая
        titles.append(title)  # Добавляем заголовок в список
    return titles  # Возвращаем список заголовков


def collect_tasks():
    tasks = []  # Список для хранения задач
    while True:
        task = input("Введите задачу (или оставьте пустым для завершения): ").strip().capitalize()
        if task == '':
            break  # Выход из цикла, если строка пустая
        tasks.append(task)  # Добавляем задачу в список
    return tasks  # Возвращаем список задач


# Сбор заголовков и задач от пользователя
user_titles = collect_titles()  # Сбор заголовков
user_tasks = collect_tasks()  # Сбор задач

# Вывод всех данных
print("\nВы ввели следующие данные:")
print("основные идеи: ")
for title in user_titles:
    print("-", title)

print("\nСписок Задачи: ")
for task in user_tasks:
    print("-", task)
