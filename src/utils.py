import os

def get_excel_file_names(basedir, prefix): # to avoid writting the name of every single file
        file_names = []
        for filename in os.listdir(basedir):
            if filename.startswith(prefix):
                file_names.append(filename.split('.')[0])  # Remove the file extension
        return file_names