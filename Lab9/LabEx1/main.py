from File import *

if __name__=="__main__":
    my_html_file=FileFactory.factory("html")
    my_html_file.read_file_from_stdin()
    my_html_file.print_html()