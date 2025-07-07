import re


def validate_phone(phone: str) -> str:
    """
    Проверка соответствия формата номера телефона (+7XXXXXXXXXX или 8XXXXXXXXXX)

    Args:
        phone (str): номер телефона

    Returns:
        phone (str): номер телефона в необходимом формате
    """
    exc = (
        "Ошибка ввода, проверьте правильность введенных данных.\n"
        "Номер телефона должен соответствовать формату: +7XXXXXXXXXX или 8XXXXXXXXXX"
    )

    if phone.startswith("7"):
        phone = "".join(["+", phone])
    if not (phone.startswith("+") or phone.startswith("8")):
        print(exc)
        phone = validate_phone(input("Введите номер телефона: "))

    for symbol in phone:
        if symbol.isalpha():
            print(exc)
            phone = validate_phone(input("Введите номер телефона: "))
            break

    # if len(re.sub(r"\D", "", phone)) != 11:
    #     print(exc)
    #     phone = validate_phone(input("Введите номер телефона: "))

    return phone


def validate_ogrnip(ogrnip: str) -> str:
    """Проверяет, что ОГРНИП содержит 15 цифр и возвращает в нужном формате"""
    for elem in ogrnip:
        if not elem.isdigit():
            print(
                "Ошибка ввода, проверьте правильность введенных данных.\n"
                "ОГРНИП должен содержать 15 цифр"
            )
            ogrnip = validate_ogrnip("Введите ОГРНИП: ")
            break

    return ogrnip
