# File System Manager for reading, writing, and modifying files
import os

# whis will check if a file and its folder path exists
# if not, it will create the file and its folder path
def create(file_path):
    directory = "/".join(file_path.split("/")[:-1])# get the directory path 
    file = file_path.split("/")[-1] # get the file name
    if not os.path.exists(directory): # check if the directory do not exists
        os.makedirs(directory) # create the directory
        open(f'{directory}/{file}', "w").close() # create the file

def write(path, content): # this will append contents to a file
    # if the file does not exist, it will create it

    # file = open(path, "at") # open the file in append text mode
    # file.write(content) # write the content to the file
    # file.close() # close the file

    with open(path, "at") as file: # open the file in append text mode
        file.write(content) # write the content to the file

def read(path):
    # file = open(path, "rt") # open the file in read text mode
    # content = file.read() # read the content of the file
    # file.close() # close the file
    # return content # return the content of the file

    with open(path, "rt") as file: # open the file in read text mode
        content = file.read() # read the content of the file
    return content # return the content of the file