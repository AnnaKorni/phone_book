# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных

filename = "phone.txt"

def work_with_phonebook(filename):
	
    choice=show_menu()
    phone_book=read_txt(filename)


    while (choice!=7):

        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('lastname ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            number=input('number ')
            print(find_by_number(phone_book,number))
        elif choice==4:
            last_name=input('lastname ')
            new_number=input('new  number ')
            print(change_number(phone_book,last_name,new_number))
            
        elif choice==5:
            lastname=input('Удалить абонента: ')
            print(delete_by_lastname(phone_book,lastname))
        elif choice==6:
            user_data=input('Введите данные нового абонента в формате: Фамилия, Имя, Телефон, Описание:')
            add_user(phone_book,user_data)
            write_txt(filename,phone_book)


        choice=show_menu()


def show_menu():
    print(
        "\nВыберите необходимое действие:\n",
        "1. Отобразить весь справочник\n",
        "2. Найти абонента по фамилии\n",
        "3. Найти абонента по номеру телефона\n",
        "4. Изменить телефон\n",
        "5. Удалить запись\n",
        "6. Добавить запись и сохранить справочник в текстовом формате")
    choice = int(input())
    return choice


def read_txt(filename): 
    phone_book=[]
    fields=["Фамилия","Имя","Телефон","Описание"]
    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
			#dict(( (фамилия,Иванов),(имя, Точка),(номер,8928) ))	
            phone_book.append(record)	
    return phone_book

def print_result(phone_book):
    print('Фамилия ','Имя ','Телефон ','Описание ')
    i = 0
    for line in phone_book:
        i=i+1
        print(i, line['Фамилия'], line['Имя'], line['Телефон'], line['Описание'])

def find_by_lastname(phone_book, last_name):
    for i in range(len(phone_book)):
        if phone_book[i]['Фамилия'] == last_name:
            return phone_book[i]
    return "не найдено"
    
def find_by_number(phone_book, number):
    for i in range(len(phone_book)):
        if phone_book[i]['Телефон'] == number:
            return phone_book[i]
    return "не найдено"


def change_number(phone_book,last_name,new_number):
    for i in range(len(phone_book)):
        if phone_book[i]['Фамилия'] == last_name:
            phone_book[i]['Телефон'] = new_number
            return phone_book[i]
    return "Абонент не найден"

def delete_by_lastname(phone_book,lastname):
    for i in range(len(phone_book)):
        if phone_book[i]['Фамилия'] == lastname:
            del phone_book[i]
            return phone_book
    return "Абонент не найден"


def add_user(phone_book,user_data):
    list = user_data.split(',')
    list = [line.strip() for line in list]
    print(f"\n Добавим запись: {list}")
    if len(list)!=4:
        return "Ввеедены не все данные"
    new_list = dict(zip(['Фамилия','Имя','Телефон','Описание'], list))
    return print(phone_book.append(new_list))

def write_txt(filename , phone_book):
    with open(filename,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')

    
work_with_phonebook(filename)
