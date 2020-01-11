import os

def file_size(filename):
    try:
        statinfo = os.stat(filename)
        return statinfo.st_size
    except FileNotFoundError as error:
        print(error)
        return None
    except Exception as error:
        print(error)
        return None

file_size("ex_005_file_size.py")
# will return 460

file_size("file_that_does_not_exist.txt")
# will print [Errno 2] No such file or directory: 'file_that_does_not_exist.txt'
# and return None
