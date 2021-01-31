from os import system, name
import platform
import users
import time
import connect


def call_menu():
    print("================WELCOME TO CHAT===================")

    print(">_ If you are new, type '$reg' to register")
    print(">_ If you already registered, type '$log' to login")
    print("--------------------------------------------------")
    command = input(">_ ")
    return command


# função para limpar o terminal a depender de qual for o OS usado
def clear():
    if platform.system() == "Windows":
        system('cls')
    elif platform.system() == "Linux":
        system('clear')


# def search_user(usr):
#     for user in users.db:
#         if user == usr:
#             print('[ERROR] username already taken')


def register():
    print("===================REGISTER======================")
    usr = input("[choose username]: ")
    connect.register_user(usr, '123') ######################### melhorar depois
    # if users.db.get(usr):
    #     clear()
    #     print("===================REGISTER======================")
    #     print('[SYSTEM] username already taken... try another')
    #     time.sleep(2)
    # else:
    #     input("[choose password]: ")
    # connect.register_user(usr, input("[choose password]: "))


def login():

    print("=====================LOGIN=======================")
    usr = input("[enter username]: ")
    psw = input("[enter password]: ")
    if connect.check_user(usr) and connect.check_pass(usr, psw):
        clear()
        print("=====================LOGIN=======================")
        print('[SYSTEM] Logged in')
    else:
        clear()
        print("=====================LOGIN=======================")
        print('[SYSTEM] Invalid credentials.')
        time.sleep(2)
        login()


proceed = False
while not proceed:

    returned = call_menu()
    if returned == '$reg':
        proceed = True
        clear()
        register()
    elif returned == '$log':
        clear()
        login()
        proceed = True
    else:
        clear()
        print('!!!!!!!!!!!!!!!!Invalid command!!!!!!!!!!!!!!!!!!')
        print("")