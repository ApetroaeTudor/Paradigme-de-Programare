from abc import ABC, abstractmethod
import pandas as pd
import copy
import html
import json

class File(ABC):
    def __init__(self):
        self.title=""
        self.author=""
        self.paragraphs=[]
    def read_file_from_stdin(self):
        self.title=input("Read title: ")
        self.author=input("Read author: ")
        nr_of_paragraphs=input("Read nr of paragraphs: ")
        for i in range(0,int(nr_of_paragraphs)):
            paragraph=input("read paragraph {0}: ".format(i+1) )
            self.paragraphs.append(paragraph)

class FileFactory():
    @staticmethod
    def factory(file_type:str)->File:
        lower_file_type=file_type.lower()
        if(lower_file_type=="html"):
            return HTMLFile()
        elif(lower_file_type=="json"):
            return JSONFile()
        elif(lower_file_type=="article"):
            return ArticleTextFile()
        elif(lower_file_type=="blog"):
            return BlogTextFile()
        else:
            raise Exception("Unknown File Type: {0} ".format(lower_file_type))
        


class HTMLFile(File):
    def __init__(self):
        super().__init__()
    def print_html(self):
        h_title=html.escape(self.title if self.title else "Untitled")
        h_author=html.escape(self.author if self.author else "No author")
        html_output = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{h_title}</title>
</head>
<body>
    <h1>{h_title}</h1>
    <p><em>By: {h_author}</em></p>
"""
        for p in self.paragraphs:
            h_paragraph=html.escape(p)
            html_output += f"    <p>{h_paragraph}</p>\n"
        html_output += """</body>
</html>"""
        print(html_output)




class JSONFile(File):
    def __init__(self):
        super().__init__()
    def print_json(self):
        data_to_serialize={
            "title":self.title if self.title else "Untitled",
            "author":self.author if self.author else "No author",
            "paragraphs":self.paragraphs
        }

        json_output=json.dumps(data_to_serialize,indent=4)
        print(json_output)

class TextFile(File):
    def __init__(self):
        self.template=""
        super().__init__()
    def clone(self):
        return copy.deepcopy(self)
    @abstractmethod
    def print_text(self):
        pass

class ArticleTextFile(TextFile):
    def __init__(self):
        self.template="article"
        super().__init__()
    def print_text(self):
        print("\t{0}\n\t\tby {1}\n".format(self.title,self.author))
        for p in self.paragraphs:
            print(p)

class BlogTextFile(TextFile):
    def __init__(self):
        self.template="blog"
        super().__init__()
    def print_text(self):
        print(self.title)
        for p in self.paragraphs:
            print(p)
        print("\nWritten by {0}".format(self.author))