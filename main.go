package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

//json dataları yakalamak için struct oluşturuyoruz
type Response struct {
	Status string `json:"status"`
	Data   []struct {
		Id    int     `json:"id"`
		Title string  `json:"title"`
		Text  string  `json:"text"`
		Price float64 `json:"price"`
	} `json:"data"`
}

func JsonGet(i interface{}) string {
	//DJANGO'DAKİ REST APİYE İSTEK ATIYORUZ
	resp, err := http.Get("http://127.0.0.1:8000/api/movie-items/?format=json")
	//HATA İLE KARŞILAŞIRSAK BURDA YAKALIYORUZ
	if err != nil {
		fmt.Println("No response from request")
	}
	//EN SON YAPILACAK İŞLEM
	defer resp.Body.Close()
	//BYTE OLARAK GELİYOR
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Println("HATA")
	}

	return string(body)

}

func homepage(w http.ResponseWriter, r *http.Request) {

	var result Response
	//JSONNGET'DEN GELEN DATAYI BURADA byte olarak ayrıştırıyoruz ve resulta atıyoruz
	if err := json.Unmarshal([]byte(JsonGet(result)), &result); err != nil {
		fmt.Println("JSON HATA!")

	}
	//yukarıda Response Struct içindeki data ya erişmek için yukarıda result değişkenine atadık üzerinde bir döngğ kuruyoruz
	for _, rec := range result.Data {
		//EĞER PRİCE 1.0 İSE
		if rec.Price == 1.0 {
			//PRİCE'A 3 EKLE
			rec.Price += 1 * 3
		}
		//RESPONSE OLARAK DATAYI DÖNÜYORUZ
		fmt.Fprint(w, PrettiyPrint(rec))

	}
	//BİR GET İSTEĞİ ATTIGIMIZDA BU ÇALIŞICAK
	fmt.Println("İstek GELDİ")
}

func handleRequest() {
	myRouter := mux.NewRouter().StrictSlash(true)
	//ANASAYFA YÖNLENDİRMESİ
	myRouter.HandleFunc("/", homepage)
	//SERVER DİNLEME localhost:10000
	log.Fatal(http.ListenAndServe(":10000", myRouter))

}

func main() {

	handleRequest()
}

func PrettiyPrint(i interface{}) string {
	s, _ := json.MarshalIndent(i, "", "\t")
	return string(s)
}
