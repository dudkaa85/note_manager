from datetime import datetime

def main():
    current_date = datetime.now()
    current_date_str = current_date.strftime('%d-%m-%Y')
    print(f"текущая дата: {current_date_str}")

    while True:
        # Запрашиваем у пользователя дату дедлайна
        issue_date_str = input("введите дату дедлайна (в формате день-месяц-год): ")

        # Обрабатываем вводные данные
        try:
            # Преобразуем вводимую дату в объект datetime
            issue_date = datetime.strptime(issue_date_str, "%d-%m-%Y")
            break
        except ValueError:
            print("не верный формат даты, попробуйте ввести в формате день-месяц-год.")

    # Сравниваем даты
    if issue_date < current_date:
        days_overdue = (current_date - issue_date).days
        print(f"внимание! дедлайн истёк {days_overdue} дня(-ей) назад.")
    elif issue_date > current_date:
        days_remaining = (issue_date - current_date).days
        print(f"до дедлайна осталось {days_remaining} дня(-ей).")
    else:
        print("дедлайн совпадает с текущей датой.")

if __name__ == "__main__":
    main()



