from os import listdir, path
dirs = [dir for dir in listdir() if path.isdir(dir)]
print(dirs)
