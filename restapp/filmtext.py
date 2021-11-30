import requests
from bs4 import BeautifulSoup
import mysql.connector


class MoviesClass():

    def getURL(self):
        #film sitesine git
        self.url = requests.get("https://www.hdfilmcehennemi.tv/category/film/page/8")
        #html parse et
        self.soup =BeautifulSoup(self.url.content,"html.parser")

        
    def getText(self):
        #parse edilen func çalıştır
        self.getURL()
        #boş bir liste oluştur
        liste = []

        #film sitesindeki ilgili text yerini al ve loop ile dön
        for link in self.soup.find_all('div',attrs={'class':'poster-desc'}):
            #boş listeye ekle
            liste.append(link.text)
        #geri dolu listeyi dön
        return liste


    

    def veritabanı_ekle(self):
        #veri tabanına baglan
        connection = mysql.connector.connect(
                host = "localhost",
                user = "mert",
                password = "xxx123",
                database = "fılm",
                )
        

        cursor = connection.cursor()
        #veri tabanına ekle
        insertTextSQL = "INSERT INTO `fılm`.`movietext` (`text`) VALUES (%s)"
        selectTextSQL = "SELECT * FROM `fılm`.`movietext` WHERE text = %s"
        #döngü ile dön
        for text in self.getText():
            cursor.execute(selectTextSQL,(text,))
            result = cursor.fetchone()
            if result:#Eğer aynı text'den varsa devam et
                continue
            #yoksa veritabanına ekle
            cursor.execute(insertTextSQL,(text,))

        
        
        
        connection.commit() #YAPILAN DEĞİŞİKLİKLERİ KAYDET
        connection.close() #VERİ TABANINI KAPAT


a = MoviesClass()
a.veritabanı_ekle()





