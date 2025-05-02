import requests as re
from abc import ABC,abstractmethod
from pathlib import Path
import time
import requests


expiration_delay = float(5)


class URL:
    def __init__(self,url:str):
        self.full_url = url
        self.short_name = url.split("/")[2].split(".")[0]

class Subject(ABC):
    @abstractmethod
    def store_entry(self,url:str):
        pass
    def read_entry(self,url:str):
        pass

class Proxy(Subject):
    def __init__(self):
        self.real_subject = None
        self.dir_path = Path("Cache")

    def init_real_subject(self):
        if self.real_subject == None:
            print("Se instantiaza RealSubj la prima utilizare..")
            self.real_subject = RealSubject()
    
    def store_entry(self,url:str):
        url_struct = URL(url)

        for file in self.dir_path.iterdir():
            if url_struct.short_name in str(file):
                timestamp = str(file).split("_")[1]
                current_time = time.time()
                #se actualizeaza cererile mai vechi de 30 de secunde
                if current_time - float(timestamp) > expiration_delay:
                    print("Cererea este invechita, se cheama RealSubject pentru a o actualiza")
                    self.init_real_subject()
                    self.real_subject.update_entry(url)
                    return
                else:
                    print("Cererea a fost deja facuta in mai putin de 30 de secunde\n") 
                    return
                    
        print("Cererea nu e inregistrata, se apeleaza RealSubject pentru a o scrie in Cache")
        self.init_real_subject()
        self.real_subject.store_entry(url)

    def read_entry(self, url):
        url_struct = URL(url)
        for file in self.dir_path.iterdir():
            if url_struct.short_name in str(file):
                timestamp = str(file).split("_")[1]
                current_time = time.time()
                if current_time - float(timestamp) > expiration_delay:
                    print("Cererea este invechita, se cheama RealSubject pentru a o actualiza")
                    self.init_real_subject()
                    self.real_subject.update_entry(url)
                    print("Acum cererea este actualizata, se apeleaza RealSubject pentru a o citi")
                    self.real_subject.read_entry(url)
                    return
                else:
                    print("Cererea este valida, se cheama RealSubject pentru a o citi")
                    self.init_real_subject()
                    self.real_subject.read_entry(url)
                    return
            
        print("Cererea nu e inregistrata, se apeleaza RealSubject pentru a o inregistra")
        self.init_real_subject()
        self.real_subject.store_entry(url)
        print("Cererea acum e initializata, se apeleaza RealSubject pentru a o citi")
        self.real_subject.read_entry(url)


class RealSubject(Subject):
    def __init__(self):
        self.dir_path = Path("Cache")
    
    def store_entry(self, url):
        url_struct = URL(url)
        current_time = time.time()
        file_name = str(self.dir_path) + "/" + url_struct.short_name + "_" + str(current_time)
        with open(file_name, 'w') as f:
            f.write(requests.get(url_struct.full_url).text)

    def update_entry(self,url):
        url_struct = URL(url)
        current_time = time.time()
        file_name = str(self.dir_path) + "/" + url_struct.short_name + "_" +str(current_time)

        for file in self.dir_path.iterdir():
            if url_struct.short_name in str(file):
                file.unlink()
                print("File with url: {} deleted in RealSubject".format(url_struct.full_url))
                with open(file_name,'w') as f:
                    f.write(requests.get(url_struct.full_url).text)
                    print("File with url: {} updated in RealSubject".format(url_struct.full_url))

    def read_entry(self, url):
        url_struct = URL(url)
        for file in self.dir_path.iterdir():
            if url_struct.short_name in str(file):
                print("Reading from file..")
                with open(str(file),'r') as f:
                    print(f.read())