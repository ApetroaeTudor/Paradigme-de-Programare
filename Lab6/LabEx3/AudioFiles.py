class AudioFile:
    def __init__(self,filename):
        if not filename.endswith(self.ext):
            raise Exception("Format nesuportat")
        self.filename=filename

class MP3File(AudioFile):
    ext="mp3"

    def play(self):
        print("se canta {} un mp3".format(self.filename))


class WavFile(AudioFile):
    ext="wav"

    def play(self):
        print("Se canta {} un wav".format(self.filename))

class OggFile(AudioFile):
    ext="ogg"

    def play(self):
        print("Se canta {} un ogg".format(self.filename))


class FlacFile:
    def __init__(self,filename):
        if not filename.endswith(".flac"):
            raise Exception("Format necunoscut")
        self.filename=filename

    def play(self):
        print("Se canta {} un flac".format(self.filename))

