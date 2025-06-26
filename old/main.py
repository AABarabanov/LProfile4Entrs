# MyProfile app

separator = "------------------------------------------"

# user profile
name = ""
age = 0
phone = ""
email = ""
additional_information = ""
postal_code = ""
postal_address = ""
# businesman profile
ogrnip = 0
inn = 0
payment_account = 0
bank = ""
bik = 0
correspondent_account = 0


# technical
def digits_counter_check(parameter, number, check):
    counter = 0
    while number != 0:
        counter += 1
        number //= 10
    if counter != check:
        return print(parameter, "должен содержать", check, "цифр")
    return counter


# data
def general_info_output(name, age, phone, email, additional_information):
    print(separator)
    print("Имя:    ", name)
    if 11 <= age % 100 <= 19:
        years_parameter = "лет"
    elif age % 10 == 1:
        years_parameter = "год"
    elif 2 <= age % 10 <= 4:
        years_parameter = "года"
    else:
        years_parameter = "лет"

    print("Возраст:", age, years_parameter)
    print("Телефон:", phone)
    print("E-mail: ", email)
    print("Индекс:", postal_code)
    print("Адрес:", postal_address)
    if additional_information:
        print("")
        print("Дополнительная информация:")
        print(additional_information)


def businessman_info_output():
    print("\nИнформация о предпринимателе")
    print("ОГРНИП: ", ogrnip)
    print("ИНН:    ", inn)
    print("Банковские реквизиты")
    print("Р/c:    ", payment_account)
    print("Банк:   ", bank)
    print("БИК     ", bik)
    print("К/c:    ", correspondent_account)


print("Приложение MyProfile")
print("Сохраняй информацию о себе и выводи ее в разных форматах")

while True:
    # main menu
    print(separator)
    print("ГЛАВНОЕ МЕНЮ")
    print("1 - Ввести или обновить информацию")
    print("2 - Вывести информацию")
    print("0 - Завершить работу")

    option = int(input("Введите номер пункта меню: "))
    if option == 0:
        break

    if option == 1:
        # submenu 1: edit info
        while True:
            print(separator)
            print("ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ")
            print("1 - Личная информация")
            print("2 - Информация о предпринимателе")
            print("0 - Назад")

            edit_menu_option = int(input("Введите номер пункта меню: "))
            if edit_menu_option == 0:
                break
            elif edit_menu_option == 1:
                # input general info
                name = input("Введите имя: ")
                while 1:
                    # validate user age
                    age = int(input("Введите возраст: "))
                    if age > 0:
                        break
                    print("Возраст должен быть положительным")

                phone = input("Введите номер телефона (+7ХХХХХХХХХХ): ")
                country_code = "+7"
                symbol_counter = 0
                for symbol in phone:
                    symbol_counter += 1
                if symbol_counter == 10:
                    phone = country_code + phone

                email = input("Введите адрес электронной почты: ")

                postal_code = input("Введите почтовый индекс: ")
                postal_code = int("".join(filter(str.isdigit, postal_code)))

                postal_address = input("Введите почтовый адрес (без индекса): ")
                additional_information = input("Введите дополнительную информацию:\n")
            elif edit_menu_option == 2:

                # enter OGRNIP with check (15 digits)
                counter = 0
                check = 15
                while counter != check:
                    ogrnip = int(input("Введите ОГРНИП: "))
                    parameter = "ОГРНИП"
                    counter = digits_counter_check(parameter, ogrnip, check)

                inn = int(input("Введите ИНН: "))

                # enter Payment Account with check (20 digits)
                counter = 0
                check = 20
                while counter != check:
                    payment_account = int(input("Введите расчётный счёт: "))
                    parameter = "Расчётный счёт"
                    counter = digits_counter_check(parameter, payment_account, check)

                bank = input("введите название банка: ")
                bik = int(input("Введите БИК: "))
                correspondent_account = int(input("Введите корреспондентский счёт: "))

            else:
                print("Введите корректный пункт меню")
    elif option == 2:
        # submenu 2: print info
        while True:
            print(separator)
            print("ВЫВЕСТИ ИНФОРМАЦИЮ")
            print("1 - Общая информация")
            print("2 - Вся информация")
            print("0 - Назад")

            option = int(input("Введите номер пункта меню: "))
            if option == 0:
                break
            if option == 1:
                general_info_output(name, age, phone, email, additional_information)
            elif option == 2:
                general_info_output(name, age, phone, email, additional_information)
                businessman_info_output()
            else:
                print("Введите корректный пункт меню")
    else:
        print("Введите корректный пункт меню")
