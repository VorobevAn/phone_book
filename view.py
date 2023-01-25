import controller
def menu():
    command = [' Показать все контакты',
                'Открыть файл',
                'Сохранить файл',
                'Новый контакт',
                'Изменить контакт',
                'удалить контакт',
                'Найти контакт',
                'Выйти из программы']
    print('\n Выберете пункт меню: ')

    for i in range(len(command)):
        print(f'\t{i + 1}.{command[i]}')
    while True:
        try:
            user_input = int(input('\nВведите пункт меню: '))
            if user_input >= 1 and user_input <=8:
                return user_input
        except:
            print('Введите от 1 до 8')


def show_contact(phone_book: list):
    if len(phone_book) > 0:
        for item in phone_book:
            print(f'{item[0]} {item[1]} ({item[2]})')
    else:
        print('телефонная книга пуста')

def load_success():
    print('телефонная книга загружена успешно!!')

def save_success():
    print('телефонная книга сохранена успешно')

def new_contact():
    name = input('Введите Имя Фамилию контакта: ')
    phone = input('Ведите номер телефона: ')
    comment = input('Ведите комментарий: ')
    return name, phone, comment

def find_contact():
    secrch = input('Введите искомое значение: ')
    return secrch

def change_contact():
    change = input('какой контакт изменить? Введите имя : ')
    return change

def changeable_contact(answer):
    if answer == 'tru':
        print('Попробуйте снова ')
        controller.start()
    else:
        print('Заполните новые данные')



def dell_contact():
    contact = input('Какой контакт удалить?: ')
    return contact

def dellit_contakt(answer):
    if answer == 'нет':
        print('попробуйте повторить' )
        controller.start()
    print('Контакт успешно удален')