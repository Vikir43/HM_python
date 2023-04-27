import text_fields as txt

def main_menu() -> int:
    print('''Главное меню:
    1. Открыть файл
    2. Сохранить контакт
    3. Показать все контакты
    4. Создать контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход ''')
    choice = ''
    while True:
        choice = input('Выберите пункт меню: ')
        if choice.isdigit() and 0 < int(choice) < 9: # choice.isdigit проверяет это цифра?
            return int(choice)
        else:
            print('Введите число от 1 до 8')

def print_info(message: str):
    print('\n' + '-'*len(message))
    print(message)
    print('-'*len(message) + '\n')


def show_contacts(book: list[dict], message: str): # book - если список придет пустой то Folse , если есть то Try
    if book:
        print('\n' + '-' * 63)
        for n, contact in enumerate(book, 1):
            print(f'{n:>3}. {contact.get("name"):<20}{contact.get("phone"):<20}{contact.get("comment"):<20}')
        print('-' * 63 + '\n') 
    else:
        print(message) 

def new_contact()-> dict:
    print()
    name = input(txt.new_name)
    phone = input(txt.new_phone)
    comment = input(txt.new_comment)
    print()
    return {'name':name, 'phone':phone, 'comment':comment}

def enter_keyword() -> str:
    print()
    key_word = input(txt.input_keyword)
    return key_word

def edit_contact(book: list, message: str) -> tuple[int, dict[str, str]]:
    index = 0
    while True:
        choice = input(message)
        if choice.isdigit() and 0 < int(choice) < len(book) + 1:
            index = int(choice)
            break
    print(txt.enter_or_empty)
    contact = new_contact()
    return index, contact

def input_index(book: list, message: str) -> int:
    while True:
        choice = input(message)
        if choice.isdigit() and 0 < int(choice) < len(book) + 1:
            return int(choice)

def confirm(messege: str) -> bool:
    print()
    answer = input(messege + ' (y/n) -> ')
    if answer.lower() == 'y':
        return True
    else:
        return False