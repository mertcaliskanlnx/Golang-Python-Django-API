import requests
from bs4 import BeautifulSoup
import mysql.connector


class MoviesClass():
    
    def getURL(self):
        self.url = requests.get("https://www.hdfilmcehennemi.tv/category/film/page/8")
        self.soup = BeautifulSoup(self.url.content,"html.parser")

        
    def getMovie(self):
        self.getURL()
        liste = []

        for link in self.soup.find_all('div',attrs={'class':'poster-info'}):
            liste.append(link.h2.text)

        return liste
    


    def veritabanı_ekle(self):
        connection = mysql.connector.connect(
                host = "localhost",
                user = "mert",
                password = "xxx123",
                database = "fılm",
        )

        cursor = connection.cursor()

        insertSQL = "INSERT INTO `fılm`.`movietitle` (`title`) VALUES (%s)"
        selectSQL = "SELECT * FROM `fılm`.`movietitle` WHERE title = %s"

        for title in self.getMovie():
            cursor.execute(selectSQL,(title,))
            result = cursor.fetchone()
            if result:
                print("'{}' isimli bir film başlığı var, db ye eklemeden dongünün başına gidilecek".format(title)) 
                continue
            cursor.execute(insertSQL,(title,))
            print("'{}' isimli bir film başlığı yok, db ye eklendi".format(title))

        
        
        
        connection.commit() #YAPILAN DEĞİŞİKLİKLERİ KAYDET
        connection.close() #VERİ TABANINI KAPAT


a = MoviesClass()
a.veritabanı_ekle()

