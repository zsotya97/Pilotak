import datetime as dt
class Adatok(object):
    def __init__(self, sor):
        splitteles = sor.split(";")
        self.Nev = splitteles[0]
        self.Szuletes = dt.datetime.strptime(splitteles[1],"%Y.%m.%d")
        self.Nemzetiseg = splitteles[2]
        if(splitteles[3]==""):self.Rajtszam  = 0
        else: self.Rajtszam  = int(splitteles[3])
