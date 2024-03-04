
def work_with_phonebook():
    
    choice = show_menu()
    print()

    phone_book = read_txt('phone.txt')

    while (choice != 8):

        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            find_by_lastname(phone_book)
        elif choice == 3:
            find_by_number(phone_book)
        elif choice == 4:
            add_abonent(phone_book)
            write_txt('phone.txt',phone_book)
        elif choice == 5:
            copy_txt('phone.txt')
        elif choice == 6:
            print('До свидания!')
            break
        choice=show_menu()

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Копировать запись из одного файла в другой\n"
          "6. Закончить работу")
    choice = int(input())
    return choice      

def find_by_lastname(phone_book):

    last_name = input('Введите фамилию для поиска: ')
    print()

    for abonent in phone_book: 
        if last_name.lower() in abonent['Фамилия'].lower():
            print(f'Фамилия: {abonent['Фамилия']}')
            print(f'Имя: {abonent['Имя']}')
            print(f'Телефон: {abonent['Телефон']}')
            print(f'Описание: {abonent['Описание']}')

def find_by_number(phone_book):

    find_number = input('Введите телефон для поиска: ')
    print()

    for abonent in phone_book: 
        if find_number.lower() in abonent['Телефон'].lower():
            print(f'Фамилия: {abonent['Фамилия']}')
            print(f'Имя: {abonent['Имя']}')
            print(f'Телефон: {abonent['Телефон']}')
            print(f'Описание: {abonent['Описание']}')

def add_abonent(phone_book):

    last_name = input('Введите фамилию: ')
    name = input('Введите имя: ')  
    phone = input('Введите номер телефона: ')
    description = input('Введите описание: ')
    new_abonent = {'Фамилия': last_name, 'Имя': name, 'Телефон': phone, 'Описание': description}
    phone_book.append(new_abonent)
    return phone_book

def print_result(phone_book):

    for i in range(len(phone_book) - 1):
        for k, v in phone_book[i].items():
            print(f'{k}: {v}')
        
def read_txt(filename):

    phone_book = []

    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename, "r", encoding='utf-8') as phb:

        for line in phb:
             record = dict(zip(fields, line.split(",")))
             phone_book.append(record)

    return phone_book

def copy_txt(filename, file_name_to_copy = 'phone2.txt'):
    
    num = int(input('Введите номер строки который хотите скопировать: '))
    num_line = num - 1
    print()
    copy_line = None
    i = 0
    flag = True

    with open(filename, "r", encoding='utf-8') as readfile:
        for line in readfile:
            if num_line == i:
                copy_line = line       
            i += 1

    if num_line >= i:
        print('Такой записи в телефонной книге ещё нету!')
        flag = False

    if flag:
        with open(file_name_to_copy, 'a', encoding='utf-8') as copyfile:
            copyfile.write(f'{copy_line}')

def write_txt(filename, phone_book):

    with open(filename, 'w', encoding = 'utf-8') as phout:

        for i in phone_book:
            s = ''
            for v in i.values():
                s = s + v + ','
            phout.write(f'{s[:-1]} \n')

work_with_phonebook()




