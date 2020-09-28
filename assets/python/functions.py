from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

class MyFunctions():
    def __init__(self):
        super().__init__()
        self.Dolar = self.DolarParse().replace(",", ".")
        self.Euro = self.EuroParse().replace(",", ".")
        self.Altin = self.AltinParse().replace(",", ".")
        self.Gumus = self.GumusParse().replace(",", ".")

    def DolarParse(self):
        pasteURL = "http://tr.investing.com/currencies/usd-try"
        data = urlopen(Request(pasteURL, headers={'User-Agent': 'Mozilla'})).read()
        parse = BeautifulSoup(data)
        for dolar in parse.find_all('span', id="last_last"):
            liste = list(dolar)
            return liste[0]


    def EuroParse(self):
        pasteURL = "http://tr.investing.com/currencies/eur-try"
        data = urlopen(Request(pasteURL, headers={'User-Agent': 'Mozilla'})).read()
        parse = BeautifulSoup(data)
        for euro in parse.find_all('span', id="last_last"):
            liste = list(euro)
            return liste[0]

    def AltinParse(self):
        pasteURL = "http://tr.investing.com/currencies/gau-try"
        data = urlopen(Request(pasteURL, headers={'User-Agent': 'Mozilla'})).read()
        parse = BeautifulSoup(data)
        for euro in parse.find_all('span', id="last_last"):
            liste = list(euro)
            return liste[0]

    def GumusParse(self):
        pasteURL = "http://tr.investing.com/currencies/xagg-try"
        data = urlopen(Request(pasteURL, headers={'User-Agent': 'Mozilla'})).read()
        parse = BeautifulSoup(data)
        for euro in parse.find_all('span', id="last_last"):
            liste = list(euro)
            return liste[0]


    def str2Num(self,string):
        try:
            return int(string)
        except ValueError:
            try: 
                return float(string) 
            except ValueError:
                return "Undefined Variable"               