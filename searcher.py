try:
    import requests
    from art import tprint
    from time import sleep
    import requests
    import re
    import os
    import phonenumbers
    from phonenumbers import carrier
    from phonenumbers import geocoder
    from phonenumbers import timezone
    import json
    import os
    from tqdm import tqdm
except ModuleNotFoundError:
    print('Установлены не все модули..')
    exit()


def number_hunt(number: str):
    pass

def nick_hunt(nick: str):
    with open("resourses/data.json", "r", encoding="utf-8") as data_file:
        data = json.load(data_file)

    base_data: dict() = {}

    social_networks = sorted(data.items())

    for site in tqdm(social_networks):
        site_name: str = site[0]
        site_url = site[1]["url"]
        site_status = site[1]["errorType"]

        target_url = site_url.replace("{}", nick)

        try:
            status = requests.get(target_url, timeout=5)
        except:
            pass

        if status.status_code == 200 and site_status == "status_code":
            base_data[site_name] = target_url
        
    print(base_data)


def main():
    os.system("cls")
    
    tprint("searcher", space=1)
    print("Выберите варинты поиска")
    print("(1) Поиск по nick\n(2) Поиск по номеру\n(3) Выход")
    num = int(input("--> "))
    
    if num == 1:
        os.system("cls")
        tprint("searcher", space=1)
        nick = str(input("nickname -> "))
        nick_hunt(nick)
    elif num == 2:
        os.system("cls")
        tprint("searcher", space=1)
        try:
            phone = re.sub("(?:\+)?(?:[^[0-9]*)", "", input("number ->"))
            PhoneNumberObject = phone

            #+792579ххххх
            #Country Code: 7 National Number: 92579ххххх
            #+7 925 79х-хх-хх
        
            FormattedPhoneNumber = "+" + phone
            PhoneNumberObject = phonenumbers.parse(FormattedPhoneNumber, None)
            #local_international_format = phonenumbers.format_number(PhoneNumberObject, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            print(1)
        except:
            print('\033[1m\033[31mНомер телефона введён неверно!\033[0m')
            sleep(2)
            main()
    elif num == 3:
        exit()
    else:
        os.system("cls")
        tprint("searcher", space=1)
        print("невернно ведены данные")
        sleep(2)
        main()

       
if __name__ == "__main__":
    main()