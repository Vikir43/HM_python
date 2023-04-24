
def main_menu():
    print("Main menu")
    print("1. Просмотреть контакты")
    print("2. Создать новый контакт")
    print("3. Изменить контакт")
    print("4. Найти контакта")
    print("5. Удалить контакт")
    print("6. Выход")

def find_contact():
    find_string = input('Введите поисковый запрос')
    file = open('Phonebook\phonebook.txt', 'r', encoding='UTF-8')
    data = file.readlines()    
    for index, data_str in enumerate(data):
        if find_string in data_str:
            print('Результат поиска =  ', data_str)
    
def delet_contact():
    with open('Phonebook\phonebook.txt', 'r', encoding='UTF-8') as file:
        old_data = file.read()    
        new_data = old_data.replace('Петров', '')
    with open('Phonebook\phonebook.txt', 'w', encoding='UTF-8') as file:
       file.write(new_data)

def edit_contact():    
    with open('Phonebook\phonebook.txt', 'r', encoding='UTF-8') as file:
        old_data = file.read()    
        new_data = old_data.replace('Панфилов', 'Гусев')
    with open('Phonebook\phonebook.txt', 'w', encoding='UTF-8') as file:
       file.write(new_data)
    
    # old = input('Введите данные для изменения: ')
    # new= input('Введите новые данные: ')
    # file = open('Phonebook\phonebook.txt', 'r', encoding='UTF-8')
    # data = file.read() 
    # new_data = []
    # for  data_str in data:
    #     if old in data_str:
    #         new_data.append(new)
    #     else:
    #         new_data.append(old)
    # with open('Phonebook\phonebook.txt', 'w', encoding='UTF-8') as file:
    #     file.write([new_data])
                 
        
def show_all():
    file = open('Phonebook\phonebook.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    #print(data)
    file.close
    for i in data:
        print(i)

def add_contact():
    file = open('Phonebook\phonebook.txt', 'a', encoding='UTF-8')
    data = input('Введите фамилию, телефон, комментарий (разделяя ;)')
    data += '\n'
    file.write(data)
    file.close
    #print('input data', data)

if __name__ == "__main__":
    main_menu()
    
    while True:
        choose = int(input("Введите пункт меню: "))
        if choose == 1:
           show_all()
        if choose == 2:
           add_contact()
        if choose == 3:
           edit_contact()   
        if choose == 4:
           find_contact() 
        if choose == 5:
           delet_contact()  
        if choose == 6:
            main_menu()