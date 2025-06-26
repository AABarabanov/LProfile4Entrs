from models import UserProfile, BusinessProfile
from utils import validate_phone, validate_ogrnip


def greetings():
    print("┌─────────────────────────────┐")
    print("│                             │")
    print("│         LehaProfile         │")
    print("│     (for Entrepreneurs)     │")
    print("│           • 1.0 •           │")
    print("|                             |")
    print("└─────────────────────────────┘\n")


def main():
    user = UserProfile()
    business = BusinessProfile()

    user.name = input("Введите имя: ")
    user.phone = validate_phone(input("Введите номер телефона: "))
    business.ogrnip = validate_ogrnip(input("Введите ОГРНИП: "))

    print(f"Профиль: {user.name}, тел.: {user.phone}")
    print(f"ОГРНИП: {business.ogrnip}")


if __name__ == "__main__":
    greetings()
    main()
