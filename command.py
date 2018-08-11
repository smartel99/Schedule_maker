import UI_String
import users


# TODO Get better cmd name
def parse_cmd(cmd):
    print("cmd: {}".format(cmd))
    if cmd[0] == "add user":
        users.add_user()
    elif cmd[0] == "show_all":
        try:
            users.list_employe(cmd[1], cmd[2])
        except IndexError:
            try:
                users.list_employe(cmd[1], False)
            except IndexError:
                users.list_employe("code", False)

    elif cmd[0] == "del_all":
        users.delete_all_employe()

    elif cmd[0] == "find":
        try:
            users.find_user(cmd[1], cmd[2].capitalize())
        except IndexError:
            print(UI_String.COMMAND_NOT_VALIDE.format(2))

    elif cmd[0] == 'x':
        exit(0)
    else:
        print(UI_String.CMD_NOT_AVAILABLE)
