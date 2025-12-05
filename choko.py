contacts = {
    # ----------------------------------------------------
    # Димаш Кудайберген (Мировой певец)
    # ----------------------------------------------------
    'Димаш Кудайберген': {
        'phones': ['+77011234567'], 
        'emails': ['dimash.dears@official.kz', 'dima.kudaibergen@music.com'],
        'notes': 'Казахстанский певец, обладатель уникального вокального диапазона.'
    },
    
    # ----------------------------------------------------
    # Геннадий Головкин (Боксер)
    # ----------------------------------------------------
    'Геннадий Головкин': {
        'phones': ['+77770001122'],
        'emails': [],  # Умышленно пустой список
        'notes': 'Профессиональный боксер, чемпион мира в среднем весе.'
    },

    # ----------------------------------------------------
    # Баян Алагузова (Продюсер, медиаперсона)
    # ----------------------------------------------------
    'Баян Алагузова': {
        'phones': ['+77079998877'], 
        'emails': ['bayan.maxatkyzy@media.kz'],
        'notes': 'Известный продюсер и телеведущая Казахстана.'
    },
    
    # ----------------------------------------------------
    # Илья Ильин (Тяжелоатлет)
    # ----------------------------------------------------
    'Илья Ильин': {
        'phones': ['+77053334455'], 
        'emails': ['ilya.ilin@sport.kz'],
        'notes': 'Тяжелоатлет, многократный чемпион мира.'
    }
}
def view_all_names():
    for name in sorted(contacts.keys()):
        print(name)


def add_contact():
    name = input("Введите имя: ").strip()
    if not name:
        print("Имя не может быть пустым.")
        return
    if name in contacts:
        print("Контакт уже существует.")
        return
    contacts[name] = {'phones': [], 'emails': [], 'notes': ''}
    print(f"Контакт '{name}' добавлен.")


def view_details():
    name = input("Введите имя: ").strip()
    if name not in contacts:
        print("Контакт не найден.")
        return
    for phone in contacts[name]['phones']:
        print("Телефон:", phone)
    for email in contacts[name]['emails']:
        print("Email:", email)
    if contacts[name]['notes']:
        print("Заметки:", contacts[name]['notes'])


def modify_data():
    name = input("Кого изменить? ").strip()
    if name not in contacts:
        print('Контакт не найден')
        return

    print("Что хотите изменить или добавить?")
    print("1 — email")
    print("2 — телефон")
    print("3 — заметка")
    choice = input("Выберите: ").strip()
    new = input("Введите что хотите добавить: ").strip()

    if choice == "1":
        contacts[name]['emails'].append(new)
        print("Email добавлен.")
    elif choice == "2":
        contacts[name]['phones'].append(new)
        print("Телефон добавлен.")
    elif choice == "3":
        if contacts[name]['notes']:
            contacts[name]['notes'] += "\n" + new
        else:
            contacts[name]['notes'] = new
        print("Заметка обновлена.")
    else:
        print("Неверный выбор.")


def delete_contact():
    """Удалить контакт по имени."""
    name = input("Введите имя для удаления: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Контакт '{name}' удалён.")
    else:
        print("Контакт не найден!")


# Пример использования:
if __name__ == "__main__":
    while True:
        print("\n--- Меню ---")
        print("1. Показать все имена")
        print("2. Добавить контакт")
        print("3. Просмотреть детали")
        print("4. Изменить данные")
        print("5. Удалить контакт")
        print("6. Выйти")
        option = input("Выберите действие (1-6): ").strip()

        if option == "1":
            view_all_names()
        elif option == "2":
            add_contact()
        elif option == "3":
            view_details()
        elif option == "4":
            modify_data()
        elif option == "5":
            delete_contact()
        elif option == "6":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")