# Примечание:
# Табуляция в 4 пробела
import os

PATH = "HW_Seminar_8\Phonebook\phonebook.txt"


def main_menu():                # Главное меню справочника
    print('=' * 60)
    print("\t\tТЕЛЕФОННЫЙ СПРАВОЧНИК")
    print('=' * 60)
    print("Выберете пункт в главном меню:")
    print("\t1. Показать весь список контактов")
    print("\t2. Добавить новый контакт в справочник")
    print("\t3. Поиск контакта в справочнике")
    print("\t4. Редактировать контакт в справочнике")
    print("\t5. Удалить контакт")
    print("\t6. Закрыть телефонный справочник")
    print('=' * 60)


def all_list():                 # Выводит весь список телефонного справочника
    file = open(PATH, 'r', encoding='UTF-8')
    data = file.readlines()
    file.close
    clear()
    print('=' * 60)
    print("Все контакты в телефонном справочнике: ")
    print()
    count = 0
    for i in data:

        print(f'\t{count}. {i}')
        count += 1
    if count == 0:
        print("\t\tСписок контактов пуст\n")
    elif count >= 1:
        print()
        print('=' * 60)
        print(f"Всего контактов: {count-1}")


def add_contact():              # Добавление нового контакта в справочник
    clear()
    print('=' * 60)
    print("     Добавление нового контакта в телефонный справочник")
    print('=' * 60)
    file = open(PATH, 'a', encoding='UTF-8')
    size = 3
    new_contact = []
    print("\t\t    !!!ПРИМЕЧАНИЕ!!!\n\tПункты помеченные *, обязательны для ввода.")
    print('=' * 60)
    print("Введите данные контакта:")
    for i in range(size):
        if i == 0:
            fio = input("* ФИО: ")
            if fio == "":
                new_contact.append("-")
            else:
                new_contact.append(fio)
            i += 1
            if i == 1:
                phone = input("* Телефон: ")
                if phone == "":
                    new_contact.append("-")
                else:
                    new_contact.append(phone)
                i += 1
                if i == 2:
                    comment = input("Комментарий: ")
                    if comment == "":
                        new_contact.append("-")
                    else:
                        new_contact.append(comment)
    if new_contact[0] == "-" and new_contact[1] == "-":
        print('=' * 60)
        print()
        print(
            "\t      Создание контакта не возможно!\n\t\t  Введите имя и телефон.")
        print()
    else:
        directory_entry = ', '.join(new_contact)
        print(f'\nНовый контакт: {directory_entry}')
        file.writelines('\n')
        file.writelines(directory_entry)
        print('=' * 60)
        print()
        print("\t      Новый контакт успешно создан!\n\t\t")
        file.close()


def find_contact():             # Поиск контакта в телефонном справочнике
    clear()
    print('=' * 60)
    print("\t  Поиск контакта в телефонном справочнике")
    print('=' * 60)
    contact_details = input("Введите данные контакта для поиска: ").lower()
    print()
    file = open(PATH, 'r', encoding='UTF-8')
    data = file.readlines()
    count = 0
    for i in data:
        if contact_details in i.lower():
            count += 1
            print(f'\t     {count}. {i}')
    print(f'\nНайдено совпадений: {count}')
    if count == 0:
        print('=' * 60)
        print(f"\n\t    Контакта с именем {contact_details} не найдено!\n")
    file.close()


def edit_contact():             # Редактирование контакта в телефонном справочнике
    file = open(PATH, 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    all_list()
    edit_data = input(
        "Введите данные контакта для его редактирования.\n\n\tВведите: ").lower()
    print()
    print('=' * 60)
    print()
    count = 0
    for i in data:
        if edit_data in i.lower():
            print(f'Выбран контакт: {i}')
            count += 1
            contact_in_file = i
    if count == 0:
        print(f"\n\tКонтакта с такими данными {edit_data} не существует!\n")
    if count == 1:
        data.remove(contact_in_file)
        file = open(PATH, 'w', encoding='UTF-8')
        for i in data:
            file.writelines(i)
        file.close()
        print('=' * 60)
        print("\t      Введите новые данные контакта")
        new_data()
    elif count != 1 and count != 0:
        print("\tУпс! Что-то пошло не так :(\nВыберите контакт из списка совпадений и еще раз введите его полные данные")
        edit_contact()


def delete_contact():               # Удаление контакта из справочника
    file = open(PATH, 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    all_list()
    print('=' * 60)
    print("\tУдаление контакта в телефонном справочнике")
    print('=' * 60)
    delete_data = input(
        "\t   Введите данные контакта для удаления\n\n\tВведите: ").lower()
    print()
    print('=' * 60)
    count = 0
    for i in data:
        if delete_data in i.lower():
            print(f'\nВыбран контакт для удаления: {i}')
            count += 1
            result = i
    if count == 0:
        print(f"\n\tКонтакта с именем {delete_data} не существует!\n")
        print('=' * 60)
    if count == 1:
        print('=' * 60)
        print(f'\n\t   Данный контакт был успешно удален!\n')
        data.remove(result)
        file = open(PATH, 'w', encoding='UTF-8')
        for i in data:
            file.writelines(f'{i}')
        file.close()
    elif count != 1 and count != 0:
        print("\tУпс! Что-то пошло не так :(\nВыберите контакт из списка совпадений и еще раз введите его полные данные")
        # print('=' * 60)
    print("\n\t      Упс! Что-то пошло не так :(\n\t\t  Попробуйте снова.\n")
    print('=' * 60)
    delete_contact()


def new_data():             # Функция для редактирования контактных данных
    file = open(PATH, 'a', encoding='UTF-8')
    size = 3
    new_data_contact = []
    print('=' * 60)
    print("\t\t    !!!ПРИМЕЧАНИЕ!!!\n\tПункты помеченные *, обязательны для ввода.")
    print('=' * 60)
    print("Введите данные контакта:")
    for i in range(size):
        if i == 0:
            fio = input("* ФИО: ")
            if fio == "":
                new_data_contact.append("-")
            else:
                new_data_contact.append(fio)
            i += 1
            if i == 1:
                phone = input("* Телефон: ")
                if phone == "":
                    new_data_contact.append("-")
                else:
                    new_data_contact.append(phone)
                i += 1
                if i == 2:
                    comment = input("Комментарий: ")
                    if comment == "":
                        new_data_contact.append("-")
                    else:
                        new_data_contact.append(comment)
    if new_data_contact[0] == "-" and new_data_contact[1] == "-":
        print('=' * 60)
        print()
        print(
            "\t      Редактирование контакта не возможно!\n\t\t  Введите имя и телефон.")
        print()
    else:
        directory_entry = ', '.join(new_data_contact)
        print(f'\nДанные контакта: {directory_entry}')
        file.writelines('\n')
        file.writelines(directory_entry)
        print('=' * 60)
        print()
        print("\t      Данные контакта успешно обновлены!\n\t\t")
        file.close()


def back_or_close():            # Возврат в главное меню или закрытие справочника
    back_close = True
    choose2 = 0
    while back_close:
        choose2 = int(input("Выберете действие: "))
        if choose2 == 1:
            back_close = False
        elif choose2 == 2:
            print_message_pb()
        else:
            clear()
            print('=' * 60)
            print(
                "\n\t      Упс! Что-то пошло не так :(\n\t\t  Попробуйте снова.\n")
            print_message_back()
    if choose2 == 1:
        clear()
        print('=' * 60)
        print("\t     Вы вернулись в главное меню!")
        return main_menu()


def print_message_pb():         # Сообщение о закрытии телефонного справочника
    clear()
    print('=' * 60)
    print("\t\tТелефонный справочник закрыт!\n\t\t\tДо свидания!")
    print('=' * 60)
    exit()


def clear():                    # отчистка консоли
    os.system('cls')


def print_message_back():       # Сообщение о возврате в главное меню или закрытия справочника
    print('=' * 60)
    print("Для возврата в главное меню, введите: 1")
    print("Закрыть телефонный справочник, введите: 2")
    print('=' * 60)


if __name__ == "__main__":
    clear()
    main_menu()
    while True:
        choose = int(input("Введите выбранный пункт: "))
        if choose == 1:
            all_list()
            print_message_back()
            back_or_close()
        if choose == 2:
            add_contact()
            print_message_back()
            back_or_close()
        if choose == 3:
            find_contact()
            print_message_back()
            back_or_close()
        if choose == 4:
            edit_contact()
            print_message_back()
            back_or_close()
        if choose == 5:
            delete_contact()
            print_message_back()
            back_or_close()
        if choose == 6:
            print_message_pb()
