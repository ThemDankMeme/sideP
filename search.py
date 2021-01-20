import os
import fnmatch
import re
import shutil

'''
def find_folder():
    print(os.getcwd())
    os.chdir('../Complete-Python-3-Bootcamp-master/12-Advanced Python Modules/08-Advanced-Python-Module-Exercise')
    print(os.listdir(os.getcwd()))
    my_file = ''
    my_folder = ''
    step = ''
    flag = False
    for file in os.listdir(os.getcwd()):
        if fnmatch.fnmatch(file, '*.zip'):
            my_file = file
            print(file)
    for name in os.listdir(os.getcwd()):
        if name == 'my_folder':
            flag = True
            os.chdir('my_folder')
            break
        else:
            flag = False
    if not flag:
        shutil.unpack_archive(my_file, 'my_folder', 'zip')
        os.chdir('my_folder')
    print(os.listdir(os.getcwd()))
    for name in os.listdir(os.getcwd()):
        my_folder = name
    for name in os.listdir(os.getcwd()):
        step = name
        #os.chdir(step)
    print(os.listdir(os.getcwd()))
    print(step)
    for folder, sub_folders, files in os.walk(step):
        print("Currently looking at folder: " + folder)
        print('\n')
        print("THE SUB_FOLDERS ARE: ")
        for sub_fold in sub_folders:
            print("\t Sub_folder: " + sub_fold)
        print('\n')
        print('THE FILES ARE: ')
        os.chdir(folder)
        for f in files:
            if fnmatch.fnmatch(f, '*.txt'):
                file_name = f
                d = open(file_name, "r")
            phone_patter = r'(\d{3}-\d{3}-\d{4})'
            some_number = re.search(phone_patter, d.read())
            d.close()
            if some_number:
                print(some_number)
                break
            else:
                pass
            print("\t File: " + f)
        print(os.getcwd())
        os.chdir('../')
        print(os.getcwd())
        print('\n')
'''


def find_folder():
    os.chdir('../Complete-Python-3-Bootcamp-master/12-Advanced Python Modules/08-Advanced-Python-Module-Exercise')
    os.listdir(os.getcwd())
    found = False
    some_folder = ''
    for folders in os.listdir(os.getcwd()):
        if folders == 'my_folder':
            found = True
            break
        elif fnmatch.fnmatch(folders, '*.zip'):
            some_folder = folders
        else:
            continue
    if found:
        pass
    else:
        shutil.unpack_archive(some_folder, 'my_folder', 'zip')
    os.chdir('my_folder')
    for name in os.listdir(os.getcwd()):
        os.chdir(name)
    print(os.listdir(os.getcwd()))
    for folder in os.listdir(os.getcwd()):
        print(folder)
        os.chdir(folder)
        for files in os.listdir(os.getcwd()):
            d = open(files, 'r')
            phone_pat = r'\d{3}-\d{3}-\d{4}'
            find = re.findall(phone_pat, d.read())
            d.close()
            if find:
                print(find)
                return find
            else:
                continue
        os.chdir('../')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    find_folder()