def display_contacts(contacts):
    for contact in contacts:
        print(f"Фамилия: {contact['surname']}, Имя: {contact['name']}, Отчество: {contact['patronymic']}, Телефон: {contact['phone']}")

def import_contacts_from_file(filename):
    contacts = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                surname, name, patronymic, phone = line.strip().split(',')
                contacts.append({
                    'surname': surname,
                    'name': name,
                    'patronymic': patronymic,
                    'phone': phone
                })
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    return contacts

def export_contacts_to_file(filename, contacts):
    with open(filename, 'w', encoding='utf-8') as file:
        for contact in contacts:
            file.write(f"{contact['surname']},{contact['name']},{contact['patronymic']},{contact['phone']}\n")

def search_contacts(contacts, search_term):
    results = []
    for contact in contacts:
        if search_term.lower() in contact['surname'].lower() or search_term.lower() in contact['name'].lower() or search_term.lower() in contact['patronymic'].lower():
            results.append(contact)
    return results

def add_contact(contacts):
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone = input("Введите номер телефона: ")
    contacts.append({
        'surname': surname,
        'name': name,
        'patronymic': patronymic,
        'phone': phone
    })
    print("Контакт успешно добавлен.")

def delete_contact(contacts, search_term):
    results = search_contacts(contacts, search_term)
    if not results:
        print("Контакт не найден.")
        return
    for contact in results:
        contacts.remove(contact)
    print("Контакт успешно удален.")

def copy_line_from_file_to_file(source_file_path, destination_file_path, line_number):
    try:
        with open(source_file_path, 'r', encoding='utf-8') as source_file:
            lines = source_file.readlines()
            if line_number > len(lines) or line_number <= 0:
                print("Номер строки выходит за пределы файла.")
                return
            line_to_copy = lines[line_number - 1]
        with open(destination_file_path, 'a', encoding='utf-8') as destination_file:
            destination_file.write(line_to_copy)
        print(f"Строка {line_number} успешно скопирована в {destination_file_path}.")
    except FileNotFoundError:
        print("Один из файлов не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def main():
    filename = 'phonebook.txt'
    contacts = import_contacts_from_file(filename)

    while True:
        print("\nТелефонный справочник:")
        print("1. Вывести все контакты")
        print("2. Поиск контакта")
        print("3. Добавить новый контакт")
        print("4. Удалить контакт")
        print("5. Копировать строку из файла в файл")
        print("6. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            display_contacts(contacts)
        elif choice == '2':
            search_term = input("Введите фамилию, имя или отчество для поиска: ")
            search_results = search_contacts(contacts, search_term)
            display_contacts(search_results)
        elif choice == '3':
            add_contact(contacts)
        elif choice == '4':
            search_term = input("Введите фамилию, имя или отчество контакта для удаления: ")
            delete_contact(contacts, search_term)
        elif choice == '5':
            source_file_path = input("Введите путь к исходному файлу: ")
            destination_file_path = input("Введите путь к файлу назначения: ")
            line_number_to_copy = int(input("Введите номер строки для копирования: "))
            copy_line_from_file_to_file(source_file_path, destination_file_path, line_number_to_copy)
        elif choice == '6':
            export_contacts_to_file(filename, contacts)
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()