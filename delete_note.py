def display_notes(notes):
    """Функция для отображения текущих заметок."""
    if not notes:
        print("Нет заметок для отображения.")
        return
    print("\nТекущие заметки:")
    for i, note in enumerate(notes, start=1):
        print(f"{i}. Имя: {note['name']}\n   Заголовок: {note['title']}\n   Описание: {note['description']}\n")

def delete_note_by_name_or_title(notes):
    """Функция для удаления заметки по имени пользователя или заголовку."""
    value = input("Введите имя пользователя или заголовок для удаления заметки: ").strip()

    # Хранение первоначальной длины списка для проверки, были ли удалены заметки
    initial_length = len(notes)

    # Удаляем заметки, соответствующие введенному значению (по имени или заголовку)
    notes[:] = [note for note in notes if note['name'] != value and note['title'] != value]

    # Проверка, были ли найдены заметки для удаления
    if len(notes) < initial_length:
        print("Успешно удалено. Остались следующие заметки:")
    else:
        print("Заметка не найдена.")
        return

    # Отображаем оставшиеся заметки
    display_notes(notes)

def main():
    notes = [
        {"title": "Список покупок", "name": "Алексей", "description": "Купить продукты на неделю"},
        {"title": "Учеба", "name": "Мария", "description": "Подготовиться к экзамену"},
    ]  # Пример списка заметок

    print("Текущие заметки:")
    display_notes(notes)  # Отобразить текущие заметки

    # Удаление заметки по имени пользователя или заголовку
    delete_note_by_name_or_title(notes)

if __name__ == "__main__":
    main()
