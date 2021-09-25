from colorama import init
from colorama import Fore, Back, Style
import os
import shutil
import sys
import time
from datetime import datetime


def wait():
    time.sleep(.05)

VERSION_PROJECT = "13.4.1"
RELEASE_DATE = '25.09.2021'

class Program_functions(object):
    def __init__(self, lan_p
        ):
        self.lan = lan_p
        self.long = "________________________________________________________________________________"
        self.deleted_file_list = []
        self.file_list_for_count = []
        self.full_name = ''
        self.new_file = ''
        self.dir_name = ''
        self.dir_name_2 = ''
        self.file_list = []
        self.file_name = ''
        self.count_index = 0
        self.index = 0
        self.index_2 = 0
        self.index_3 = 0
        self.index_4 = 0
        self.white = "\033[37m{}\033[0m"
        self.yellow = "\033[33m{}\033[0m"
        self.tag = "\033[32m{}\033[0m"
        self.green = "\033[32m{}\033[0m"
        self.cyan = "\033[36m{}"
        self.cyan_short = "\033[36m{}\033[0m"
        self.lightred = "\033[91m"
        self.lightgreen = "\033[92m"
        self.h3 = []
        self.coped_file_list = []
        self.progress_bar = [
            " [##   ]",
            " [ ##  ]",
            " [  ## ]",
            " [   ##]",
            " [#   #]"
            ]
        self.progress_bar_2 = [
            "[----------]",
            "[          ]",
            "[#         ]",
            "[##        ]",
            "[###       ]",
            "[####      ]",
            "[#####     ]",
            "[######    ]",
            "[#######   ]",
            "[########  ]",
            "[######### ]",
            "[##########]"
        ]
            
    def dir_name_input_to(self, input_text=None):
        if input_text:
            self.dir_name = input(input_text)
        else:
            self.dir_name = input("{0}:".format(self.lan["53"]))
        if self.dir_name == '*':
            self.dir_name = os.getcwd()
            return True
        elif '*>' in self.dir_name:
            dir_name = os.getcwd()
            after_this = self.dir_name.partition('>')[-1]
            if after_this == '':
                self.dir_name = dir_name
                return True
            else:
                self.dir_name = os.path.join(dir_name, after_this)
                if os.path.exists(self.dir_name):
                    return True
                else:
                    print("Директория \"{0}\" не найдена.".format(self.dir_name))
                    return False
        else:
            if os.path.exists(self.dir_name):
                if not self.dir_name == '':
                    return True
            else:
                print("Директория \"{0}\" не найдена.".format(self.dir_name))
                return False

    def dir_name_input_out(self, input_text=None):
        if input_text:
            self.dir_name_2 = input(input_text)
        else:
            self.dir_name_2 = input("{0}:".format(self.lan["53"]))
        if self.dir_name_2 == '*':
            self.dir_name_2 = os.getcwd()
            return True
        elif '*>' in self.dir_name_2:
            dir_name = os.getcwd()
            after_this = self.dir_name_2.partition('>')[-1]
            if after_this == '':
                self.dir_name_2 = dir_name
                return True
            else:
                self.dir_name_2 = os.path.join(dir_name, after_this)
                if os.path.exists(self.dir_name_2):
                    return True
                else:
                    print("Директория \"{0}\" не найдена.".format(self.dir_name_2))
                    return False
        else:
            if os.path.exists(self.dir_name_2):
                if not self.dir_name_2 == '':
                    return True
            else:
                print("Директория \"{0}\" не найдена.".format(self.dir_name_2))
                return False

    def file_info_form(self, tag):
        print(self.tag .format("{0}:".format(tag)))
        if self.dir_name_input_to():
            self.file_list = os.listdir(self.dir_name)
            self.file_name = input(self.lan["80"])
            self.full_name = os.path.join(self.dir_name, self.file_name)


    def file_list_for_count_(self):
        count_index = 0
        for self.file_name in self.file_list:
            self.full_name = os.path.join(self.dir_name, self.file_name)
            if os.path.isfile(self.full_name):
                if not "_copy_" in self.file_name:
                    count_index += 1
        return count_index


    def print_progress(self, text_content, index_1, index_2, index_3):
        if self.index < index_1 and self.index >= index_2:
            print("{0}: {1}% ({2}/{3}) {4}       \r".format(text_content, self.index, self.index_2, self.index_3, self.progress_bar_2[index_3]), end='')

    def progress_animation(self, text_content):
        self.print_progress(text_content, 1, 0, 0)
        self.print_progress(text_content, 10, 0, 1)
        self.print_progress(text_content, 20, 10, 2)
        self.print_progress(text_content, 30, 20, 3)
        self.print_progress(text_content, 40, 30, 4)
        self.print_progress(text_content, 50, 40, 5)
        self.print_progress(text_content, 60, 50, 6)
        self.print_progress(text_content, 70, 60, 7)
        self.print_progress(text_content, 80, 70, 8)
        self.print_progress(text_content, 90, 80, 9)
        self.print_progress(text_content, 100, 90, 10)

class Program_GUI(Program_functions):

    def __init__(self, lan_p
        ):
        super().__init__(lan_p
                )

    def header(self):
        print("\033[2J")
        print(
            "v: {0}  {1}: {2}  {3}: {4}".format(
                self.green.format("13.4.1"),
                self.lan["47"],
                self.cyan_short.format("25.09.21"),
                self.lan["48"],
                self.yellow.format(self.lan["26"])
            )
        )
        print(self.long)
        wait()
       
    def loading(self):
        wait()
        print("[ 20% ] ")
        wait()
        print("[ 40% ]")
        wait()
        print("[ 60% ]")
        wait()
        print("[ 80% ]")
        wait()
        print("[ 100% ]")
        wait()
        print("{0}:".format(self.lan["2"]))
        time.sleep(0.5)
        print(self.long)
        time.sleep(0.1)

    def actions(self):
        print(self.tag.format("{0}:".format(self.lan["3"])))
        print(" [1] {0}".format(self.lan["4"]))
        wait()
        print(" [2] {0}".format(self.lan["5"]))
        wait()
        print(" [3] {0}".format(self.lan["6"]))
        wait()
        print(" [4] {0}".format(self.lan["7"]))
        wait()
        print(" [5] {0}".format(self.lan["74"]))
        wait()

    def actions_2(self):
        print(self.tag.format("{0}:".format(self.lan["49"])))
        print(" [1] {0}".format(self.lan["55"]))
        wait()
        print(" [2] {0}".format(self.lan["12"]))
        wait()
        print(" [3] {0}".format(self.lan["52"]))

    def actions_3(self):
        print(self.tag.format("{0}:".format(self.lan["74"])))
        wait()
        print(" [1] {0}".format(self.lan["56"]))
        wait()
        print(" [2] {0}".format(self.lan["72"]))
        wait()
        print(" [3] {0}".format(self.lan["67"]))
        wait()
        print(" [4] {0}".format(self.lan["78"]))

    def actions_4(self):
        wait()
        print(self.tag.format("{0}:".format(self.lan["37"])))
        wait()
        print(" [1] {0}".format(self.lan["38"]))
        wait()
        print(" [2] {0}".format(self.lan["30"]))
        wait()
        print(" [3] {0}".format("Debug"))

    def print_animation(self, index):
        print(self.white.format("{0} {1}    \r".format(self.lan["24"], self.progress_bar[index])), end='')
        time.sleep(.4)

    def reboot_animation(self):
        print("\033[2J")
        x = 0
        for y in range(9):
            if x > 4:
                x = 0
            self.print_animation(x)
            x += 1
        time.sleep(.1)
        print("\033[2J")


class Sysyem_info(Program_functions):

    def __init__(self, lan_p):
        self.files = []
        self.folders = []
        self.count_files = 0
        self.count_folders = 0
        self.tag_1 = ''
        self.tag_2 = ''
        self._os_ = ''
        super().__init__(lan_p)

    def print_name_list(self, file_list):
        for name in file_list:
            wait()
            print(self.yellow.format(" " + name))

    def search_information(self):
        if self.dir_name_input_to():
            self.file_list = os.listdir(self.dir_name)
            for self.file_name in self.file_list:
                self.full_name = os.path.join(self.dir_name, self.file_name)
                if os.path.isfile(self.full_name):
                    if self.count_files <= 50:
                        self.files.append(self.file_name)
                    self.count_files += 1
                else:
                    if self.count_folders <= 50:
                        self.folders.append(self.file_name)
                    self.count_folders += 1
            return True
        else:
            return False

    def folder_info(self):
        self.files = []
        self.folders = []
        self.count_files = 0
        self.count_folders = 0
        self.tag_1 = ''
        self.tag_2 = ''
        wait()
        print(self.tag .format("{0}:".format(self.lan["65"])))
        try:
            if self.search_information():
                if self.count_files == 0:
                    pass
                elif self.count_files == 1:
                    self.tag_1 = "{0}:".format(self.lan["86"])
                else:
                    self.tag_1 = "{0}:".format(self.lan["87"])

                if self.count_folders == 0:
                    pass
                elif self.count_folders == 1:
                    self.tag_2 = "{0}:".format(self.lan["88"])
                else:
                    self.tag_2 = "{0}:".format(self.lan["89"])

                if not self.count_files > 50 or self.count_files == 0:
                    print(self.tag_1)
                    self.print_name_list(self.files)
                if not self.count_folders > 50 or self.count_folders == 0:
                    print(self.tag_2)
                    self.print_name_list(self.folders)
                wait()
                print("{0}: {1}".format(self.lan["84"], self.count_files))
                wait()
                print("{0}: {1}".format(self.lan["85"], self.count_folders))
                wait()
                print("{0}: {1}".format(self.lan["62"], (self.count_files + self.count_folders)))
        except FileNotFoundError:
            print(self.lan["57"])
        except OSError:
            print(self.lan["57"])

    def c_info(self):
        print(self.tag .format("{0}:".format(self.lan["23"])))
        self.dir_name = os.getcwd()
        print("{0}: {1}".format(self.lan["18"], self.yellow.format(self.dir_name)))
        print("{0}: {1}".format(self.lan["19"], self.cyan_short.format(os.getlogin())))

        self._os_ = str(sys.platform)

        if self._os_ == "win32":
            self._os_ = "Windows"
        elif self._os_ == "linux":
            pass
        elif self._os_ == "darwin":
            os_ = "Mac OS"
        elif self._os_ == "cygwin":
            self._os_ = "Windows Cygwin"
        elif self._os_ == "os2":
            self._os_ = 'OS/2'
        elif self._os_ == "os2emx":
            self._os_ = "OS/2 EMX"

        print("{0}: {1}".format(self.lan["20"], self.cyan_short.format(self._os_)))
        print("{0}: {1}".format(self.lan["21"], self.yellow.format(sys.getfilesystemencoding())))


class Copy_files(Program_functions):

    def __init__(self, lan_p):
        self.full_name_2 = ''
        self.file_dict = {}
        self.format_list = []
        self.coped_file_index = []
        self.name_list = []
        self.not_coped_file_list = []
        super().__init__(lan_p)

    def copy(self):
        if os.path.isfile(self.full_name):
            if '_copy_' in self.file_name:
                format_name = self.file_name.partition(".")[-1]
                file_name = self.file_name.partition(".")[-3]
                coped_file_index = file_name.partition('_copy_')[-1]
                name = file_name.partition('_copy_')[-3]
                coped_name = name + '_copy_'
                coped_file_index = int(coped_file_index) + 1
                new_file_name = coped_name + str(coped_file_index)
                self.new_file = new_file_name + '.' + format_name
                self.full_name_2 = os.path.join(self.dir_name_2, self.new_file)
                shutil.copy(self.full_name, self.full_name_2)
            else:
                format_name = self.file_name.partition(".")[-1]
                file_name = self.file_name.partition(".")[-3]
                self.new_file = file_name + "_copy_1." + format_name
                self.full_name_2 = os.path.join(self.dir_name_2, self.new_file)
                shutil.copy(self.full_name, self.full_name_2)
        else:
            self.new_file = 'not_file'

    def find_files_to_copy(self):

        self.coped_file_list = []
        self.file_dict = {}
        self.format_list = []
        self.coped_file_index = []
        self.name_list = []
        self.not_coped_file_list = []

        for self.file_name in self.file_list:
            full_name_alg = os.path.join(self.dir_name, self.file_name)
            if os.path.isfile(full_name_alg):
                if "_copy_" in self.file_name:
                    file_name_copy = self.file_name.partition(".")[-3]
                    format_name = self.file_name.partition(".")[-1]
                    coped_file_index = file_name_copy.partition("_copy_")[-1]
                    name = self.file_name.partition("_copy_")[-3]
                    if int(coped_file_index) == 1:
                        self.file_dict[name] = [int(coped_file_index)]
                        self.format_list.append(format_name)
                        self.name_list.append(name)
                    else:
                        try:
                            self.file_dict[name].append(int(coped_file_index))
                        except:
                            self.file_dict[name] = [int(coped_file_index)]
                            self.format_list.append(format_name)
                            self.name_list.append(name)
                else:
                    name = self.file_name.partition('.')[-3]
                    format_name = self.file_name.partition('.')[-1]
                    new_file_name = "{0}_copy_1.{1}".format(name, format_name)
                    if not new_file_name in self.file_list:
                        self.not_coped_file_list.append(self.file_name)
        self.file_list.clear()
        if len(self.not_coped_file_list) >= 1:
            self.file_list = self.not_coped_file_list
            self.index_3 = len(self.file_list)
        if len(self.file_dict) >= 1 :
            self.file_list.clear()
            self.index_3 = 0
            for name in self.name_list:
                new_file_name = "{0}_copy_{1}.{2}".format(name, max(self.file_dict[name]), self.format_list[self.index_3])
                self.file_list.append(new_file_name)
                self.index_3 += 1
        if self.index_3 >= 1:
            return True
        else:
            return False

    def copy_algoritm(self):
        try:
            print('Идет подсчет...\r', end='')
            self.index_2 = 0
            if self.find_files_to_copy():
                for self.file_name in self.file_list:
                    self.full_name = os.path.join(self.dir_name, self.file_name)
                    self.copy()
                    if not self.new_file == 'not_file' and self.new_file not in self.file_list:
                        self.index_2 += 1
                        self.coped_file_list.append(self.new_file)
                        self.index = round(self.index_2 / self.index_3 * 100, 1)
                        self.progress_animation(self.lan["91"])
        except FileNotFoundError:
            pass

    def print_result(self):
        if self.index_2 <= 50 and self.index_2 > 0:
            if self.index_2 == 1:
                print("{0}:                     ".format(self.lan["33"]))
            else:
                print("{0}:                     ".format(self.lan["83"]))
            for self.file_name in self.coped_file_list:
                print(" {0}".format(self.yellow.format(self.file_name)))
        wait()
        print("{0}: {1}               ".format(self.lan["61"], self.index_2))

    def copy_in_dir(self):
        print(self.tag .format("{0}:".format(self.lan["55"])))
        if self.dir_name_input_to('{0}  [-->]:'.format(self.lan["53"])):
            if self.dir_name_input_out(self.lan["53"] + '  [<--]:'):
                self.file_list = []
                self.file_list_for_count = []
                try:
                    self.file_list = os.listdir(self.dir_name)
                    self.copy_algoritm()
                    self.print_result()
                except FileNotFoundError:
                    pass

    def copy_file(self):
        print(self.tag .format("{0}:".format(self.lan["12"])))
        if self.dir_name_input_to('{0}  [-->]:'.format(self.lan["53"])):
            if self.dir_name_input_out('{0}  [<--]:'.format(self.lan["53"])):
                self.file_name = input("{0}:".format(self.lan["80"]))
                self.full_name = os.path.join(self.dir_name, self.file_name)
                if os.path.isfile(self.full_name):
                    try:
                        self.file_list = os.listdir(self.dir_name)
                        print("Идет додсчет...\r", end='')
                        name = self.file_name.partition(".")[-3]
                        format_name = self.file_name.partition(".")[-1]
                        if "_copy_" in name:
                            name = name.partitiin("_copy_")[-3]
                        files_list = []
                        index_list = []
                        for file_name in self.file_list:
                            if name in file_name and format_name in file_name:
                                files_list.append(file_name)
                        for file_name_3 in files_list:
                            if "_copy_" in file_name_3:
                                main_name = file_name_3.partition(".")[-3]
                                index = main_name.partition("_copy_")[-1]
                                index_list.append(int(index))
                        if len(index_list) >= 1:
                            self.file_name = "{0}_copy_{1}.{2}".format(name, max(index_list), format_name)
                        self.full_name = os.path.join(self.dir_name, self.file_name)
                        self.copy()
                        if not self.new_file == "not_file":
                            print("{0}                          ".format(self.lan["33"]))
                            print(" {0}".format(self.yellow.format(self.new_file)))
                        else:
                            print(self.lan["90"] + Fore.YELLOW + self.file_name + Fore.WHITE + ".")
                    except:
                        pass
                else:
                    print("Файл \"{}\" не найден.".format(self.file_name))

class Delete_coped_files(Program_functions):

    def __init__(self, lan_p):
        super().__init__(lan_p)

    def count_files_for_delete(self):
        print('Идет подсчет...\r', end='')
        index = 0
        for self.file_name in self.file_list:
            self.full_name = os.path.join(self.dir_name, self.file_name)
            if os.path.isfile(self.full_name):
                if "_copy_" in self.file_name:
                    index += 1
        return index

    def delete(self):
        self.index_2 = 0
        self.deleted_file_list = []
        self.index_3 = self.count_files_for_delete()
        for self.file_name in self.file_list:   
            self.full_name = os.path.join(self.dir_name, self.file_name)
            if os.path.isfile(self.full_name):
                if '_copy_' in self.file_name:
                    os.remove(self.full_name)
                    if not os.path.exists(self.full_name):
                        self.deleted_file_list.append(self.file_name)
                        self.index_2 += 1
                        self.index = round(self.index_2 / self.index_3 * 100, 1)
                        self.progress_animation(self.lan["92"])

    def delete_coped_files(self):
        wait()
        print(self.tag .format("{0}:".format(self.lan["29"])))
        wait()
        if self.dir_name_input_to():
            try:
                self.file_list = os.listdir(self.dir_name)
                self.delete()
                if self.index_2 <= 50 and self.index_2 > 0:
                    print("                                         \r", end='')
                    if self.index_2 == 1:
                        print("{0}:".format(self.lan["46"]))
                    elif self.index_2 > 1:
                        print("{0}:".format(self.lan["51"]))
                    else:
                        pass
                    for self.file_name in self.deleted_file_list:
                        print(" {0}".format(self.yellow.format(self.file_name)))
                wait()
                print("{0}: {1}              ".format(self.lan["31"], self.index_2))
            except FileNotFoundError:
                pass

class Directory_functions(Program_functions):

    def __init__(self, lan_p):

        super().__init__(lan_p)

    def delete_file(self):
        self.file_info_form(self.lan["71"])
        if os.path.isfile(self.full_name):
            try:
                os.remove(self.full_name)
                print("{0}:".format(self.lan["46"]))
                print(self.yellow.format(" {0}".format(self.file_name)))
            except FileNotFoundError:
                pass
        else:
            print("Файл \"{0}\" не найден.".format(self.file_name))

    def create_file(self):
        print(self.tag .format("{0}:".format(self.lan["71"])))
        if self.dir_name_input_to():
            self.file_name = input("{0}:".format(self.lan["32"]))
            self.full_name = os.path.join(self.dir_name, self.file_name)
            try:
                open(self.full_name, "w")
                print(self.lan["33"])
                print(' ' + self.yellow.format(self.file_name))
            except FileNotFoundError:
                pass

    def create_directory(self):
        print(self.tag.format("{0}:".format(self.lan["68"])))
        self.dir_name = input("{0}:".format(self.lan["53"]))
        try:
            os.makedirs(self.dir_name)
            print("{0}:".format(self.lan["40"]))
            print(self.yellow.format(self.dir_name))
        except FileExistsError:
            print(self.lan["43"])

    def find_file(self):
        self.file_info_form(self.lan["79"])
        if os.path.isfile(self.full_name):
            print("{0} {1} {2}".format(self.lan["25"], self.yellow.format(self.file_name), self.lan["81"]))
        else:
            print("{0} {1} {2}".format(self.lan["25"], self.yellow.format(self.file_name), self.lan["82"]))

class Calculator(Program_functions):

    def __init__(self, lan_p):
        self.calc_index = 0
        super().__init__(lan_p)

    def calc_start(self):
        print(self.tag .format(self.lan["35"]))
        try:
            self.calculator(0)
        except:
            pass

    def calc_long(self):
        self.cls()
        Program_GUI(self.lan).header()
        while True:
            try:
                if self.index_2 == 1:
                    self.calculator(1)
                else:
                    self.index_2 = 0
                    self.calculator(0)
                self.cls()
                Program_GUI(self.lan).header()
            except ValueError:
                print(self.lan["58"])
                break
            except KeyboardInterrupt:
                break

    def calculator(self, modification):
        print(self.lan["42"])
        a, sy, b = '', '', ''
        if modification == 0:
            nums = input(">")
            if nums == 'long':
                self.calc_long()
            else:
                a, sy, b = nums.split(' ')
            
        elif modification == 1:
            a = self.calc_index
            nums = input(" >{0} ".format(a))
            sy, b = nums.split(' ')
        a, b = float(a), float(b)
        if sy == "+":
            self.count(a, b, "+")
            self.answer__0()
        elif sy == "-":
            self.count(a, b, "-")
            self.answer__0()
        elif sy == "*":
            self.count(a, b, "*")
            self.answer__0()
        elif sy == "^":
            self.count(a, b, "**")
            self.answer__0()
        elif sy == "/":
            if not b == 0:
                self.count(a, b, "/")
            else:
                print(self.lan["64"])
        else:
            pass
        if not modification == 1:
                print("{0}".format(self.green.format("{0} {1}".format(self.lan["39"], self.calc_index))))
                self.index_2 = 1

    def count(self, a, b, action):
        if action == "+":
            self.calc_index = a + b
        elif action == "-":
            self.calc_index = a - b
        elif action == "*":
            self.calc_index = a * b
        elif action == "**":
            self.calc_index = a ** b
        elif action == "/":
            if b == 0:
                print(self.lan["64"])
            else:
                self.calc_index = a / b

    def answer__0(self):
        if self.calc_index % 1 == 0:
            self.calc_index = round(self.calc_index)

    def cls(self):
        if __name__ == '__main__':
            Other.cls(self)

class Other(Program_functions):

    def __init__(self, lan_p):

        super().__init__(lan_p)

    def print_language_frases(self):
        print(self.tag .format(self.lan["38"] + ":"))
        x = 1
        for f in range(len(self.lan)):
            h = self.lan[str(f + 1)]
            print(f"{x}: {h}")
            x += 1

    def cls(self):
        print("\033[2J")

    def no(self):
        print(self.lan["41"])
        time.sleep(.5)
        print("\033[2J")
        exit(0)

    def path_python(self):
        print(self.tag .format(self.lan["30"] + ":"))
        for f in sys.path:
            print(Fore.YELLOW + " " + f + Fore.WHITE)

    def debug(self):
        vesion = str(VERSION_PROJECT)
        release = str(RELEASE_DATE)
        system = str(sys.platform)
        time = str(datetime.now())
        print(self.tag .format('Debug'))
        print(" version: " + vesion)
        print(" release date: " + release)
        print(" time: " + time)
        print(" system: " + system)

    def wait(self):
        time.sleep(.05)

    def exit(self):
        print("\033[2J")
        exit(0)
        os.abort()
