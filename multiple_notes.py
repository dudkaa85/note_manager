def main():
    notes = []  # Список для хранения заметок

    while True:
        # Запрашиваем у пользователя название заметки, если он хочет закончить - вводим "стоп"
        print("Введите информацию о заметке или 'стоп' для завершения:")
        title = input("Заголовок заметки: ")
        if title.lower() == "стоп":
            break

        name = input("Имя автора заметки: ")
        description = input("Описание заметки: ")
        status = input("Статус заметки (например, 'новая', 'в процессе', 'завершена'): ")
        creation_daate = input("Дата создания заметки (например, '27-11-2023'): ")
        deadline = input("Дедлайн заметки (например, '30-11-2023'): ")

        # Создаем словарь для заметки
        note = {
            "title": title,
            "name": name,
            "description": description,
            "status": status,
            "creation_daate": creation_daate,
            "deadline": deadline
        }

        # Добавляем заметку в список
        notes.append(note)

    # Отображаем все созданные заметки
    print("\nВсе созданные заметки:")
    for i, note in enumerate(notes, start=1):
        print(f"\nЗаметка {i}:")
        for key, value in note.items():
            print(f"{key.capitalize()}: {value}")

if __name__ == "__main__":
    main()

