phone_book = []
path = 'phone_book.txt'



def get_phone_book():
    global phone_book
    return phone_book


def update_phone_book(contact: list):
    global phone_book
    phone_book.append(contact)




def open_phone_book():
    global path
    global phone_book
    with open(path, 'r', encoding='UTF-8') as file:
       data = file.readlines()
       for line in data:
          phone_book.append(line.strip().split(';'))


def save_phone_book():
    global path
    global phone_book
    data = []
    for line in phone_book:
        data.append(';'.join(line))
    with open(path, 'w', encoding = 'UTF-8') as file:
        data = file.write('\n'.join(data))


def search_contact(search: str):
    global phone_book
    search_result = []
    for line in phone_book:
        for field in line:
            if search in field:
                search_result.append(line)
                break
    return search_result

def dell_contact(contakt: str):
    global phone_book
    answer = 'нет'
    for item in phone_book:
        for neim in item:
            if contakt in neim:
                print(*item)
                answer = input('Удалить? да\нет: ')
                if answer.lower() == 'да':
                    phone_book.remove(item)
                else:
                    print('Повторите поиск ')
                    return answer
    return answer

def change_phone_book(change):
    global phone_book
    answer = 'folse'
    for element in phone_book:
        for meaning in element:
            if change in meaning:
                print(*element)

                if input('Изменить контакт? да\нет: ').lower() == 'да':
                    phone_book.remove(element)
                    return answer

    answer = 'tru'
    return answer

def change_contact_phone_book(new_contakt: list):
    print(*new_contakt)
    update_phone_book(new_contakt)

    # elce:


