import os
import json
import UI_String
import command
import schedule
import session
import users


def main():
    print_header()
    users.employe = users.load_employe_data()
    schedule.settings = schedule.load_json_settings()
    schedule.schedule_of_the_week = schedule.load_xls_template()
    print(users.employe)
    cmd = 'None'
    while cmd != "exit":
        cmd = input('> ').lower().strip().split(' -')
        command.parse_cmd(cmd)


def print_header():
    print(UI_String.PROGRAM_HEADER)
    print(UI_String.PROGRAM_HELP_INFO)


def get_full_path_name(file_name):
    return os.path.abspath(os.path.join('.', 'data', file_name))


if __name__ == '__main__':
    main()
