import os,shutil,sys
# Задача-1:

# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


#print(dir_list)

#print(os.getcwd())
def create_dirs(*dirs):
    result = ""
    for dir in dir_list:
        try:
            path = os.path.join(os.getcwd(),dir)
            os.mkdir(path)
        except FileExistsError:
            result += " {}".format(dir)
    if result:
        result = "Folders exists: " + result
    else:
        result = "all created"
    return result

def remove_dirs(*dirs):
    result = ""
    for dir in dirs:
        try:
            path = os.path.join(os.getcwd(),dir)
            os.rmdir(path)
        except:
            result += " {}".format(dir)
    if result:
        return "error! folders not empty: " + result
    else:
        return "all eliminated"

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def get_dir_list(path):
    result = []
    dir_content = os.listdir(path)
    for dir in dir_content:
        if os.path.isdir(dir):
            result.append(dir)
    return result

def get_dir_content(path):
    result = []
    dir_content = os.listdir(path)
    result = "\n".join(dir_content)
    return result


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

#file_path = os.path.realpath(__file__)
#with open(file_path,"rt", encoding="utf-8") as file:
#   content = file.read()
#print(file)

#shutil.copyfile(os.path.realpath(__file__),os.path.join(file[0]+"-copy",file[1]))
#def current_file_copy():
#    try:
#        fname, ext = __file__.split(".")
#        file_copy = f"{fname}_copy.{ext}"
#        print(new_file_name)
#        shutil.copyfile(__file__,file_copy)
#    except:
#        return "ошибка"
#    else:
#        return "ок"
#print(current_file_copy)



def file_copy(filename):
    try:
        fname, ext =filename.split(".")
        file_copy = f"{fname}_copy.{ext}"
        shutil.copyfile(filename, file_copy)
    except:
        return "Невозможно скопировать файл"
    else:
        return "Скопировано верно"

def remove_file(*file):
    result = ""
    for dir in dirs:
        try:
            path = os.path.join(os.getcwd(),dir)
            os.rmdir(path)
        except:
            result += " {}".format(dir)
    if result:
        return "error! folders not empty: " + result
    else:
        return "all eliminated"


if __name__ == "__main__":
    dir_list = [ "dir_{}".format(x) for x in range(1,10)]
    print(get_dir_list(os.getcwd()))
    print(create_dirs(*dir_list))
    print(remove_dirs(*dir_list))
    print(file_copy(__file__))
    print(get_dir_content(os.getcwd()))
    print(__name__)