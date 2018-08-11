import datetime

import UI_String
import schedule_maker
import json

# TODO Make custom Poste/Formation from user to personalize
global employe
employe = []


def save_employe_data():
    path = schedule_maker.get_full_path_name("employe.json")
    with open(path, "w", encoding="utf-8") as fout:
        # TODO Format json before/while dumping it
        fout.write(json.dumps(employe, indent=4))
        print(UI_String.DATA_EMPLOYE_SAVED)


def load_employe_data():
    path = schedule_maker.get_full_path_name("employe.json")
    try:
        with open(path, "r", encoding="utf-8") as fin:
            try:  # Essaie de loader le fichier
                de_data = json.loads(fin.read())
                return de_data
            except json.decoder.JSONDecodeError:  # Si le fichier est vide
                return []
    except FileNotFoundError:
        save_employe_data()
        return load_employe_data()


def is_code_already_assigned(code):
    for e in employe:
        if e["code"] == code:
            return True
    return False


def get_code():
    while True:
        code = input(UI_String.USERS_GET_CODE).upper().strip(' ')
        if code == "INFO":
            print(UI_String.USERS_CODE_INFO)
            continue
        if not code.isdecimal or code.__len__() != 4:
            print(UI_String.USERS_CODE_NOT_GOOD)
            continue

        if is_code_already_assigned(code):
            continue
        return code


def get_name():
    while True:
        name = input(UI_String.USERS_GET_NAME).capitalize().strip(' ')
        if name == "Info":
            print(UI_String.USERS_NAME_INFO)
            continue
        if not name.isalpha():
            if name.find('-') == -1:
                print(UI_String.USERS_NAME_NOT_GOOD)
                continue
        return name


def get_surname():
    while True:
        name = input(UI_String.USERS_GET_SURNAME).capitalize().strip(' ')
        if name == "Info":
            print(UI_String.USERS_SURNAME_INFO)
            continue
        if not name.isalpha():
            if name.find('-') == -1:
                print(UI_String.USERS_NAME_NOT_GOOD)
                continue
        return name


def get_pin():
    while True:
        pin = input(UI_String.USERS_GET_PIN).strip().upper()
        if pin == 'INFO':
            print(UI_String.USERS_PIN_INFO)
            continue
        if not pin or pin.__len__() != 5 or not pin.isdecimal():
            print(UI_String.USERS_PIN_NOT_GOOD)
            continue
        return pin


def get_poste():
    while True:
        poste = input(UI_String.USERS_GET_POSTE).lower().strip(' ')
        if poste == "info":
            print(UI_String.USERS_POSTE_INFO)
            continue
        if poste != "cuisine" and poste != "caisse" and poste != "responsable":
            print(UI_String.USERS_POSTE_NOT_GOOD)
            continue
        return poste


def is_formation_cuisine_good(f):
    if f == "frite":
        return True
    elif f == "panier":
        return True
    elif f == "sauce":
        return True
    elif f == "fromage":
        return True
    elif f == "panne":
        return True
    elif f == "table":
        return True
    elif f == "1":
        return True
    elif f == "pizza":
        return True
    elif f == "sortie":
        return True
    elif f == "étirage":
        return True
    else:
        return False


def is_formation_caisse_good(f):
    if f == "base":
        return True
    elif f == "call":
        return True
    elif f == "dispatch":
        return True
    else:
        return False


def is_formation_respo_good(f):
    # TODO Learn possibilities for respo
    if f.isalpha():
        return True
    else:
        return False


def get_formation(poste):
    should_stop = False
    while not should_stop:
        formation = input(UI_String.USERS_GET_FORMATION).lower().split(", ")
        if formation == "info":
            print(UI_String.USER_FORMATION_INFO)
            continue

        should_stop = True
        for f in formation:
            if poste == "cuisine":
                if not is_formation_cuisine_good(f):
                    print(UI_String.USERS_FORMATION_NOT_GOOD)
                    should_stop = False
                    break
            elif poste == "caisse":
                if not is_formation_caisse_good(f):
                    print(UI_String.USERS_FORMATION_NOT_GOOD)
                    should_stop = False
                    break
            elif poste == "responsable":
                if not is_formation_respo_good(f):
                    print(UI_String.USERS_FORMATION_NOT_GOOD)
                    should_stop = False
                    break
    return formation


def get_date():
    while True:
        bday = input(UI_String.USERS_GET_DATE).strip(' ').lower()
        if bday == "info":
            print(UI_String.USERS_DATE_INFO)
            continue
        try:
            day, month, year = bday.split('/')
        except ValueError:
            print(UI_String.USERS_DATE_NOT_GOOD)
            continue
        try:
            d = datetime.date(day=int(day), month=int(month), year=int(year))
        except ValueError:
            print(UI_String.USERS_DATE_NOT_VALID)
            continue
        if d > datetime.date.today():
            print(UI_String.USERS_DATE_IN_THE_FUTURE)
            continue
        return bday


def get_salary():
    while True:
        s = input(UI_String.USERS_GET_SALARY).lower().strip()
        if s == "info":
            print(UI_String.USERS_SALARY_INFO)
            continue
        if not s.isdecimal():
            if s.find('.') != -1:
                t = s.split('.')
                v = t[0] + t[1]
                if not v.isdecimal():
                    print(UI_String.USERS_SALARY_NOT_GOOD)
                    continue
            else:
                print(UI_String.USERS_SALARY_NOT_GOOD)
                continue
        try:
            salary = float(s)
        except ValueError:
            print(UI_String.USERS_SALARY_NOT_GOOD)
            continue
        if salary < 11.25:  # TODO Maybe get minimum wage from internet?
            print(UI_String.USERS_SALARY_BELLOW_MINIMUM)
            continue
        return s


def is_dispo_good(q):  # TODO Make personalization of quarters available
    if q != "ND" and q != "OUI" and q != "MATIN" and q != "MIDI" and q != "SOIR" and q != "CLOSE" and q != "JOURNÉE":
        return False
    return True


def get_dispo():
    dispo = {"lundis": 'ND', "mardis": 'ND', "mercredis": 'ND', "jeudis": 'ND', "vendredis": 'ND',
             "samedis": 'ND', "dimanches": 'ND'}
    should_return = False
    while True:
        for d in dispo:  # TODO restart the current loop if input is bad instead of having to restart
            should_return = False
            quart = input(UI_String.USERS_GET_DISPO.format(d)).upper().strip(" ")
            if quart == "INFO":
                print(UI_String.USERS_DISPO_INFO)
                break
            quarts = quart.split(', ')
            for q in quarts:
                if not is_dispo_good(q):
                    print(UI_String.USERS_DISPO_NOT_GOOD)
                    break
            dispo[d] = quarts
            should_return = True
        if should_return:
            return dispo


def get_priority():
    while True:
        p = input(UI_String.USERS_GET_PRIORITY).lower().strip(' ')
        if p == 'info':
            print(UI_String.USERS_PRIORITY_INFO)
            continue
        if not p.isdigit():
            print(UI_String.USERS_PRIORITY_NOT_GOOD)
            continue
        priority = int(p)
        if priority < 0 or priority > 10:
            print(UI_String.USERS_PRIORITY_NOT_GOOD)
            continue
        return priority


def is_info_good(user):
    print(UI_String.USERS_CREATION_VERIFICATION)
    print()
    for k in user:
        print("{}: {}".format(k, user[k]))
    while True:
        resp = input(UI_String.USERS_IS_INFO_GOOD).strip().lower()
        if resp == "oui":
            return user
        else:
            try:
                user[resp] = resp  # Verify if field exists
            except KeyError:
                print(UI_String.USERS_FIELD_NOT_EXIST)
                continue
            return user


def get_date_difference(h_date):
    day, month, year = h_date.split('/')
    th_date = datetime.date(day=int(day), month=int(month), year=int(year))
    delta = datetime.date.today() - th_date
    print(delta.days)
    return delta.days


def add_user():
    print()
    print(UI_String.USERS_CREATION_HEADER)
    user = {"nom": get_name(),
            "nom de famille": get_surname(),
            "code": get_code(),
            'nip': get_pin(),
            "poste": get_poste(),
            "date d'embauche": get_date(),
            "salaire": get_salary(),
            "disponibilitée": get_dispo(),
            "priorité": get_priority()}  # TODO find a proper/better name instead of priority

    user["formation"] = get_formation(user["poste"])
    user["ancienneté"] = get_date_difference(user["date d'embauche"])
    user = is_info_good(user)
    employe.append(user)
    save_employe_data()


def sort_employe(filtre, is_ascending):
    try:
        return sorted(employe, key=lambda k: k[filtre], reverse=bool(is_ascending))
    except KeyError:
        raise KeyError


def list_employe(filtre, is_ascending):
    try:
        temp = sort_employe(filtre, is_ascending)
    except KeyError:
        print("UI_String.USERS_FILTER_NOT_GOOD")
        return
    if not employe:
        print(UI_String.USERS_NO_DATA)
    for e in temp:
        print("---------------")
        for f in e:
            print("{}: {}".format(f, e[f]))
        print("---------------")
        print()


def delete_all_employe():
    print(UI_String.USERS_ABOUT_TO_DELETE_ALL.format(employe.__len__()))
    if input(UI_String.USERS_CONFIRMATION_DELETE).strip().lower() == 'o':
        employe.clear()
        print(employe)
        print(UI_String.USER_DATA_DELETED)
        save_employe_data()


def print_user(e):
    print("----------")
    for f in e:
        print("{}: {}".format(f, e[f]))
    print("----------")


def find_user(key, value):
    matches = []
    for e in employe:
        try:
            if e[key] == value:
                matches.append(e)
        except KeyError:
            print(UI_String.USERS_FIELD_INVALID.format(key))
            return
    if not matches:
        print(UI_String.USERS_NOT_FOUND)
    else:
        print(UI_String.USERS_FOUND)
        for e in matches:
            print_user(e)
