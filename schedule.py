import json
import os
import platform
import subprocess
import pyexcel

import UI_String
import schedule_maker
import users

global settings
global schedule_of_the_week
settings = {}
schedule_of_the_week = {}


def create_schedule():
    for jour in settings:
        pass


def save_json_settings():
    try:
        with open(schedule_maker.get_full_path_name("setting_for_schedule.json"), 'w', encoding='utf-8') as fout:
            fout.write(json.dumps(settings))
    except Exception as x:
        print(type(x), x)


def load_json_settings():
    r = {}
    try:
        with open(schedule_maker.get_full_path_name("setting_for_schedule.json"), 'r', encoding='utf-8') as fin:
            r = json.loads(fin.read())
    except FileNotFoundError:
        print(UI_String.SCHEDULE_COULDNT_FIND_SETTING_FILE)
    except json.decoder.JSONDecodeError:
        print(UI_String.SCHEDULE_SETTING_IS_EMPTY)
    except Exception as e:
        print("Unhandled exception:\n{}, {} ".format(type(e), e))
    finally:
        return r


def create_xls_template():
    d = {
        'Sheet 1':
            [
                ['DATE', 'Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi']
            ]
    }
    employe_sorted = users.sort_employe("poste", is_ascending=False)
    caisse = []
    cuisine = []
    respo = []
    for i, e in enumerate(employe_sorted):

        if e['poste'] == 'caisse':
            caisse.append(employe_sorted.pop(i))
        elif e['poste'] == 'cuisine':
            cuisine.append(employe_sorted.pop(i))
        elif e['poste'] == 'respo':
            respo.app

    d['Sheet 1'].append(["{} {}".format(e.get('nom'), e.get("nom de famille"))])
    try:
        pyexcel.save_book_as(bookdict=d, dest_file_name=schedule_maker.get_full_path_name("template.xls"))
    except Exception as x:
        print(UI_String.UNHANDLED_EXCEPTION.format(type(x), x))


def load_xls_template():
    try:
        raw = pyexcel.get_book_dict(file_name=schedule_maker.get_full_path_name('template.xls'), name_columns_by_row=0)
        temp = []
        for l in raw:
            pass
        return raw

    except FileNotFoundError:
        print(UI_String.SCHEDULE_TEMPLATE_NOT_FOUND)
        create_xls_template()
        load_xls_template()
    except Exception as x:
        print(type(x), x)
