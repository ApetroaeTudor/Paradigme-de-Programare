import os

path_list = ['file1.txt','file2.c','notExistingFile','file3.html','file4.txt']

def generatorExistingFilter(iterable_list):
    for elem in iterable_list:
         if os.path.exists(elem):
              yield elem

def generatorTxtFormatFilter(iterable_list):
    for elem in iterable_list:
            if os.path.splitext(elem)[1].lower() == '.txt':
                yield elem

def generatorLineCounter(iterable_list):
    for elem in iterable_list:
        with open(elem,'r') as f:
            nr_of_lines=0
            for line in f:
                nr_of_lines+=1
        yield (os.path.basename(elem),nr_of_lines)

if __name__ == '__main__':
    existing_files = generatorExistingFilter(path_list)
    txt_files = generatorTxtFormatFilter(existing_files)
    numbers_of_lines = generatorLineCounter(txt_files)

    for elem in numbers_of_lines:
        print(elem)    