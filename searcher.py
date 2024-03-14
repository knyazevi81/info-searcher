try:
    import requests
    from art import tprint
    import re
    import os
except ModuleNotFoundError:
    print('Установлены не все модули..')
    exit()


def number_hunt(nick: str):
    pass

def nick_hunt(number: str):
    pass


def main():
    os.system("cls")
    
    tprint("searcher", space=1)
    print("Выберите варинты поиска")
    print("(1) Поиск по id\n(2) Поиск по номеру")
    num = int(input("--> "))
    
    if num == 1:
        os.system("cls")
        tprint("searcher", space=1)
        nick_hunt(input("nickname -> "))
    elif num == 2:
        os.system("cls")
        tprint("searcher", space=1)
        number = re.sub("(?:)?(?:[^[0-9]*)", "", input("number  ->"))
    else:
        


if __name__ == "__main__":
    main()