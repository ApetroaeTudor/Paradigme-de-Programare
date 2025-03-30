from abc import ABC,abstractmethod

class GenericFile(ABC):
    @abstractmethod
    def get_path(self):
        raise NotImplementedError("Methods must be implemented!")
    def get_freq(self):
        raise NotImplementedError("Methods must be implemented!")

    def __repr__(self):
        return "File "





class TextASCII(GenericFile):
    path_absolut:str
    frecvente:list[int]

    def __init__(self,path,freq):
        self.path_absolut=path
        self.frecvente=freq

    def get_path(self):
        return self.path_absolut
    def get_freq(self):
        return self.frecvente

    def __repr__(self):
        return super().__repr__()+"ASCII:"+"\nPathAbsolut " + self.path_absolut+"\nFrecvente: " + ', '.join(map(str,self.frecvente))


class XMLFile(TextASCII):
    first_tag:str

    def __init__(self,path,freq,first_tag):
        super().__init__(path,freq)
        self.first_tag=first_tag

    def get_first_tag(self):
        return self.first_tag

    def __repr__(self):
        return super().__repr__()+"\nXML:"+"\nFirstTag:"+self.first_tag




class TextUNICODE(GenericFile):
    path_absolut: str
    frecvente: list[float]

    def __init__(self, path, freq):
        self.path_absolut = path
        self.frecvente = freq

    def get_path(self):
        return self.path_absolut

    def get_freq(self):
        return self.frecvente

    def __repr__(self):
        return super().__repr__()+"UNICODE:"+"\nPathAbsolut: " + self.path_absolut+"\nFrecvente: " + ', '.join(map(str,self.frecvente))






class Binary(GenericFile):
    path_absolut: str
    frecvente: list[float]

    def __init__(self, path, freq):
        self.path_absolut = path
        self.frecvente = freq

    def get_path(self):
        return self.path_absolut

    def get_freq(self):
        return self.frecvente

    def __repr__(self):
        return super().__repr__()+" Binary: "+ "\nPathAbsolut: " + self.path_absolut+"\nFrecvente: " + ', '.join(map(str,self.frecvente))

class BMP(Binary):
    width:int
    height:int
    bpp:int

    def __init__(self,path,freq,width,height,bpp):
        super().__init__(path,freq)
        self.width=width
        self.height=height
        self.bpp=bpp

    def __repr__(self):
        return super().__repr__() + "\nBMP: " + "\nWidth: "+ str(self.width) +"; Height: " + str(self.height)+"; BPP: " + str(self.bpp)


