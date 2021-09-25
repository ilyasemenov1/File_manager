#!/usr/bin/python3
# -*- utf-8 -*-
#pyinstaller main.py --onefile
VERSION = "13.4.1"
RELEASE_DATE = "25.09.2021"

from colorama import init
from colorama import Fore, Back, Style
import os
import shutil
import sys
import time
import textwrap
from datetime import datetime
from string import ascii_lowercase
from back.project_metods import VERSION_PROJECT
if VERSION_PROJECT == VERSION:
    from back.project_metods import Program_GUI, Sysyem_info, Copy_files, Delete_coped_files, Directory_functions, Calculator, Other
else:
    print("Program version error.")
    time.sleep(3)
    exit(0)
    os.abort()
from back.langauges.EN_en.en import en
from back.langauges.RU_ru.ru import ru
init()

class Program():
    def __init__(self, lan_p):
        
        self.lan = ''
        if lan_p == "ru":
            self.lan = ru
        if lan_p == "en":
            self.lan = en

        self.GUI = Program_GUI(self.lan)
        self.info = Sysyem_info(self.lan)
        self.copy = Copy_files(self.lan)
        self.delete = Delete_coped_files(self.lan)
        self.dir = Directory_functions(self.lan)
        self.calc = Calculator(self.lan)
        self.other = Other(self.lan)

        self.is_start = ''
        self.actions1 = ''
        self.actions2 = ''
        self.actions3 = ''
        self.actions4 = ''
        self.object = ''

    def qq_function(self):
        if __name__ == '__main__':
            self.GUI.header()
            self.is_start = input("{0}:".format(self.lan["1"]))
            if self.is_start == "y":
                self.actions_1()
            else:
                self.other.exit()

    def actions_1(self):
        if __name__ == '__main__':
            self.GUI.loading()
            while not self.actions1 == "reboot" or self.object == "break":
                self.GUI.actions()
                self.actions1 = input("{0}:".format(self.lan["8"]))
                if self.actions1 == "1":
                    self.info.folder_info()
                elif self.actions1 == "2":
                    self.info.main_info()
                elif self.actions1 == "3":
                    self.calc.calc_start()
                elif self.actions1 == "4":
                    self.actions_2()
                elif self.actions1 == "5":
                    self.actions_3()
                elif self.actions1 == "dev":
                    self.actions_4()
                elif self.actions1 == "reboot":
                    self.reboot_program()
                elif self.actions1 == "off":
                    self.other.exit()
                elif self.actions1 == "cls":
                    self.other.cls()
                    self.GUI.header()
                elif self.actions1 == "calc long":
                    self.calc.calc_long()
                else:
                    print("{0}".format(self.lan["27"]))

    def actions_2(self):
        if __name__ == '__main__':
            self.GUI.actions_2()
            self.actions2 = input("{0}:".format(self.lan["8"]))
            if self.actions2 == '1':
                self.copy.copy_in_dir()
            elif self.actions2 == "2":
                self.copy.copy_file()
            elif self.actions2 == "3":
                self.delete.delete_coped_files()
            elif self.actions2 == "cls":
                self.other.cls()
                self.GUI.header()
            elif self.actions2 == "reboot":
                self.object = "break"
                self.reboot_program()
            elif self.actions2 == "off":
                self.object = "break"
                self.other.exit()
            else:
                print("{0}".format(self.lan["27"]))

    def actions_3(self):
        if __name__ == '__main__':
            self.GUI.actions_3()
            self.actions3 = input("{0}:".format(self.lan["8"]))
            if self.actions3 == "1":
                self.dir.create_file()
            elif self.actions3 == "2":
                self.dir.delete_file()
            elif self.actions3 == "3":
                self.dir.create_directory()
            elif self.actions3 == "4":
                self.dir.find_file()
            elif self.actions3 == "cls":
                self.other.cls()
                self.GUI.header()
            elif self.actions3 == "reboot":
                self.object = "break"
                self.reboot_program()
            elif self.actions3 == "off":
                self.object = "break"
                self.other.exit()
            else:
                print("{0}".format(self.lan["27"]))

    def actions_4(self):
        if __name__ == '__main__':
            self.GUI.actions_4()
            self.actions4 = input("{0}:".format(self.lan["8"]))
            if self.actions4 == "1":
                self.other.print_language_frases()
            elif self.actions4 == "2":
                self.other.path_python()
            elif self.actions4 == "3":
                self.other.debug()
            elif self.actions4 == "cls":
                self.other.cls()
                self.GUI.header()
            elif self.actions4 == "reboot":
                self.object = "break"
                self.reboot_program()
            elif self.actions4 == "off":
                self.other.exit()
            else:
                print("{0}".format(self.lan["27"]))
            
    def reboot_program(self):
        self.GUI.reboot_animation()
        lan_choose = input("[RU/EN]:")
        if lan_choose == "RU":
            if __name__ == "__main__":
                Program("ru").qq_function()
        elif lan_choose == "EN":
            if __name__ == "__main__":
                Program("en").qq_function()
        else:
            self.other.exit()

lan_choose = input("[RU/EN]:")
if lan_choose == "RU":
    if __name__ == "__main__":
        Program("ru").qq_function()
elif lan_choose == "EN":
    if __name__ == "__main__":
        Program("en").qq_function()
else:
    print("\033[2J")
    exit(0)
    os.abort()
